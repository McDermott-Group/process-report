from pyProcessReport.layerProcess import LayerProcess


class Unaxis790RIE(LayerProcess):
    def __init__(self, process_date, process_comment=None):

        self.process_name = 'Etching'

        LayerProcess.__init__(self, process_name = self.process_name,
                              process_date = process_date,
                              process_comment = process_comment)

        self.required_params = ['Recipe Name',
                                'Platen',
                                'Tool',
                                'Etched Material',
                                'DC Response (V)']

        self.required_steps  = ['Etch Time (s)',
                                'Pre-seed Time (s)',
                                'Pre-clean Time (s)']

        self.add_parameter('Tool', 'Unaxis 790 RIE')


class PT770Etch(LayerProcess):
    def __init__(self, process_date, process_comment=None):

        self.process_name = 'Etching'

        LayerProcess.__init__(self, process_name = self.process_name,
                              process_date = process_date,
                              process_comment = process_comment)

        self.required_params = ['Recipe Name',
                                'Tool',
                                'Etched Material',
                                'DC Response (V)']

        self.required_steps  = ['Etch Time (s)',
                                'Pre-seed Time (s)',
                                'Pre-clean Time (s)']

        self.add_parameter('Tool', 'PT 770 ICP/RIE')


