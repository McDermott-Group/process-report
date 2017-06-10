from pyProcessReport.layerProcess import LayerProcess


class Cleaning(LayerProcess):
    def __init__(self, process_date, process_name, process_comment=None):

        self.process_name = process_name

        LayerProcess.__init__(self, process_name = self.process_name,
                              process_date = process_date,
                              process_comment = process_comment)

        # this is purposefully left wide open since cleaning/stripping is so variable
        self.required_params = []

        self.required_steps = []