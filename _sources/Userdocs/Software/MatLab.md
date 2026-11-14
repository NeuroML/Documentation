(matlab)=
# MatLab NeuroML Toolbox

The NeuroML 2 Toolbox for MATLAB facilitates access to the Java NeuroML 2 API functionality ({ref}`jNeuroML <jNeuroML>`) directly within Matlab.

(neuromlmatlab:quickstart)=
## Quick start

Please install jNeuroML following the instructions provided {ref}`here <jneuroml:quickstart>`.
Run Matlab and run the `prefdir` command to find the location of your preferences folder.
Create a file `javaclasspath.txt` within that folder containing, on a single line, the full path to the `jNeuroML-<version>-jar-with-dependencies.jar` from jNeuroML.

Restart Matlab, and you will be able to access jNeuroML classes.
You can test your setup by validating an example file:

```{code-block}
import org.neuroml.model.util.NeuroML2Validator
file = java.io.File('/full/path/to/model.nml');
validator = NeuroML2Validator();
validator.validateWithTests(file);
disp(validator.getValidity())
```

(neuromlmatlab:docs)=
## Documentation

Please refer to the {ref}`jNeuroML documentation <jneuroml:docs>` for information on the Java NeuroML API.
Examples on using the Matlab toolbox are available [here](https://github.com/NeuroML/NeuroMLToolbox/blob/master/examples/run_examples.m).

(neuromlmatlab:gethelp)=
## Getting help

For any questions regarding the NeuroML Matlab toolbix, please open an issue on the GitHub issue tracker [here](https://github.com/NeuroML/NeuroMLToolbox/issues).
Any bugs and feature requests can also be filed there.

You can also use any of the {ref}`communication channels of the NeuroML community <contact>`.

(neuromlmatlab:development)=
## Development

The NeuroML Matlab toolbox is developed on GitHub at [https://github.com/NeuroML/NeuroMLToolbox](https://github.com/NeuroML/NeuroMLToolbox).
