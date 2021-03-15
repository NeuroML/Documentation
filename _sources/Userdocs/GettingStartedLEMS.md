(userdocs:getting_started_lems)=
# NeuroML under the hood: LEMS

In LEMS, **ComponentType** elements which specify **Parameter**s, **StateVariable**s and their **Dynamics** and **Structure** can be defined as templates for model elements.
For example, the definition of the Izhikevich cell component type that we have been using in NeuroML, in LEMS is below:
```{code-block} xml
<Lems xmlns="http://www.neuroml.org/lems/0.7.4"
      xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
      xsi:schemaLocation="http://www.neuroml.org/lems/0.7.4 ../../LEMS/Schemas/LEMS/LEMS_v0.7.4.xsd"
      description="Defines both abstract cell models (e.g. _izhikevichCell_, adaptive exponential integrate and fire cell, _adExIaFCell_), point conductance based cell models (_pointCellCondBased_, _pointCellCondBasedCa_) and cells models (_cell_) which specify the _morphology_ (containing _segment_s) and _biophysicalProperties_ separately.">

    <!-- other components -->

    <ComponentType name="izhikevich2007Cell"
        extends="baseCellMembPotCap"
        description="Cell based on the modified Izhikevich model in Izhikevich 2007, Dynamical systems in neuroscience, MIT Press">

        <Parameter name="v0" dimension="voltage"/>
        <!--
        Defined in baseCellMembPotCap:
        <Parameter name="C" dimension="capacitance"/>
        -->
        <Parameter name="k" dimension="conductance_per_voltage"/>

        <Parameter name="vr" dimension="voltage"/>
        <Parameter name="vt" dimension="voltage"/>
        <Parameter name="vpeak" dimension="voltage"/>

        <Parameter name="a" dimension="per_time"/>
        <Parameter name="b" dimension="conductance"/>
        <Parameter name="c" dimension="voltage"/>
        <Parameter name="d" dimension="current"/>

        <Attachments name="synapses" type="basePointCurrent"/>

        <Exposure name="u" dimension="current"/>

        <Dynamics>
            <StateVariable name="v" dimension="voltage" exposure="v"/>
            <StateVariable name="u" dimension="current" exposure="u"/>
            <DerivedVariable name="iSyn"  dimension="current" exposure="iSyn" select="synapses[*]/i" reduce="add" />
            <DerivedVariable name="iMemb" dimension="current" exposure="iMemb" value="k * (v-vr) * (v-vt) + iSyn - u"/>
            <TimeDerivative variable="v" value="iMemb / C"/>
            <TimeDerivative variable="u" value="a * (b * (v-vr) - u)"/>

            <OnStart>
                <StateAssignment variable="v" value="v0"/>
                <StateAssignment variable="u" value="0"/>
            </OnStart>

            <OnCondition test="v .gt. vpeak">
                <StateAssignment variable="v" value="c"/>
                <StateAssignment variable="u" value="u + d"/>
                <EventOut port="spike"/>
            </OnCondition>
        </Dynamics>
    </ComponentType>

```
The `<izhikevich2007 ..>`  *Component* in our NeuroML files is an *instance* of this defined *ComponentType* with specific values of Parameters.
If you are familiar with object oriented programming, you can think of the definition of the component type in LEMS as the definition of a class.
The component then becomes an instance of this class, with whatever parameter values we need to use.
So, for the Izhikevich cell where we have been using parameters that model a regular spiking neuron, we can have another instance with different parameters that models an adaptive spiking neuron.
They will both use the same ComponentType, but will be two different Components, with different parameter values.


## More extra text
Different aspects of computational models---cells, synapses, ion channels, and so on---have some *dynamics* associated with them.
The dynamics of the Izhikevich cell model, for example, are defined by a set of equations:

\begin{align}
iMemb &= k * (v- vr) * (v - vt) * iSyn -u \\
\frac{du}{dt} &= a (bv -u) \\
\frac{dv}{dt} &= iMemb/C
\end{align}

Here, `iSyn` and `iMemb` are two *derived variables*: the synaptic input current, and the membrane current respectively.
Additionally, a spike is detected when the membrane potential `v` is greater than the threshold `thresh`.
When this occurs, some variables are updated:

- `v` is set to `c`,
- `u` is incremented: `u = u+d`.

How are these dynamics represented in NeuroML?
The answer is: "with [LEMS](http://lems.github.io/LEMS)".
Let us take a short segue to understand how NeuroML constructs are defined LEMS, and we will return to the Izhikevich model after.

[LEMS](http://lems.github.io/LEMS) (Low Entropy Model Specification) is an XML based language with interpreter originally developed by Robert Cannon for specifying generic models of hybrid dynamical systems.

In other words, similar to NeuroML, LEMS defines a Schema but one that allows us to describe dynamical systems.

For example, a class can be defined as follows:
```{code-block} cpp
class rectangle {
  int length;
  int breadth;
}
```

There can be many rectangles of different dimensions, so we can *instantiate* different objects of this class:
```{code-block} cpp
/* A rectangle */
rectangle r1 = rectangle();
r1.length = 5;
r1.breadth = 6;

/* A different rectangle */
rectangle r1 = rectangle();
r1.length = 10;
r1.breadth = 50;
```
In the same way, once the `izhikevichCell` ComponentType has been defined in the NeuroML standard with its parameters and dynamics, any number of cells of this type can be instantiated.
