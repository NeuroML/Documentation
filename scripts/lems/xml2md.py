#!/usr/bin/env python3
"""
Convert xml source annotations from LEMS to markdown/myst

File: scripts/lems/xml2md.py

Copyright 2023 NeuroML contributors
"""

import xmltodict
from datetime import date
import asttemplates
from collections import OrderedDict


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

todays_date = date.today().strftime("%d/%m/%y")
parsed_data = {}

srcfile = "sourceannotations.xml"
destdir = "../../source/Userdocs/LEMS_elements/"

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

print(parsed_data)

# render templates
for pg, pginfo in sections_pages.items():
    outputfile = "{}/{}.md".format(destdir, pginfo[0].replace(" ", ""))
    with open(outputfile, 'w') as ast_doc:
        print(
            asttemplates.page_header.render(section_data=pginfo, todays_date=todays_date),
            file=ast_doc)
        for et in parsed_data[pg]:
            print(f"Rendering {et['@name']}")
            print(
                asttemplates.elementtype.render(et=et),
                file=ast_doc)
            if 'Property' in et or 'ListProperty' in et:
                print("""`````{tab-set}""", end="", file=ast_doc)

            try:
                if type(et['Property']) == list:
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
                if type(et['ListProperty']) == list:
                    lprops=et['ListProperty']
                else:
                    lprops=[et['ListProperty']]
                print(f" - {len(lprops)} properties: {lprops}")
                print(
                    asttemplates.listprop.render(lprops=lprops),
                    file=ast_doc)
            except KeyError:
                pass

            # process them, close tab-set
            if 'Property' in et or 'ListProperty' in et:
                print("""`````""", end="", file=ast_doc)


# print(parsed_data)
