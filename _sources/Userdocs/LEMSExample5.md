(userdocs:lemsexample5)=
# Example 5: References and paths

The ChannelPopulation type used earlier repeats a common model specification error in that it makes the reversal potential of a population of channels a parameter of the population (often it is made a parameter of the channel specification, which is equally bad):

```{code-block} xml
<ComponentType name="ChannelPopulation">
   <ComponentRef name="channel" type="KSChannel" />
   <Parameter name="number" dimension="none" />
   <Parameter name="erev" dimension="voltage" />
</ComponentType>
```
In fact, of course, the reversal potential is not a property of a channel population, or of a channel.
It depends on the environment the channel is put in and the ions it is permeable to.
But, it is needed in the Dynamics specification for the population so just putting it in as a parameter solves the immediate problem.
In the process, however, it introduces the potential for easily creating contradictory models, by, for example setting different reversals for populations of the same type of channel.

A much better approach is to let the channel just say what it is permeable to.
Some other element in the model can define the membrane reversal potentials for different channels, and the channel population object should then look up the relevant value for the permeant ion of its channel.
This provides a cleaner expression of what is there, removes redundancy and lowers the entropy of the model specification.

The following three types are sufficient to provide a simple framework to centralize the definitions of species and reversal potentials on one place:

```{code-block} xml
<ComponentType name="Species">
   <Text name="name" />
   <Parameter name="charge" dimension="none" />
</ComponentType>
<ComponentType name="Environment">
   <Children name="membranePotentials" type="MembranePotential" />
</ComponentType>
<ComponentType name="MembranePotential">
   <ComponentRef name="species" type="Species" />
   <Parameter name="reversal" dimension="voltage" />
</ComponentType>
```
Once these are available, they can be used to define some species, and to create an environment component that sets their reversal potentials:

```{code-block} xml
<Species id="Na" name="Sodium" charge="1" />
<Species id="K" name="Potassium" charge="1" />
<Species id="Ca" name="Calcium" charge="1" />
<Environment id="env1">
   <MembranePotential species="Na" reversal="50mV" />
   <MembranePotential species="K" reversal="-80mV" />
</Environment>
```
The next step is to add a species reference to the channel type, so that channel definitions can say what species they are permeant to.

```{code-block} xml
<ComponentType name="KSChannel">
   <Parameter name="conductance" dimension="conductance" />
   <ComponentRef name="species" type="Species" />
   <Children name="gates" type="KSGate" />
   <Dynamics>
      <DerivedVariable name="fopen" dimension="none" select="gates[*]/fopen" reduce="multiply" />
      <DerivedVariable name="g" dimension="conductance" value="fopen * conductance" />
   </Dynamics>
</ComponentType>
```
Finally the channel population type needs modifying to add a derived parameter that addresses the reversal potential from the membrane properties:

```{code-block} xml
<ComponentType name="ChannelPopulation">
   <ComponentRef name="channel" type="KSChannel" />
   <Parameter name="number" dimension="none" />
   <Requirement name="v" dimension="voltage" />
   <DerivedParameter name="erev" dimension="voltage" select="//MenbranePotential[species = channel/species]/reversal" />
   <Dynamics>
      <DerivedVariable name="channelg" dimension="conductance" select="channel/g" />
      <DerivedVariable name="geff" value="channelg * number" />
      <DerivedVariable name="current" value="geff * (erev - v)" />
   </Dynamics>
</ComponentType>
```
This introduces a new construct, the DerivedParameter specification that defines a local parameter "erev" to hold the quantity from the specified path:

```{code-block} xml
<DerivedParameter name="erev" dimension="voltage" select="//MenbranePotential[species = channel/species]/reversal" />
```

The path here uses XPath like syntax operating on the component tree in the model.
In this case, it finds all the elements of thpe MembranePotential in the model.
The predicate selects the one for which the species is the same as the species referred to from the channel used for this population.
Finally, it takes the "reversal" parameter from the membrane potential component.
This is made locally available as the parameter "erev".

The Dynamics of this model is exactly the same as example 4.
The full model including both the type definitions and the components is included below.


```{literalinclude} ./LEMS_examples/example5.xml
----
language: xml
----
```
