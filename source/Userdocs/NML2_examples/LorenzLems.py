#!/usr/bin/env python3

import lems.api as lems
from lems.base.util import validate_lems

model = lems.Model()

model.add(lems.Dimension(name="time", t=1))
model.add(lems.Unit(name="second", symbol="s", dimension="time", power=1))
model.add(lems.Unit(name="milli second", symbol="ms", dimension="time", power=-3))

lorenz = lems.ComponentType(name="lorenz1963", description="The Lorenz system is a simplified model for atomspheric convection, derived from the Navier Stokes equations")
model.add(lorenz)

lorenz.add(lems.Parameter(name="sigma", dimension="none", description="Prandtl Number"))
lorenz.add(lems.Parameter(name="beta", dimension="none", description="Also named b elsewhere"))
lorenz.add(lems.Parameter(name="rho", dimension="none", description="Related to the Rayleigh number, also named r elsewhere"))


lorenz.add(lems.Parameter(name="x0", dimension="none"))
lorenz.add(lems.Parameter(name="y0", dimension="none"))
lorenz.add(lems.Parameter(name="z0", dimension="none"))

lorenz.add(lems.Exposure(name="x", dimension="none"))
lorenz.add(lems.Exposure(name="y", dimension="none"))
lorenz.add(lems.Exposure(name="z", dimension="none"))

lorenz.add(lems.Constant(name="sec", value="1s", dimension="time"))

lorenz.dynamics.add(lems.StateVariable(name="x", dimension="none", exposure="x"))
lorenz.dynamics.add(lems.StateVariable(name="y", dimension="none", exposure="y"))
lorenz.dynamics.add(lems.StateVariable(name="z", dimension="none", exposure="z"))

lorenz.dynamics.add(lems.TimeDerivative(variable="x", value="( sigma * (y - x)) / sec"))
lorenz.dynamics.add(lems.TimeDerivative(variable="y", value="( rho * x - y - x * z ) / sec"))
lorenz.dynamics.add(lems.TimeDerivative(variable="z", value="( x * y - beta * z) / sec"))

onstart = lems.OnStart()
onstart.add(lems.StateAssignment(variable="x", value="x0"))
onstart.add(lems.StateAssignment(variable="y", value="y0"))
onstart.add(lems.StateAssignment(variable="z", value="z0"))
lorenz.dynamics.add(onstart)


model.add(lems.Component(id_="lorenzCell", type_=lorenz.name, sigma="10",
                         beta="2.67", rho="28", x0="1.0", y0="1.0", z0="1.0"))

file_name = "LEMS_lorenz.xml"
model.export_to_file(file_name)


validate_lems(file_name)
