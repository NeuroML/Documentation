(userdocs:lemsexample2)=
# Example 2: tidying up example 1

This models is the same as in example 1, except that the definitions have been split out into several self-contained files.

The main file, included below, uses the Include element to include definitions from other files.
Each file is only read once, even if several files include it.
Because some of these files, such as the HH channel definitions, are intended to be used on their own, they include all the dimension definitions they need.
These may also occur in other files with the same dimension names.
This is fine as long as the dimensions being declared are the same.
An error will be reported if a new definition is supplied that changes any of the values.
The same applies for Unit definitions.
For other element types names and ids must be unique.
An id or name can't appear twice, even if the content of the elements is the same.

# Main model
This defines a few components, then a network that uses them and a simulation to run it all. The HHCell component refers to channel types coming from the included hhmodels.xml file which in turn depends on hhcell.xml and hhchannel.xml.
```{literalinclude} ./LEMS_examples/example2.xml
----
language: xml
----
```

# Included files

```{literalinclude} ./LEMS_examples/ex2dims.xml
----
language: xml
----
```

The file hhchannel.xml contains complete definitions of a fairly general HH-style channel model with any number of gates based on the three standard types used in the original HH work.


```{literalinclude} ./LEMS_examples/hhchannel.xml
----
language: xml
----
```
As mentioned in example1, the numerics are too feeble to cope with this gate definition though, so a change of variables is employed instead:

```{literalinclude} ./LEMS_examples/hhaltgate.xml
----
language: xml
----
```

The file hhcell.xml defines a simple cell model with some populations of HH channels.


```{literalinclude} ./LEMS_examples/hhcell.xml
----
language: xml
----
```

A couple of spike generators.

```{literalinclude} ./LEMS_examples/spikegenerators.xml
----
language: xml
----
```

And now the components themselves.
These are the standard HH sodium and potassium channels (as used in Rallpack3).


```{literalinclude} ./LEMS_examples/hhmodels.xml
----
language: xml
----
```

Some miscellaneous iaf models.

```{literalinclude} ./LEMS_examples/misciaf.xml
----
language: xml
----
```

Finally, a small collection of dimension definitions useful for things like the miscellaneous iaf cell definitions.


```{literalinclude} ./LEMS_examples/elecdims.xml
----
language: xml
----
```
