# Copyright (C) 2017 Edward Leonard
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

from datetime import datetime

class LayerProcess(object):

    def __init__(self, process_name, process_date, process_comment):

        self.process_name = process_name
        self.comment = process_comment

        # Expected string format for date: ddmmmyyyy (e.g. 30aug2017)
        self.process_date = process_date
        self.process_datetime = datetime.strptime(self.process_date, '%d%b%Y')
        self.process_datestr = self.process_datetime.strftime('%b %d, %Y')

        # parameters listed as bullet points
        self.params = {}
        self.required_params = []

        # parameters listed as enumuerated steps
        self.steps = {}
        self.required_steps = []

    def add_parameter(self, param, value):
        if param in self.params.keys():
            self.update_parameter(param, value)
        else:
            self.params[param] = value

    def add_parameters(self, params_dict):
        for key in params_dict:
            self.add_parameter(key, params_dict[key])

    def get_parameter(self, param):
        return self.params[param]

    def update_parameter(self, param, new_value):
        self.params[param] = new_value

    def add_step(self, step_dict):

        if step_dict['step number'] in self.steps:
            raise ValueError('{}: Step number {} already in use.'.format(step_dict['step'], step_dict['step number']))

        self.steps[step_dict['step number']] = step_dict

    def add_steps(self, step_dict_list):
        for step_dict in step_dict_list:
            self.add_step(step_dict)

    def get_required(self):
        return self.required_steps, self.required_params

    def verify_required(self):

        # Checks for both sets of required parameters for the layer process
        if not all(param in self.required_params for param in self.params):

            for param in self.required_params:
                if param not in self.params:
                    raise ValueError('Required parameter missing: {}'.format(param))

        if not all(step in self.required_steps for step in self.steps):

            for step in self.required_steps:
                if step not in (self.steps[step_num]['step'] for step_num in self.steps):
                    raise ValueError('Required step missing: {}'.format(step))
        else:
            return True

    def get_datestr(self):
        return self.process_datestr


