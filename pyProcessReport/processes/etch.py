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

        self.add_parameter('Tool', 'Unaxis 790')


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


