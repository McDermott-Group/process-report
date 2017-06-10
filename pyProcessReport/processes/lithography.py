from pyProcessReport.layerProcess import LayerProcess


class Lithography(LayerProcess):
    def __init__(self, process_date, process_comment=None):

        self.process_name = 'Lithography'

        LayerProcess.__init__(self, process_name = self.process_name,
                              process_date = process_date,
                              process_comment = process_comment)

        self.required_params = ['Softbake Temperature (C)',
                                'Post-exposure Bake Temperature (C)',
                                'Exposure Tool',
                                'Photoresist',
                                'Thickness Target (um)',
                                'Developer',
                                'Spinner Used']

        self.required_steps = ['Spin Recipe',
                               'Softbake Time (s)',
                               'Post-exposure Bake Time (s)',
                               'Exposure Time (s)',
                               'Develop Time (s)',
                               'DI H2O Rinse Time (s)']