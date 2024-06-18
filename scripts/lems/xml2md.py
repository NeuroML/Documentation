#!/usr/bin/env python3
"""
Convert xml source annotations from LEMS to markdown/myst

File: scripts/lems/xml2md.py

Copyright 2023 NeuroML contributors
"""

import logging
import tempfile
import subprocess
import re
import lxml
import lxml.etree as ET
import xmltodict
from datetime import date
import asttemplates
from collections import OrderedDict


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)


# pages to which different sections should belong
# key is the name in the annotated source, list entries are [heading,
# description]
sections_pages = {
    "root": ["Model structure", "Models can be spread over multiple files. The root element in each file is Lems."],
    "unitsdimensions": ["Units and dimensions", ""],
    "componenttypes": ["Defining component types", ""],
    "dynamics": ["Dynamics", ""],
    "structure": ["Structure", ""],
    "simulation": ["Simulation", ""],
    "procedure": ["Procedure", ""],
    "geometry": ["Geometry", ""],
    "components": ["Defining Components", ""]
}

lems_branch = "master"
lems_version = "0.7.6"
GitHubRepo = "https://github.com/LEMS/LEMS.git"
lems_date = date.today().strftime("%d/%m/%y")
lems_commit = ""

parsed_data = {}

srcfile = "sourceannotations.xml"

comp_type_schema = {}

def get_schema_doc(schemafile):
    """Get schemas for everything

    :param schemafile: path to the XSD schema file
    """
    print(ET.__file__)
    parser = lxml.etree.XMLParser(remove_comments=True,
                                  remove_blank_text=True, ns_clean=True)
    try:
        tree = ET.parse(schemafile, parser=parser)
        root = tree.getroot()
    except ET.XMLSyntaxError as e:
        print(f"Could not parse file {schemafile}: {e}")
    namespaces = root.nsmap

    # currently unused
    for simple_type in root.findall("xs:simpleType", namespaces=namespaces):
        simple_type_str = ET.tostring(simple_type, pretty_print=True,
                                      encoding="unicode",
                                      xml_declaration=False)

        # needs to be lowerCamelCase to match XML core types
        type_name = simple_type.attrib['name'].lower().replace("nml2quantity_", "")
        comp_type_schema[type_name] = re.sub(r"Type.*name=",r"Type name=", simple_type_str)

    for complex_type in root.findall("xs:complexType", namespaces=namespaces):
        for node in complex_type:
            if "annotation" in str(node.tag) or "documentation" in str(node.tag):
                complex_type.remove(node)

        complex_type_str = ET.tostring(complex_type, pretty_print=True,
                                       encoding="unicode",
                                       xml_declaration=False)
        # needs to be lowerCamelCase to match XML core types
        type_name = complex_type.attrib['name'].lower()
        comp_type_schema[type_name] = re.sub(r"Type.*name=",r"Type name=", complex_type_str)


def main(srcdir, destdir):
    """Main runner function.

    :param arg1: TODO
    :returns: TODO

    """
    # If not defined or empty, download a new copy to a temporary directory
    if not srcdir or src == "":
        print("No src directory specified. Cloning NeuroML2 repo")
        tempdir = tempfile.TemporaryDirectory()
        tmpsrcdir = tempdir.name
        print("Temporariy directory: {}".format(tmpsrcdir))
        clone_command = ["git", "clone", "--depth", "1", "--branch", lems_branch, GitHubRepo, tmpsrcdir]
        subprocess.run(clone_command)
    else:
        tmpsrcdir = srcdir

    # TODO: add LEMS examples
    #  exampledirs = [tmpsrcdir + "/examples/", tmpsrcdir + "/LEMSexamples/"]
    exampledirs = [tmpsrcdir + "/examples/"]
    xsdsrc = tmpsrcdir + f"/Schemas/LEMS/LEMS_v{lems_version}.xsd"

    # Get current commit
    commit_command = ["git", "log", "-1", "--pretty=format:%H"]
    output = subprocess.run(commit_command, capture_output=True,
                            cwd=tmpsrcdir, text=True)
    lems_commit = output.stdout

    # populate our page info
    with open(srcfile, 'r') as ast_doc:
        elementtypes = xmltodict.parse(ast_doc.read())['ElementTypes']['ElementType']
        for et in elementtypes:
            try:
                parsed_data[et['@section']].append(et)
            except KeyError:
                parsed_data[et['@section']] = []
                parsed_data[et['@section']].append(et)

    # add Include
    parsed_data['root'].append(
        OrderedDict(
            {
                '@name': 'Include',
                'Info': 'Include LEMS files in other LEMS files. Files are included where the Include declaration occurs.  The enclosing Lems block is stripped off and the rest of the content included as is',
                'Property': OrderedDict(
                    {
                        '@name': 'file',
                        '@type': 'String',
                        '#text': 'the name or relative path of a file to be included'
                    }
                )
            }
        )
    )

    logger.debug(parsed_data)

    # start
    get_schema_doc(xsdsrc)

    # render templates
    for pg, pginfo in sections_pages.items():
        outputfile = "{}/{}.md".format(destdir, pginfo[0].replace(" ", ""))
        with open(outputfile, 'w') as ast_doc:
            print(
                asttemplates.page_header.render(section_data=pginfo,
                                                lems_date=lems_date,
                                                lems_commit=lems_commit,
                                                lems_version=lems_version,
                                                lems_branch=lems_branch),
                file=ast_doc)
            for et in parsed_data[pg]:
                print(f"Rendering {et['@name']}")
                print(
                    asttemplates.elementtype.render(et=et),
                    file=ast_doc)

                # if the component has schema documentation, add that, otherwise
                comp_type_schemadoc = None
                # skip
                try:
                    comp_type_schemadoc = comp_type_schema[et['@name'].lower()]
                    logger.debug(f"Schema doc for {et['@name']}")
                    logger.debug(comp_type_schemadoc)
                except KeyError:
                    logger.warning(f"No schema doc found for {et['@name']}")

                if 'Property' in et or 'ListProperty' in et or comp_type_schemadoc is not None:
                    print("""`````{tab-set}""", end="", file=ast_doc)

                try:
                    if isinstance(et['Property'], list):
                        props=et['Property']
                    else:
                        props=[et['Property']]
                    print(f" - {len(props)} properties: {props}")
                    print(
                        asttemplates.prop.render(props=props),
                        file=ast_doc)
                except KeyError:
                    pass

                try:
                    if isinstance(et['ListProperty'], list):
                        lprops=et['ListProperty']
                    else:
                        lprops=[et['ListProperty']]
                    print(f" - {len(lprops)} properties: {lprops}")
                    print(
                        asttemplates.listprop.render(lprops=lprops),
                        file=ast_doc)
                except KeyError:
                    pass

                if comp_type_schemadoc is not None:
                    print(asttemplates.schema_quote.render(schemadoc=comp_type_schemadoc), file=ast_doc)

                # process them, close tab-set
                if 'Property' in et or 'ListProperty' in et or comp_type_schemadoc is not None:
                    print("""`````""", end="", file=ast_doc)


# print(parsed_data)

if __name__ == "__main__":
    # src = "/home/asinha/Documents/02_Code/00_mine/NeuroML/software/NeuroML2/"
    src = None
    destdir = "../../source/Userdocs/LEMS_elements/"
    main(src, destdir)
