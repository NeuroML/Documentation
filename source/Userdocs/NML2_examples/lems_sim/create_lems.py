from pyneuroml.lems import LEMSSimulation

ls = LEMSSimulation('sim1', 500, 0.05, 'net1')
ls.include_neuroml2_file('NML2_SingleCompHHCell.nml')

ls.create_display('display0', "Voltages", "-90", "50")
ls.add_line_to_display('display0', "v", "hhpop[0]/v", "1mV", "#ffffff")

ls.create_output_file('Volts_file', "v.dat")
ls.add_column_to_output_file('Volts_file', 'v', "hhpop[0]/v")

ls.save_to_file()
