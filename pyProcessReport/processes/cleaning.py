from pyProcessReport.layerProcess import LayerProcess


class Strip(LayerProcess):
    def __init__(self, process_date, process_comment=None):

        self.process_name = 'Resist Removal'

        LayerProcess.__init__(self, process_name = self.process_name,
                              process_date = process_date,
                              process_comment = process_comment)

        self.required_params = ['Removal Temperature (C)']

        self.required_steps = []