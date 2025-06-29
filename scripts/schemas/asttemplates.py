#!/usr/bin/env python3
"""
Templates for use in the ast generator

File: ast-templates.py

Copyright 2023 NeuroML contributors
"""


from lems.model.dynamics import OnStart
from lems.model.dynamics import OnCondition
from lems.model.dynamics import OnEvent
from lems.model.dynamics import OnEntry
from lems.model.dynamics import Transition
from lems.model.dynamics import StateAssignment
from lems.model.dynamics import EventOut
import textwrap
from jinja2 import Environment


def get_lems_type(variable):
    """Return the type of the event_handler.

    To be used as a filter in the templates below since Jinja does not include
    all Python built-ins, like isinstance.

    https://jinja.palletsprojects.com/en/2.11.x/api/?highlight=globals#writing-filters

    This is better than trying to use isinstance in the templates because to do
    that all the LEMS model will have to be added to the Jinja globals.
    https://groups.google.com/g/pocoo-libs/c/99YXzP8RpFw

    :param variable: variable to test
    :type variable: object
    :returns: string name of class that the object is of

    """
    if isinstance(variable, OnStart):
        return "OnStart"
    if isinstance(variable, StateAssignment):
        return "StateAssignment"
    if isinstance(variable, OnCondition):
        return "OnCondition"
    if isinstance(variable, EventOut):
        return "EventOut"
    if isinstance(variable, OnEvent):
        return "OnEvent"
    if isinstance(variable, OnEntry):
        return "OnEntry"
    if isinstance(variable, Transition):
        return "Transition"

    return None


def format_math(expr):
    """Replace math symbols with HTML counterparts

    :param expr: expression to format
    :type expr: str
    :returns: replaced string

    """
    expr2 = expr.replace(".gt.", "&gt;")
    expr2 = expr2.replace(".geq.", "&gt;=")
    expr2 = expr2.replace(".lt.", "&lt;")
    expr2 = expr2.replace(".leq.", "&lt;=")
    expr2 = expr2.replace(".and.", "AND")
    expr2 = expr2.replace(".eq.", "=")
    expr2 = expr2.replace(".neq.", "!=")

    return expr2


env = Environment()
env.filters['get_lems_type'] = get_lems_type
env.filters['format_math'] = format_math

"""Template for the page header"""
page_header = env.from_string(textwrap.dedent(
    """
    (schema:{{ comp_definition|lower }}_)=
    # {{ comp_definition }}

    {% if comp_description and comp_description | length > 0 -%}
        **{{- comp_description -}}**

    ---
    {%- endif %}


    Original ComponentType definitions: [{{ comp_definition }}.xml]({{ GitHubCompSources }}/{{ comp_definition }}.xml).
    Schema against which NeuroML based on these should be valid: [NeuroML_v{{ nml_version }}.xsd](https://github.com/NeuroML/NeuroML2/tree/{{ nml_branch }}/Schemas/NeuroML2/NeuroML_v{{ nml_version }}.xsd).
    Generated on {{ nml_date }} from [this](https://github.com/NeuroML/NeuroML2/commit/{{ nml_commit }}) commit.
    Please file any issues or questions at the [issue tracker here](https://github.com/NeuroML/NeuroML2/issues).

    ---
    """))

dimension = env.from_string(textwrap.dedent(
    """
    (schema:dimensions:*)=
    ## Dimensions
    {% for dim in dimensions %}
    (schema:dimensions:{{ dim.name }})=
    ### {{ dim.name | replace("_", "\_") }}

    `````{grid}
    {% if schemas['dim.name'] %}
    :gutter: 3
    {%- else -%}
    :gutter: 2
    {% endif %}

    ````{grid-item-card} Dimensions
    :columns: 6
    {% if dim.m is not none and dim.m != 0 -%}
    M{superscript}{{ "`%s` "|format(dim.m)  }}
    {%- endif -%}
    {%- if dim.l is not none and dim.l != 0 -%}
    L{superscript}{{ "`%s` "|format(dim.l)  }}
    {%- endif -%}
    {%- if dim.t is not none and dim.t != 0 -%}
    T{superscript}{{ "`%s` "|format(dim.t)  }}
    {%- endif -%}
    {%- if dim.i is not none and dim.i != 0 -%}
    I{superscript}{{ "`%s` "|format(dim.i)  }}
    {%- endif -%}
    {%- if dim.k is not none and dim.k != 0 -%}
    K{superscript}{{ "`%s` "|format(dim.k)  }}
    {%- endif -%}
    {%- if dim.n is not none and dim.n != 0 -%}
    N{superscript}{{ "`%s` "|format(dim.n)  }}
    {%- endif %}
    ````

    ````{grid-item-card} Units
    :columns: 6
    {% for unit in units %}
    {%- if unit.dimension == dim.name %}
    - Defined unit: {ref}`schema:units:{{ unit.symbol }}`
    {% endif -%}
    {%- endfor %}
    ````

    {% if schemas["{}".format(dim.name).replace("_", "")] %}
    ````{grid-item-card} Schema
    :columns: 12
    ```{code-block} xml
    {{ schemas["{}".format(dim.name).replace("_", "")] }}
    ```
    ````
    {%- endif %}

    `````
    {% endfor %}

    """
))


unit = env.from_string(textwrap.dedent(
    """
    ## Units
    {% for unit in units %}
    (schema:units:{{ unit.symbol }})=
    ### {{ unit.symbol | replace("__", "")}}

    ````{grid}
    :gutter: 2

    ```{grid-item-card} Summary
    - Dimension: {ref}`schema:dimensions:{{ unit.dimension }}`
    - Power of 10: {{ unit.power  }}
    {% if unit.offset is not none and unit.offset != 0 -%}
    - {{ "Offset: %s"|format(unit.offset)  }}
    {% endif %}
    {% if unit.scale is not none and unit.scale != 1 %}
    - {{ "Scale: %s"|format(unit.scale)  }}
    {% endif %}
    {% if unit.factors| length > 0 %}
    ```

    ```{grid-item-card} Conversions
    {% for factor in unit.factors %}
    - 1 {{ unit.symbol | replace("__", "") }} = {{ factor[0] }} {ref}`schema:units:{{ factor[1] }}`
    {%- endfor %}
    {% endif %}
    ```
    ````
    {% endfor %}

    """
))

comp = env.from_string(textwrap.dedent(
    """
    (schema:{{ comp_type.name | lower}})=
    {% if comp_type.name.startswith("base") %}
    ## *{{ comp_type.name }}*
    {% else %}
    ## {{ comp_type.name }}
    {% endif %}

    {% if comp_type.extends is not none %}
    {% if comp_type.extends.startswith("base") %}
    extends *{ref}`schema:{{ comp_type.extends | lower}}`*
    {% else %}
    extends {ref}`schema:{{ comp_type.extends | lower}}`
    {% endif %}
    {% endif %}

    <i>{{ comp_type.description }}</i>

    {% if cno is not none %}
    [Bioportal entry for Computational Neuroscience Ontology related to {{ comp_type.name }}.](https://bioportal.bioontology.org/ontologies/CNO/?p=classes&conceptid={{ cno}})
    {% endif %}
    """
))


misc2c = env.from_string(textwrap.dedent(
    """
    ````{tab-item} {{ title }}
    ```{csv-table}
    :widths: 1, 7
    :width: 100%
    :delim: $

    {% for text in textlist -%}
    **{{ text.name }}**$ {{ text.description if text.description }}
    {% endfor %}
    ````
    """

))

misc3c = env.from_string(textwrap.dedent(
    """
    ````{tab-item} {{ title }}
    ```{csv-table}
    :widths: 1, 7, 2
    :width: 100%
    :delim: $

    {% for entry in textlist -%}
    **{{ entry.name }}**$ {{ entry.description if entry.description }} $ {ref}`schema:{{ entry.type | lower }}`
    {% endfor %}
    ```
    ````
    """

))

constants = env.from_string(textwrap.dedent(
    """
    ````{tab-item} {{ title }}
    ```{csv-table}
    :widths: 3, 5, 2
    :width: 100%
    :delim: $

    {% for entry in textlist -%}
    **{{ entry.name }}** = {{ entry.value }}$ {{ entry.description if entry.description }} $ {{ "{ref}`schema:dimensions:%s`" | format(entry.dimension) if entry.dimension != "none" else "Dimensionless" }}
    {% endfor %}
    ```
    ````
    """

))

properties = env.from_string(textwrap.dedent(
    """
    ````{tab-item} {{ title }}
    ```{csv-table}
    :widths: 3, 5, 2
    :width: 100%
    :delim: $

    {% for entry in textlist -%}
    **{{ entry.name }}** (default: {{ entry.default_value }})$ {{ entry.description if entry.description }} $ {{ "{ref}`schema:dimensions:%s`" | format(entry.dimension) if entry.dimension != "none" else "Dimensionless" }}
    {% endfor %}
    ```
    ````
    """

))


params = env.from_string(textwrap.dedent(
    """
    ````{tab-item} {{ title }}
    ```{csv-table}
    :widths: 1, 7, 2
    :width: 100 %
    :delim: $

    {% for entry in keysort -%}
    {# inherited parameters, which we print first #}
    {%- if entries[entry] != comp_type.name -%}
    **{{ entry.name }}**$ {{ entry.description if entry.description }} *(from {ref}`schema:{{ entries[entry] | lower }}`)* $
    {%-if entry.dimension -%}
    {{ "{ref}`schema:dimensions:%s`" | format(entry.dimension) if entry.dimension != "none" else "Dimensionless"}}
    {% else -%}
    Dimensionless
    {% endif -%}
    {# Not an inherited parameter #}
    {%- else -%}
    **{{ entry.name }}**$ {{ entry.description if entry.description }} $
    {%-if entry.dimension -%}
    {{ "{ref}`schema:dimensions:%s`" | format(entry.dimension) if entry.dimension != "none" else "Dimensionless" }}
    {% else -%}
    Dimensionless
    {% endif -%}
    {% endif -%}
    {%- endfor %}
    ```
    ````
    """
))

derived_params = env.from_string(textwrap.dedent(
    """
    ````{tab-item} {{ title }}
    {% for entry in keysort -%}
    ```{csv-table}
    :widths: 1, 7, 2
    :width: 100 %
    :delim: $

    {# inherited parameters, which we print first #}
    {%- if entries[entry] != comp_type.name -%}
    **{{ entry.name }}**$ {{ entry.description if entry.description }} *(from {ref}`schema:{{ entries[entry] | lower }}`)* $
    {%-if entry.dimension -%}
    {{ "{ref}`schema:dimensions:%s`" | format(entry.dimension) if entry.dimension != "none" else "Dimensionless"}}
    {% else -%}
    Dimensionless
    {% endif -%}
    {# Not an inherited parameter #}
    {%- else -%}
    **{{ entry.name }}**$ {{ entry.description if entry.description }} $
    {%-if entry.dimension -%}
    {{ "{ref}`schema:dimensions:%s`" | format(entry.dimension) if entry.dimension != "none" else "Dimensionless" }}
    {% else -%}
    Dimensionless
    {% endif -%}
    {% endif -%}
    ```
    {% if entry.value -%}
    &emsp;&emsp;&emsp;**{{ entry.name }}** = {{ entry.value }}
    {% endif -%}
    {%- endfor %}
    ````
    """
))

# Same works for exposures
exposures = params

# Same for requirements
requirements = params


eventPorts = env.from_string(textwrap.dedent(
    """
    ````{tab-item} {{ title }}
    ```{csv-table}
    :widths: 1, 7, 2
    :width: 100 %
    :delim: $

    {% for entry in keysort -%}
    {%- if entries[entry] != comp_type.name -%}
    **{{ entry.name }}**$ {{ entry.description if entry.description }} *(from {ref}`schema:{{ entries[entry] | lower }}`)*$
    {%- else -%}
    **{{ entry.name }}**$ {{ entry.description if entry.description }}$
    {%- endif -%}
    Direction: {{ entry.direction }}
    {% endfor %}
    ```
    ````
    """
))


dynamics = env.from_string(textwrap.dedent(
    """
    ````{tab-item} {{ title }}
    {% if comp_type.structure  and (comp_type.structure.widths|length +
    comp_type.structure.child_instances|length +
    comp_type.structure.multi_instantiates|length +
    comp_type.structure.event_connections|length) > 0 %}
    <i>**Structure**</i>
    {%- for w in comp_type.structure.widths %}
    : WITH **{{ w.instance }}** AS **{{ w.as_ }}**
    {%- endfor -%}
    {% for ci in comp_type.structure.child_instances %}
    : CHILD INSTANCE: **{{ ci.component}}**
    {%- endfor -%}
    {% for mi in comp_type.structure.multi_instantiates %}
    : INSTANTIATE: **{{ mi.number }}** COMPONENTS OF TYPE **{{ mi.component }}**
    {%- endfor -%}
    {% for ec in comp_type.structure.event_connections %}
    : EVENT CONNECTION from **{{ ec.from_ }}** TO  **{{ ec.to }}** {{ "RECEIVER: %s" | format(ec.receiver) if ec.receiver }} {{ "TARGET PORT: %s" | format(ec.target_port) if ec.target_port }} {{ "DELAY: %s" | format(ec.delay) if ec.delay }}
    {{ ": ASSIGN: %s = %s" | format(ec.assign.property, ec.assign.value) if ec.assign }}
    {%- endfor %}

    {% endif %}

    {% if comp_type.dynamics.state_variables|length > 0 %}
    <i>**State Variables**</i>
    {% for v in comp_type.dynamics.state_variables -%}
    : **{{ v.name }}**: {{ "{ref}`schema:dimensions:%s`" | format(v.dimension) if v.dimension != "none" else "Dimensionless" }} {{ "&emsp;(exposed as **%s**)"|format(v.exposure) if v.exposure }}
    {% endfor %}
    {% endif %}

    {% if comp_type.dynamics.event_handlers %}
    {% set ns = namespace() %}
    {% set ns.os_printed = "no" %}
    {% set ns.oc_printed = "no" %}
    {% set ns.oe_printed = "no" %}

    {% for eh in comp_type.dynamics.event_handlers -%}

    {%- if eh|get_lems_type == "OnStart" -%}
    {%- if ns.os_printed == "no" -%}
    {%- set ns.os_printed = "yes" -%}

    <i>**On Start**</i>
    {% endif -%}

    {%- for ac in eh.actions -%}
    {%- if ac|get_lems_type == "StateAssignment" -%}
    : **{{ ac.variable }}** = {{ ac.value }}
    {% endif -%}

    {%- endfor -%}
    {%- endif -%}

    {% if eh|get_lems_type == "OnCondition" %}
    {%- if ns.oc_printed == "no" -%}
    {% set ns.oc_printed = "yes" %}


    <i>**On Conditions**</i>
    {% endif %}
    : IF {{ eh.test|format_math }} THEN
    {% for ac in eh.actions %}
    {%- if ac|get_lems_type == "StateAssignment" -%}
    : &emsp;&emsp;&emsp;**{{ ac.variable }}** = {{ ac.value }}
    {% endif -%}
    {%- if ac|get_lems_type == "EventOut" -%}
    : &emsp;&emsp;&emsp;EVENT OUT on port: **{{ ac.port }}**
    {% endif -%}
    {%- endfor -%}
    {% endif -%}

    {% if eh|get_lems_type == "OnEvent" %}
    {%- if ns.oe_printed == "no" -%}
    {% set ns.oe_printed = "yes" %}

    <i>**On Events**</i>
    {% endif %}
    : EVENT IN on port: **{{ eh.port }}**
    {% for ac in eh.actions %}
    {%- if ac|get_lems_type == "StateAssignment" -%}
    : &emsp;&emsp;&emsp;**{{ ac.variable }}** = {{ ac.value }}
    {% endif -%}
    {%- if ac|get_lems_type == "EventOut" -%}
    : &emsp;&emsp;&emsp;EVENT OUT on port: **{{ ac.port }}**
    {% endif -%}
    {%- endfor -%}
    {% endif -%}

    {% endfor %}
    {% endif %}

    {% if comp_type.dynamics.derived_variables|length > 0 %}

    <i>**Derived Variables**</i>
        {% for dv in comp_type.dynamics.derived_variables -%}
    : **{{ dv.name }}** =&nbsp;
            {%- if dv.value is none -%}
    {{ dv.select|replace('/', '->') }}{{ "(reduce method: %s)"| format(dv.reduce) if dv.reduce }}
            {%- else -%}
    {{ dv.value }}
            {%- endif -%}
    {{ "&emsp;(exposed as **%s**)"|format(dv.exposure) if dv.exposure }}
        {% endfor %}
    {% endif %}

    {% if comp_type.dynamics.conditional_derived_variables|length > 0 %}
    <i>**Conditional Derived Variables**</i>
        {% for cdv in comp_type.dynamics.conditional_derived_variables -%}
            {%- for case in cdv.cases -%}
                {%- if case.condition %}
    : IF {{ case.condition|format_math }} THEN
                {%- else %}
    : OTHERWISE
                {%- endif %}
    : &emsp; **{{ cdv.name }}** = {{ case.value|replace("*", "\*") }} {{ "&emsp;(exposed as **%s**)"|format(cdv.exposure) if cdv.exposure }}
            {%- endfor %}
        {%- endfor %}
    {%- endif %}

    {% if comp_type.dynamics.time_derivatives|length > 0 %}
    <i>**Time Derivatives**</i>
        {% for td in comp_type.dynamics.time_derivatives -%}
    : d **{{ td.variable }}** /dt = {{ td.value }}
        {% endfor %}
    {% endif %}

    {%- if comp_type.dynamics.regimes|length > 0 %}
        {%- for rg in comp_type.dynamics.regimes %}

    <i>**Regime: {{ rg.name }} {%- if rg.initial is not none and rg.initial != "false" %} (initial) {%- endif -%}**</i>
        {%- set ns.oentry_printed = "no" -%}
        {%- set ns.oc_printed = "no" -%}
            {%- for eh in rg.event_handlers -%}
                {%- if eh|get_lems_type == "OnEntry" -%}
                    {%- if ns.oentry_printed == "no" -%}
                        {%- set ns.oentry_printed = "yes" %}
    : <i>**On Entry**</i>
                    {%- endif %}
                    {%- for ac in eh.actions -%}
                        {%- if ac|get_lems_type == "StateAssignment" %}
    : &emsp;&emsp; **{{ ac.variable }}** = {{ ac.value|replace("*", "\*")  }}
                        {%- endif %}
                    {%- endfor -%}
                {%- endif -%}
                {%- if eh|get_lems_type == "OnCondition" %}
                    {%- if ns.oc_printed == "no" -%}
                        {%- set ns.oc_printed = "yes" %}
    : <i>**On Conditions**</i>
                    {%- endif %}
    : &emsp;&emsp; IF {{ eh.test|format_math }} THEN
                    {%- for ac in eh.actions %}
                        {%- if ac|get_lems_type == "StateAssignment" %}
    : &emsp;&emsp;&emsp;&emsp;**{{ ac.variable }}** = {{ ac.value|replace("*", "\*")  }}
                        {%- endif %}
                        {%- if ac|get_lems_type == "EventOut" %}
    : &emsp;&emsp;&emsp;&emsp;EVENT OUT on port: **{{ ac.port }}**
                        {%- endif %}
                        {%- if ac|get_lems_type == "Transition" %}
    : &emsp;&emsp;&emsp;&emsp;TRANSITION to REGIME **{{ ac.regime }}**
                        {%- endif %}
                    {%- endfor %}
                {%- endif -%}
            {%- endfor -%}
            {%- if rg.time_derivatives|length > 0 %}
    : <i>**Time Derivatives**</i>
                {%- for td in rg.time_derivatives %}
    : &emsp;&emsp; d **{{ td.variable }}** /dt = {{ td.value }}
                {%- endfor %}
            {%- endif %}
        {%- endfor %}
    {%- endif %}
    ````
    """
))

examples = env.from_string(textwrap.dedent(
    """
    {% if pysig -%}
    ````{tab-item} {{ title }}: Python
    *<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q={{ pysig[0] }}" target="_blank">Go to the libNeuroML documentation</a>*
    ```{code-block} python
    from neuroml import {{ pysig[0] }}
    from neuroml.utils import component_factory

    variable = component_factory(
        {{ pysig[0] }},
    {%- for sig in pysig[1] %}
        {{ sig | indent(4) }},
    {%- endfor %}
    )
    ```
    ````
    {%- endif -%}
    {% if lemsexamples|length > 0 %}
    ````{tab-item} {{ title }}: XML
    {% for e in lemsexamples -%}
    ```{code-block} xml
    {{ e|trim }}
    ```
    {% endfor -%}
    ````
    {%- endif -%}
    """
))

schema_quote = env.from_string(textwrap.dedent(
    """
    ````{tab-item} Schema
    ```{code-block} xml
    {{ schemadoc }}
    ```
    ````
    """
))
