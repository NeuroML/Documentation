(userdocs:lemsschema)=
# LEMS

The current version of the LEMS specification is 0.7.6 and the schema for this can be seen [here](https://github.com/LEMS/LEMS/blob/master/Schemas/LEMS/LEMS_v0.7.6.xsd).
The following figure, taken from Cannon et al. 2014 ({cite}`Cannon2014`) shows the structure of LEMS models.
The following pages give details of all the elements that are included in LEMS.
For examples on LEMS, and using LEMS to extend NeuroML, please see the relevant sections in the documentation.

```{figure} ../images/lems-figure2.png
:alt: Structure of LEMS models
:align: center
:width: 80%

*(A)* Models in LEMS are specified using ComponentType definitions with nested
Dynamics elements. Any Parameter or StateVariable declaration must refer to a
Dimension element defined at the top level. A Component element sets parameter
values for a particular instance of a ComponentType. Each Parameter value must
refer to one of the Unit elements defined at the top level. The Dynamics
element supports continuous time systems defined in terms of first order
differential equations, and event driven processing as specified by the various
"On. . ." elements. Multiple Regimes, each with independent TimeDerivative
expressions can be defined, along with the rules to transition between them.
*(B)* Example of a ComponentType, the passive channel model from Figure 1.
*(C)* The XML equivalent of the ComponentType (top) and Component (bottom) for this
model. *(D)* Defining containment in LEMS, using Child (exactly one sub element
of the given type) or Children (zero or multiple copies). **(E)** Extension in
LEMS. Extending ComponentTypes inherit the structure of the base type.  Example
Components in XML are shown in *(D,E)*.

```

