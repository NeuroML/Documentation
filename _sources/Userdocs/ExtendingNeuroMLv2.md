(userdocs:extending)=
# Extending NeuroML

As a language, LEMS defines a set of built-in `types` which can be used together to build more user-defined types.
For example, Python defines `int`, `float`, `str` and so on as built-in types, and these can then be combined to define user defined types, classes.
An object of a particular class/type can be instantiated by supplying values for the members defined in the class/type.

**ComponentTypes** in LEMS are similar to classes in Python.
They define the membership structure of the type, but they do not specify values for their members.
Once a ComponentType has been defined, an instance of it can be created by setting values for its members.
This object is referred to as a **Component** in LEMS.

Having definitions in LEMS allows their re-use, and all new ComponentTypes can be submitted for inclusion to the NeuroMLv2 specification to be made accessible to other users.

- Like NeuroML, LEMS also has a [well defined schema](https://github.com/LEMS/LEMS/tree/master/Schemas/LEMS) (XSD) that is used to validate LEMS XML files.
- Also similar to NeuroML, you can use the {ref}`LEMS Python tools <pylems>` to work with LEMS and do not need to work directly with the XML files.

The NeuroML2 standard is a list of {ref}`curated LEMS ComponentTypes <userdocs:neuromlv2>`.
In cases where the set of ComponentTypes defined in the NeuroML standard is not sufficient for a particular modelling project, new ComponentTypes can be defined to extend the NeuroMLv2 standard.

(userdocs:extending:withneuroml)=
## Creating new ComponentTypes with existing NeuroML ComponentTypes

Existing ComponentTypes defined in the NeuroMLv2 standard, when sufficient, should be used to create new ComponentTypes.
These new ComponentTypes, since they consist of NeuroMLv2 ComponentTypes, *will be valid against the NeuroMLv2 schema* (must use a {code}`<neuroml ..>` root element).
For convenience, the NeuroMLv2 schema includes a subset of the {ref}`LEMS elements <userdocs:lemsschema>`.

An example of this type of extension of NeuroML can be see [here](https://github.com/OpenSourceBrain/BlueBrainProjectShowcase/blob/master/NMC/NeuroML2/Ca_LVAst.channel.nml#L42) where a new Calcium dependent ion channel Component requires a new ComponentType {code}`Ca_LVAst_m_tau_tau` that implements the time course of the gate.

However, please note that while the ComponentType will be valid NeuroML, the new Components (instances) one creates of this ComponentType (and models where Components are referenced/used) *will not*---since the NeuroML schema *does not know of the new ComponentType*.
The new Components (and the models) will be valid LEMS.
For this reason, while the ComponentType file will use a {code}`<neuroml ..>` root tag, the file containing its instantiated Components will use the {code}`<Lems ..>` root tag.

(userdocs:extending:withlems)=
## Creating new ComponentTypes with LEMS elements

When ComponentTypes from the NeuroMLv2 standard are not sufficient for the creation of new ComponentTypes, one must use LEMS elements to do so.
The definitions of the {ref}`NeuroMLv2 standard core ComponentTypes <userdocs:neuromlv2inlems>` are examples of this.

(userdocs:extending:withlems:types)=
### LEMS elements

The list of built-in types provided by LEMS can be seen {ref}`in the LEMS documentation <userdocs:lemsschema>`.
As the documentation notes, a ComponentType is the "Root element for defining component types".
It must contain a `name`, and can `extend` another ComponentType, thus inheriting its members/attributes.
Each ComponentType can contain members of other LEMS types: `Parameter`, `DerivedParameter`, `Dynamics`, `Exposure` and so on.

(userdocs:extending:withlems:examplexml)=
### Example: Lorenz model for cellular convection

To see how to create new ComponentTypes using LEMS, let us create one that is not neuroscience specific.
We will first create it using the plain XML and then see how it can be done using the Python pyLEMS API.

For this example, we will use the Lorenz model for cellular convection {cite}`Lorenz1963`.
The [Wikipedia article](https://en.wikipedia.org/wiki/Lorenz_system#Overview) provides a short summary of the model, and the equations that govern it:

\begin{align}
\frac{dx}{dt} &= \sigma (y - x) \\
\frac{dy}{dt} &= x (\rho - z) - y \\
\frac{dz}{dt} &= xy - \beta z
\end{align}

So we can see here that we have three parameters:

- $\sigma$
- $\rho$
- $\beta$

Next, `x`, `y`, and `z` are the *state variables* for this model, with initial values `x0`, `y0`, and `z0` respectively.
We also want to be able to observe the values of `x`, `y`, and `z`, so they must be *exposed* in the LEMS definition.

Let us start with the XML definition of a ComponentType that will describe this model.
Each XML file must start with a `<Lems>` "root node".
This includes information about the version of the LEMS schema that this document is valid against.
In this case, we document that this LEMS file should be valid against version 0.7.6 of the LEMS schema.

```{code-block} xml

<Lems xmlns="http://www.neuroml.org/lems/0.7.6"
      xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
      xsi:schemaLocation="http://www.neuroml.org/lems/0.7.6 https://raw.github.com/LEMS/LEMS/master/Schemas/LEMS/LEMS_v0.7.6.xsd">

      <ComponentType name="lorenz1963" description="The Lorenz system is a simplified model for atomspheric convection, derived from the Navier Stokes equations.">

        <!-- Parameters: free parameters to be used in the model -->
        <Parameter name="sigma" dimension="none" description="Prandtl Number"/>
        <Parameter name="beta" dimension="none" description="Also named b elsewhere"/>
        <Parameter name="rho" dimension="none" description="Related to the Rayleigh number, also named r elsewhere"/>

        <!-- Initial Conditions: also free parameters to be set when creating a Component from the ComponentType -->
        <Parameter name="x0" dimension="none"/>
        <Parameter name="y0" dimension="none"/>
        <Parameter name="z0" dimension="none"/>


        <!-- Exposure: what we want to be able to record from the LEMS simulation -->
        <Exposure name="x" dimension="none"/>
        <Exposure name="y" dimension="none"/>
        <Exposure name="z" dimension="none"/>
      </ComponentType>
</Lems>
```

Note that each parameter has a *dimension*, not a *unit*.
This is because LEMS allows us to use any valid units for each dimension, and takes care of the conversion factors and so on.
NeuroML also takes advantage of this LEMS feature, as noted {ref}`here <userdocs:unitsanddimensions>`.

Now, we can define the *dynamics* of the model, summarised in the equations above:

```{code-block} xml

        <Dynamics>
            <!-- State variables: linked to Exposures so that they can be accessed -->
            <StateVariable name="x" dimension="none" exposure="x"/>
            <StateVariable name="y" dimension="none" exposure="y"/>
            <StateVariable name="z" dimension="none" exposure="z"/>

            <!-- Equations defining the dynamics of each state variable -->
            <TimeDerivative variable="x" value="( sigma * (y - x) ) / sec"/>
            <TimeDerivative variable="y" value="( rho * x - y - x * z ) / sec"/>
            <TimeDerivative variable="z" value="( x * y - beta * z) / sec"/>

            <!-- Actions to take on the start of a LEMS simulation -->
            <OnStart>
                <StateAssignment variable="x" value="x0"/>
                <StateAssignment variable="y" value="y0"/>
                <StateAssignment variable="z" value="z0"/>
            </OnStart>
        </Dynamics>

```

Our LEMS file is almost complete.
However, notice that we have used `sec` in the dynamics to denote time but have not yet declared it.
We define `sec` as a *constant* whose value is defined in the ComponentType itself (and will not be set by us when instantiating a Component of this ComponentType):

```{code-block} xml
        <Constant name="sec" dimension="time" value="1s"/>
```

Also note that while we have defined this constant, we have not yet defined the `time` dimension or its units.
We can do that outside the ComponentType:

```{code-block} xml
  <Dimension name="time" t="1"/>
  <Unit name="second" symbol="s" dimension="time" power="1"/>
  <Unit name="milli second" symbol="ms" dimension="time" power="-3"/>
```

We have defined two units for the time dimension, with their conversion factors.
LEMS will use this information to correctly convert all dimensions as required.
The NeuroMLv2 standard defines various dimensions and their units {ref}`in the schema <schema:neuromlcoredimensions_>` for us to use.

The complete LEMS file will be this:

```{code-block} xml
<Lems xmlns="http://www.neuroml.org/lems/0.7.6"
      xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
      xsi:schemaLocation="http://www.neuroml.org/lems/0.7.6 https://raw.github.com/LEMS/LEMS/master/Schemas/LEMS/LEMS_v0.7.6.xsd">

  <Dimension name="time" t="1"/>
  <Unit name="second" symbol="s" dimension="time" power="1"/>
  <Unit name="milli second" symbol="ms" dimension="time" power="-3"/>

  <ComponentType name="lorenz1963" description="The Lorenz system is a simplified model for atomspheric convection, derived from the Navier Stokes equations.">

    <!-- Parameters: free parameters to be used in the model -->
    <Parameter name="sigma" dimension="none" description="Prandtl Number"/>
    <Parameter name="beta" dimension="none" description="Also named b elsewhere"/>
    <Parameter name="rho" dimension="none" description="Related to the Rayleigh number, also named r elsewhere"/>

    <!-- Initial Conditions: also free parameters to be set when creating a Component from the ComponentType -->
    <Parameter name="x0" dimension="none"/>
    <Parameter name="y0" dimension="none"/>
    <Parameter name="z0" dimension="none"/>


    <!-- Exposure: what we want to be able to record from the LEMS simulation -->
    <Exposure name="x" dimension="none"/>
    <Exposure name="y" dimension="none"/>
    <Exposure name="z" dimension="none"/>
    <Constant name="sec" dimension="time" value="1s"/>

    <Dynamics>
        <!-- State variables: linked to Exposures so that they can be accessed -->
        <StateVariable name="x" dimension="none" exposure="x"/>
        <StateVariable name="y" dimension="none" exposure="y"/>
        <StateVariable name="z" dimension="none" exposure="z"/>

        <!-- Equations defining the dynamics of each state variable -->
        <TimeDerivative variable="x" value="( sigma * (y - x) ) / sec"/>
        <TimeDerivative variable="y" value="( rho * x - y - x * z ) / sec"/>
        <TimeDerivative variable="z" value="( x * y - beta * z) / sec"/>

        <!-- Actions to take on the start of a LEMS simulation -->
        <OnStart>
            <StateAssignment variable="x" value="x0"/>
            <StateAssignment variable="y" value="y0"/>
            <StateAssignment variable="z" value="z0"/>
        </OnStart>
    </Dynamics>
  </ComponentType>
</Lems>
```

We now have a complete LEMS model declaration.
To use this model, we need to create an instance of the ComponentType, a Component.
This requires us to set the values of various parameters of the defined model:

```{code-block} xml
<lorenz1963 id="lorenzCell" sigma="10" beta="2.67" rho="28"
    x0="1.0" y0="1.0" z0="1.0"/>
```

Here, we've set parameters that result in the chaotic attractor regime.
We could also use different values for the parameters---like a class can have many many objects with different parameters, a ComponentType can have also have different Components.

Note that one can also define a Component using the standard constructor form:
```{code-block} xml
  <Component id="lorenzCell" type="lorenz1963" sigma="10" beta="2.67" rho="28" x0="1.0" y0="1.0" z0="1.0"/>
```
The two forms are equivalent.
As with other conventions, either form can be used as long as it is used consistently.

The `Include` element type allows us to modularise our models.
In NeuroML based models, we use it to break our model down into small independent reusable files.

(userdocs:extending:lorenz:python)=
### Writing the model in Python using PyLEMS

While the underlying format for NeuroML and LEMS is XML, Python is the suggested programming language for end users.
In this section we will see how the Lorenz model can be written using the {ref}`PyLEMS <pylems>` Python LEMS API.
The complete script is below:

```{literalinclude} ./NML2_examples/LorenzLems.py
----
language: python
----
```

As you will see, the PyLEMS API exactly follows the XML constructs that we used before.
Running this script, let's call it `LorenzLems.py` gives us:

```{code-block} console
$ python LorenzLems.py
Validating LEMS_lorenz.xml against https://raw.githubusercontent.com/LEMS/LEMS/development/Schemas/LEMS/LEMS_v0.7.6.xsd
It's valid!
```

The generated XML file is below.
As you can see, it is identical to the XML file that we wrote by hand in the previous section.
You will also see that the Python API also provides convenience functions, such as the `export_to_file` and `validate_lems` functions to quickly save your model to an XML file, and validate it.

```{literalinclude} ./NML2_examples/LEMS_lorenz.xml
----
language: xml
----
```

We strongly suggest that users use the Python tools when working with both NeuroML and LEMS.
Not only is Python easier to read and write than XML, it also provides powerful programming constructs and has a rich ecosystem of scientific software.

(userdocs:extending:examples)=
## Examples

Here are some examples of Components written using LEMS to extend NeuroML that can be used as references.

- [The Lorenz example XML source code](https://github.com/NeuroML/NeuroMLlite/blob/master/examples/test_files/Lorenz1963.xml)
- [An example script for building a LEMS model using Python](https://github.com/LEMS/pylems/blob/master/examples/apitest2.py)
- [Defining a new synapse in LEMS](https://github.com/OpenSourceBrain/BonoClopath2017/blob/master/NeuroML2/AMPA_NMDA.synapse.nml)
- [Defining an ion channel in LEMS](https://github.com/OpenSourceBrain/SmithEtAl2013-L23DendriticSpikes/blob/master/NeuroML2/na.channel.nml)
- [Defining a new Calcium pool in LEMS](https://github.com/OpenSourceBrain/PospischilEtAl2008/blob/master/NeuroML2/channels/Ca/Ca.nml)
