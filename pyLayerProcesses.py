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

from pyProcessReport import LayerProcess

class PT70_PECVD(LayerProcess):
    def __init__(self, step_date):
        LayerProcess.__init__(self, step_date=step_date)

        self.required_params = ['Recipe Name',
                                'Platen Temperature',
                                'Tool',
                                'Deposition Material',
                                'Thickness Target',
                                'DC Response (average)']

        self.required_steps  = ['Deposition Time',
                                'Pre-seed Time',
                                'Pre-clean Time (x2)']