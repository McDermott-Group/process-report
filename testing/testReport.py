from pyProcessReport import *
from pyLayerProcesses import *

report=ProcessReport('SFQ','T053017A')

M1 = Layer('M1', layer_comment='Bottom electrode of JJ stack and DC/SFQ shunt inductor.' )
V2 = Layer('V2', layer_comment='JJ pocket definition in dielectric.')
V2dep = PT70_PECVD('01aug2017')
V2dep.add_parameters({'Recipe Name': 'SiOxide2.ch1',
                      'Platen Temperature': '250 C',
                      'Tool': 'PT 70',
                      'Deposition Material': 'SiOx',
                      'Thickness Target': '180 nm',
                      'DC Response': '-18 V'})
V2dep.add_steps({'Deposition Time': '350 s',
                 'Pre-seed Time': '500 s',
                 'Pre-clean Time (x2)': '150 s'})
V2dep.verify_required()
M2 = Layer('M2', layer_comment='JJ oxidation and wiring layer.')

report.add_layer(M1)
report.add_layer(V2)
report.add_layer(M2)

report.build_pdf(filename='testing1', save_tex=False)
