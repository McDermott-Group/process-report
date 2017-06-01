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

import sys
from datetime import datetime

from pylatex import Section, Subsection, Subsubsection, LargeText, MediumText, \
        PageStyle, Document, MiniPage, Head, Foot, LineBreak, \
        simple_page_number, Figure, Package
from pylatex.utils import bold, italic, NoEscape
from pylatex.base_classes import Command


class ProcessReport(object):
    def __init__(self, project_name, wafer_name, section_numbering=None):
        self.project_name = project_name
        self.wafer_name = wafer_name
        self.layers = {}
        self.numLayers = 0

        if section_numbering is None:
            self.numbering = True
        else:
            self.numbering = section_numbering

    def add_layer(self, layer):
        self.layers[self.numLayers] = layer
        self.numLayers += 1


    def build_prematter(self):

        # SETTING MARGINS
        geometry_options = {"tmargin": "1in", "lmargin": "1in"}
        self.doc = Document(geometry_options=geometry_options)

        # SETTING HEADER/FOOTER OPTIONS
        header = PageStyle('header')
        with header.create(Foot('R')):
            # header.append(simple_page_number())
            header.append(NoEscape(r'Page \thepage'))

        datestr = datetime.now().strftime('%b %d, %Y')
        with header.create(Foot("L")):
            header.append('Report Generated: ' + datestr)

        # ADD THE HEADER TO THE PREAMBLE
        self.doc.preamble.append(header)
        self.doc.preamble.append(Package('hyperref'))
        self.doc.change_document_style('header')
        self.doc.append(Command('pagenumbering', arguments='roman'))

        # PAGE HEADER
        with self.doc.create(MiniPage(align='c')):
            self.doc.append(LargeText(bold(self.project_name + ' Wafer ' + self.wafer_name)))
            self.doc.append(LineBreak())
            self.doc.append(MediumText(bold('Processing Report')))

        self.doc.append(Command('tableofcontents'))
        self.doc.append(Command('pagebreak'))
        self.doc.append(Command('pagenumbering', arguments='arabic'))
        self.doc.append(Command('setcounter', arguments='page', extra_arguments='1'))

    def build_layers(self):

        for key in self.layers:

                with self.doc.create(Section('Layer ' + self.layers[key].get_id(), numbering=self.numbering)):
                    self.doc.append(self.layers[key].get_comment())

    def build_pdf(self, filename=None, save_tex=None):
        if filename is not None:
            self.filename = filename
        else:
            self.filename = 'wafer' + self.wafer_name
        if save_tex is None:
            self.clean_tex = True
        else:
            self.clean_tex = not save_tex

        self.build_prematter()
        self.build_layers()
        self.doc.generate_pdf(self.filename, clean_tex=self.clean_tex)


class Layer(object):

    def __init__(self, layer_id, layer_comment):

        self.layer_id = layer_id
        self.layer_comment = layer_comment

        self.step = {}
        self.numSteps = 0

    def get_id(self):
        return self.layer_id

    def get_comment(self):
        return self.layer_comment

    def add_step(self, layer_step):
        self.step[self.numSteps] = layer_step
        self.numSteps += 1

    def get_num_steps(self):
        return self.numSteps


class LayerProcess(object):

    def __init__(self, step_date):

        # Expected string format for date: ddmmmyyyy (e.g. 30aug2017)
        self.step_date = step_date
        self.step_datetime = datetime.strptime(self.step_date, '%d%b%Y')
        self.step_datestr = self.step_datetime.strftime('%b %d, %Y')

        # parameters listed as bullet points
        self.params = {}
        self.required_params = []

        # parameters listed as enumuerated steps
        self.steps = {}
        self.required_steps = []

    def add_parameter(self, param, value):
        self.params[param] = value

    def add_parameters(self, params_dict):
        for key in params_dict:
            self.add_parameter(key, params_dict[key])

    def add_step(self, step, value):
        self.steps[step] = value

    def add_steps(self, steps_dict):
        for key in steps_dict:
            self.add_step(key, steps_dict[key])

    def get_required(self):
        return self.required_steps, self.required_params

    def verify_required(self):

        # Checks for both sets of required parameters for the layer process
        if not (all(param in self.required_params for param in self.params) and
                all(step in self.required_steps for step in self.steps)):

            for param in self.required_params:
                if param not in self.params:
                    raise ValueError('Required parameter missing: {}'.format(param))

            for step in self.required_steps:
                if step not in self.steps:
                    raise ValueError('Required step missing: {}'.format(step))
        else:
            return True
    def get_datestr(self):
        return self.step_datestr