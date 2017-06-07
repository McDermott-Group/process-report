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
        simple_page_number, Figure, Package, Tabular
from pylatex.utils import bold, italic, NoEscape
from pylatex.base_classes import Command
from pylatex.lists import Enumerate, Description


class ProcessReport(object):
    def __init__(self, project_name, wafer_name, section_numbering=None):
        self.project_name = project_name
        self.wafer_name = wafer_name
        self.layers = {}
        self.numLayers = 0
        self.numSteps = 0

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
        self.doc = Document(geometry_options = geometry_options)

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
            processes = self.layers[key].get_processes()

            with self.doc.create(Section('Layer ' + self.layers[key].get_id(), numbering=self.numbering)):
                self.doc.append(self.layers[key].get_comment())
                if len(self.layers[key].get_images()) is not 0:
                    self.build_layer_images(key)

                for process in processes:
                    self.build_layer_process(processes[process])

    def build_layer_process(self, process):
        with self.doc.create(Subsection(numbering=self.numbering,
                                        title=process.process_name + ' (' + process.get_datestr() + ')')):
            if process.comment is not None:
                self.doc.append(process.comment)

            if len(process.params.keys()) > 0:
                self.build_process_params(process.params)

            if len(process.steps.keys()) > 0:
                self.build_process_steps(process.steps)

    def build_layer_images(self, layer):
        for key in self.layers[layer].get_images():
            with self.doc.create(Figure(position='h!')) as layer_pic:
                layer_pic.add_image(key)
                try:
                    layer_pic.add_caption(self.layers[layer].get_images()[key])
                except:
                    raise ValueError('All images must be captioned.')


    def build_process_params(self, params):
        with self.doc.create(Subsubsection('Parameters', numbering=self.numbering)):
            # with self.doc.create(Description()) as desc:
            #     for param,val in sorted(params.items()):
            #         desc.add_item(param, NoEscape(Command('hfill').dumps()) +  ' ' + val)

            with self.doc.create(Tabular('l|c')) as table:
                # table.add_row('Parameters','a')
                table.add_hline()
                for param,val in sorted(params.items()):
                    table.add_row((bold(param), val))

    def build_process_steps(self, steps):
        with self.doc.create(Subsubsection('Steps', numbering=self.numbering)):
            if self.numSteps == 0:
                self.numSteps += 1
            with self.doc.create(Enumerate(enumeration_symbol=r"\arabic*)", options={'start': self.numSteps})) as enum:
                for key in steps:
                    enum.add_item(steps[key]['step'] + ': ' + steps[key]['value'])
                    self.numSteps += 1



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