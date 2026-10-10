(userdocs:lemsexample8)=
# Example 8: Regimes in Dynamics definitions

This example introduces the Regime, Transition and OnEntry elements within a Dynamics block.
Rather than having a single state instance, the entity can be on one of the defined regimes at any given time.
The Transition element occurring inside a condition block serves to move it from one regime to another.
The OnEntry block inside a regime can contain initialization directives that apply each time the entity enters that regime.

```{code-block} xml
<ComponentType name="refractiaf">
   <Parameter name="threshold" dimension="voltage" />
   <Parameter name="refractoryPeriod" dimension="time" />
   <Parameter name="capacitance" dimension="capacitance" />
   <Parameter name="vleak" dimension="voltage" />
   <Parameter name="gleak" dimension="conductance" />
   <Parameter name="current" dimension="current" />
   <Parameter name="vreset" dimension="voltage" />
   <Parameter name="deltaV" dimension="voltage" />
   <Parameter name="v0" dimension="voltage" />
   <EventPort name="out" direction="out" />
   <EventPort name="in" direction="in" />
   <Dynamics>
      <StateVariable name="v" dimension="voltage" />
      <OnStart>
         <StateAssignment variable="v" value="v0" />
      </OnStart>
      <Regime name="refr">
         <StateVariable name="tin" dimension="time" />
         <OnEntry>
            <StateAssignment variable="tin" value="t" />
            <StateAssignment variable="v" value="vreset" />
         </OnEntry>
         <OnCondition test="t .gt. tin + refractoryPeriod">
            <Transition regime="int" />
         </OnCondition>
      </Regime>
      <Regime name="int" initial="true">
         <TimeDerivative variable="v" value="(current + gleak * (vleak - v)) / capacitance" />
         <OnCondition test="v .gt. threshold">
            <EventOut port="out" />
            <Transition regime="refr" />
         </OnCondition>
         <OnEvent port="in">
            <StateAssignment variable="v" value="v + deltaV" />
         </OnEvent>
      </Regime>
   </Dynamics>
</ComponentType>
```

Full listing:
```{literalinclude} ./LEMS_examples/example8.xml
----
language: xml
----
```
