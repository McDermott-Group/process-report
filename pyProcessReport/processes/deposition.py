from pyProcessReport.layerProcess import LayerProcess


class LeskerSingleSputter(LayerProcess):
    def __init__(self, process_date, process_comment=None):

        self.process_name = 'Sputtering'

        LayerProcess.__init__(self, process_name = self.process_name,
                              process_date = process_date,
                              process_comment = process_comment)

        self.required_params = ['Base Pressure (Torr)',
                                'Indium Heat Sinking?',
                                'Tool',
                                'Sputtered Material',
                                'Ion Mill?',
                                'Target Cleaning Power (W)',
                                'Deposition Power (W)']

        self.required_steps  = ['Target Cleaning Time (s)',
                                'Deposition Time (s)']

        self.add_parameter('Tool', 'Lesker System')


class LeskerJunctionSputter(LayerProcess):
    def __init__(self, process_date, process_comment=None):

        self.process_name = 'Junction Sputtering'

        LayerProcess.__init__(self, process_name = self.process_name,
                              process_date = process_date,
                              process_comment = process_comment)

        self.required_params = ['Base Pressure (Torr)',
                                'Indium Heat Sinking?',
                                'Tool',
                                'Junction Technology',
                                'Top Electrode Cleaning Power (W)',
                                'Top Electrode Deposition Power (W)',
                                'O2 Seed Pressure (mTorr)',
                                'O2 Growth Pressure (mTorr)',
                                'Ion Mill Pressure (Torr)']

        self.required_steps  = ['Top Electrode Target Cleaning Time (s)',
                                'Top Electrode Deposition Time (s)',
                                'O2 Seed Time (min)',
                                'O2 Growth Time (min)',
                                'Ion Mill Time (s)']

        self.add_parameter('Tool', 'Lesker System')


class PT70PECVD(LayerProcess):
    def __init__(self, process_date, process_comment=None):

        self.process_name = 'PECVD Deposition'

        LayerProcess.__init__(self, process_name = self.process_name,
                              process_date = process_date,
                              process_comment = process_comment)

        self.required_params = ['Recipe Name (ch1)',
                                'Platen Temperature (C)',
                                'Tool',
                                'Deposition Material',
                                'Thickness Target (nm)',
                                'DC Response (V)']

        self.required_steps = ['Deposition Time (s)',
                                'Pre-seed Time (s)',
                                'Pre-clean Time (x2, s)']

        self.add_parameter('Tool', 'PT 70')
