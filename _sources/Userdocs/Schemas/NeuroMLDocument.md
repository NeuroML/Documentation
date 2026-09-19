(schema:neuroml_main_)=
# NeuroMLDocument

**The main NeuroML container class, and other associated types that do not fit into the other categories**

---


Schema against which NeuroML based on these should be valid: [NeuroML_v2.3.xsd](https://github.com/NeuroML/NeuroML2/tree/master/Schemas/NeuroML2/NeuroML_v2.3.xsd).
Please file any issues or questions at the [issue tracker here](https://github.com/NeuroML/NeuroML2/issues).

---

(schema:neuromldocument)=
## NeuroMLDocument

`````{tab-set}
````{tab-item} Schema
```{code-block} xml
  <xs:element name="neuroml" type="NeuroMLDocument">
    <xs:annotation>
      <xs:documentation>The root NeuroML element.</xs:documentation>
    </xs:annotation>
  </xs:element>

  <xs:complexType name="NeuroMLDocument">
    <xs:complexContent>
      <xs:extension base="Standalone">
        <xs:sequence>
          <xs:element name="include" type="IncludeType" minOccurs="0" maxOccurs="unbounded"/>
          <xs:element name="extracellularProperties" type="ExtracellularProperties" minOccurs="0" maxOccurs="unbounded"/>
          <xs:element name="intracellularProperties" type="IntracellularProperties" minOccurs="0" maxOccurs="unbounded"/>
          <xs:element name="morphology" type="Morphology" minOccurs="0" maxOccurs="unbounded"/>
          <xs:element name="ionChannel" type="IonChannel" minOccurs="0" maxOccurs="unbounded"/>
          <xs:element name="ionChannelHH" type="IonChannelHH" minOccurs="0" maxOccurs="unbounded"/>
          <xs:element name="ionChannelVShift" type="IonChannelVShift" minOccurs="0" maxOccurs="unbounded"/>
          <xs:element name="ionChannelKS" type="IonChannelKS" minOccurs="0" maxOccurs="unbounded"/>
          <xs:group ref="ConcentrationModelTypes"/>
          <xs:group ref="SynapseTypes"/>
          <xs:element name="biophysicalProperties" type="BiophysicalProperties" minOccurs="0" maxOccurs="unbounded"/>
          <xs:group ref="CellTypes"/>
          <xs:group ref="InputTypes"/>
          <xs:group ref="PyNNCellTypes"/>
          <xs:group ref="PyNNSynapseTypes"/>
          <xs:group ref="PyNNInputTypes"/>
          <xs:element name="network" type="Network" minOccurs="0" maxOccurs="unbounded"/>
          <xs:element name="ComponentType" type="ComponentType" minOccurs="0" maxOccurs="unbounded"/>
        </xs:sequence>
      </xs:extension>
    </xs:complexContent>
  </xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=NeuroMLDocument" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import NeuroMLDocument
from neuroml.utils import component_factory

variable = component_factory(
    NeuroMLDocument,
    id: 'a NmlId (required)' = None
    metaid: 'a MetaId (optional)' = None
    notes: 'a string (optional)' = None
    properties: 'list of Property(s) (optional)' = None
    annotation: 'a Annotation (optional)' = None
    includes: 'list of IncludeType(s) (optional)' = None
    extracellular_properties: 'list of ExtracellularProperties(s) (optional)' = None
    intracellular_properties: 'list of IntracellularProperties(s) (optional)' = None
    morphology: 'list of Morphology(s) (optional)' = None
    ion_channel: 'list of IonChannel(s) (optional)' = None
    ion_channel_hhs: 'list of IonChannelHH(s) (optional)' = None
    ion_channel_v_shifts: 'list of IonChannelVShift(s) (optional)' = None
    ion_channel_kses: 'list of IonChannelKS(s) (optional)' = None
    decaying_pool_concentration_models: 'list of DecayingPoolConcentrationModel(s) (optional)' = None
    fixed_factor_concentration_models: 'list of FixedFactorConcentrationModel(s) (optional)' = None
    alpha_current_synapses: 'list of AlphaCurrentSynapse(s) (optional)' = None
    alpha_synapses: 'list of AlphaSynapse(s) (optional)' = None
    exp_one_synapses: 'list of ExpOneSynapse(s) (optional)' = None
    exp_two_synapses: 'list of ExpTwoSynapse(s) (optional)' = None
    exp_three_synapses: 'list of ExpThreeSynapse(s) (optional)' = None
    blocking_plastic_synapses: 'list of BlockingPlasticSynapse(s) (optional)' = None
    double_synapses: 'list of DoubleSynapse(s) (optional)' = None
    gap_junctions: 'list of GapJunction(s) (optional)' = None
    silent_synapses: 'list of SilentSynapse(s) (optional)' = None
    linear_graded_synapses: 'list of LinearGradedSynapse(s) (optional)' = None
    graded_synapses: 'list of GradedSynapse(s) (optional)' = None
    biophysical_properties: 'list of BiophysicalProperties(s) (optional)' = None
    cells: 'list of Cell(s) (optional)' = None
    cell2_ca_poolses: 'list of Cell2CaPools(s) (optional)' = None
    base_cells: 'list of BaseCell(s) (optional)' = None
    iaf_tau_cells: 'list of IafTauCell(s) (optional)' = None
    iaf_tau_ref_cells: 'list of IafTauRefCell(s) (optional)' = None
    iaf_cells: 'list of IafCell(s) (optional)' = None
    iaf_ref_cells: 'list of IafRefCell(s) (optional)' = None
    izhikevich_cells: 'list of IzhikevichCell(s) (optional)' = None
    izhikevich2007_cells: 'list of Izhikevich2007Cell(s) (optional)' = None
    ad_ex_ia_f_cells: 'list of AdExIaFCell(s) (optional)' = None
    fitz_hugh_nagumo_cells: 'list of FitzHughNagumoCell(s) (optional)' = None
    fitz_hugh_nagumo1969_cells: 'list of FitzHughNagumo1969Cell(s) (optional)' = None
    pinsky_rinzel_ca3_cells: 'list of PinskyRinzelCA3Cell(s) (optional)' = None
    hindmarshRose1984Cell: 'list of HindmarshRose1984Cell(s) (optional)' = None
    pulse_generators: 'list of PulseGenerator(s) (optional)' = None
    pulse_generator_dls: 'list of PulseGeneratorDL(s) (optional)' = None
    sine_generators: 'list of SineGenerator(s) (optional)' = None
    sine_generator_dls: 'list of SineGeneratorDL(s) (optional)' = None
    ramp_generators: 'list of RampGenerator(s) (optional)' = None
    ramp_generator_dls: 'list of RampGeneratorDL(s) (optional)' = None
    compound_inputs: 'list of CompoundInput(s) (optional)' = None
    compound_input_dls: 'list of CompoundInputDL(s) (optional)' = None
    voltage_clamps: 'list of VoltageClamp(s) (optional)' = None
    voltage_clamp_triples: 'list of VoltageClampTriple(s) (optional)' = None
    spike_arrays: 'list of SpikeArray(s) (optional)' = None
    timed_synaptic_inputs: 'list of TimedSynapticInput(s) (optional)' = None
    spike_generators: 'list of SpikeGenerator(s) (optional)' = None
    spike_generator_randoms: 'list of SpikeGeneratorRandom(s) (optional)' = None
    spike_generator_poissons: 'list of SpikeGeneratorPoisson(s) (optional)' = None
    spike_generator_ref_poissons: 'list of SpikeGeneratorRefPoisson(s) (optional)' = None
    poisson_firing_synapses: 'list of PoissonFiringSynapse(s) (optional)' = None
    transient_poisson_firing_synapses: 'list of TransientPoissonFiringSynapse(s) (optional)' = None
    IF_curr_alpha: 'list of IF_curr_alpha(s) (optional)' = None
    IF_curr_exp: 'list of IF_curr_exp(s) (optional)' = None
    IF_cond_alpha: 'list of IF_cond_alpha(s) (optional)' = None
    IF_cond_exp: 'list of IF_cond_exp(s) (optional)' = None
    EIF_cond_exp_isfa_ista: 'list of EIF_cond_exp_isfa_ista(s) (optional)' = None
    EIF_cond_alpha_isfa_ista: 'list of EIF_cond_alpha_isfa_ista(s) (optional)' = None
    HH_cond_exp: 'list of HH_cond_exp(s) (optional)' = None
    exp_cond_synapses: 'list of ExpCondSynapse(s) (optional)' = None
    alpha_cond_synapses: 'list of AlphaCondSynapse(s) (optional)' = None
    exp_curr_synapses: 'list of ExpCurrSynapse(s) (optional)' = None
    alpha_curr_synapses: 'list of AlphaCurrSynapse(s) (optional)' = None
    SpikeSourcePoisson: 'list of SpikeSourcePoisson(s) (optional)' = None
    networks: 'list of Network(s) (optional)' = None
    ComponentType: 'list of ComponentType(s) (optional)' = None
```
````

````{tab-item} Usage: XML
```{code-block} xml
<neuroml xmlns="http://www.neuroml.org/schema/neuroml2"  xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.neuroml.org/schema/neuroml2 https://raw.github.com/NeuroML/NeuroML2/development/Schemas/NeuroML2/NeuroML_v2.3.xsd" id="HL23PYR">
    <include href="HL23PYR.cell.nml"/>
    <pulseGenerator id="pg_HL23PYR" delay="50ms" duration="200ms" amplitude="0.2nA">
        <notes>Simple pulse generator</notes>
    </pulseGenerator>
    <network id="HL23PYRNet" type="networkWithTemperature" temperature="34 degC">
        <population id="HL23PYR_pop" component="HL23PYR" type="populationList">
            <property tag="color" value="0.3220229197377431 0.19279726280626452 0.37635392246534727"/>
            <property tag="region" value="L23"/>
            <instance id="0">
                <location x="0.0" y="0.0" z="0.0"/>
            </instance>
        </population>
        <inputList id="stim_iclamp_HL23PYR" population="HL23PYR_pop" component="pg_HL23PYR">
            <input id="0" target="../HL23PYR_pop/0" destination="synapses"/>
        </inputList>
    </network>
</neuroml>
```
````
`````

(schema:includetype)=
## IncludeType


<i>Used to include other documents into each other.</i>

`````{tab-set}
````{tab-item} Schema
```{code-block} xml
  <xs:complexType name="IncludeType">
    <xs:attribute name="href" use="required" type="xs:anyURI"/>
  </xs:complexType>
```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=IncludeType" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import IncludeType
from neuroml.utils import component_factory

variable = component_factory(
    IncludeType,
    href: 'a anyURI (required)' = None)
```
````

````{tab-item} Usage: XML
```{code-block} xml
<neuroml xmlns="http://www.neuroml.org/schema/neuroml2"  xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.neuroml.org/schema/neuroml2 https://raw.github.com/NeuroML/NeuroML2/development/Schemas/NeuroML2/NeuroML_v2.3.xsd" id="HL23PYR">
    <include href="A.cell.nml"/>
    ..
</neuroml>
```
````
`````
