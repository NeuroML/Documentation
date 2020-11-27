# NeuroML under the hood: LEMS

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
