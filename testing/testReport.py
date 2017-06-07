from pyProcessReport import *
from pyLayerProcess import *

# A project name as well as wafer name are required to build a report
report=ProcessReport('SFQ','T053017A')

# Building the appropriate layers to which processes will be later added
M1 = Layer('M1', layer_comment='Bottom electrode of JJ stack and DC/SFQ shunt inductor.' )
V2 = Layer('V2', layer_comment='JJ pocket definition in dielectric.')
M2 = Layer('M2', layer_comment='JJ oxidation and wiring layer.')

# Build processes which will be added to layers
V2dep = PT70PECVD('01aug2017', process_comment='Ezpz')

V2dep.add_parameter('Recipe Name (ch1)', 'SiOxide2')
V2dep.add_parameters({'Platen Temperature (C)':     '250',
                      'Deposition Material':        'SiOx',
                      'Thickness Target (nm)':      '180',
                      'DC Response (V)':            '-18'})

V2dep.add_step({'step number': 1, 'step': 'Pre-clean Time (x2, s)', 'value': '150'})

V2dep.add_steps([{'step number': 2, 'step': 'Pre-seed Time (s)',    'value': '500'},
                 {'step number': 3, 'step': 'Deposition Time (s)',  'value': '350'}])


V2etch = Unaxis790RIE('01aug2017', process_comment='Etch the Ezpz')

V2etch.add_parameter('Recipe Name', '50CHF3')
V2etch.add_parameters({'Platen':            'Carbon',
                      'Etched Material':    'PECVD SiOx',
                      'DC Response (V)':    '272'
                       })

V2etch.add_step({'step number': 1, 'step': 'Pre-clean Time (s)', 'value': '300'})

V2etch.add_steps([{'step number': 2, 'step': 'Pre-seed Time (s)', 'value': '0'},
                  {'step number': 3, 'step': 'Etch Time (s)', 'value': '480'}])

# Add processes to the appropriate layers
V2.add_process(V2dep)
V2.add_process(V2etch)
V2.add_image('kitten.jpg', 'This is a kitten. It does not care about you.')

V2.add_image('cat.jpg', 'This is a cat. It still does not care about you.')

# Add layers to the report
report.add_layer(M1)
report.add_layer(V2)
report.add_layer(M2)

# Build the report once all pieces are added to it
report.build_pdf(filename='testing1', save_tex=True)

