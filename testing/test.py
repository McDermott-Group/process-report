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

try:
    from pylatex import Section, Subsection, Subsubsection, LargeText, MediumText, \
        PageStyle, Document, MiniPage, Head, Foot, LineBreak, \
        simple_page_number, Figure, Package
    from pylatex.utils import bold, italic
except ImportError:
    raise ImportError('Please install PyLaTeX (available via pip install pylatex).')

from pylatex.base_classes import Command

# the default in PyLaTeX is to have un-numbered sections, so this changes it
SECTION_NUMBERING = True


if __name__ == '__main__':

    # SETTING MARGINS
    geometry_options = {"tmargin": "1in", "lmargin": "1in"}
    doc = Document(geometry_options=geometry_options)

    # SETTING HEADER/FOOTER OPTIONS
    header=PageStyle('header')
    with header.create(Foot("R")):
        header.append(simple_page_number())

    datestr=datetime.now().strftime('%b %d, %Y')
    with header.create(Foot("L")):
        header.append('Report Generated: ' + datestr)

    # ADD THE HEADER TO THE PREAMBLE
    doc.preamble.append(header)
    doc.preamble.append(Package('hyperref'))
    doc.change_document_style("header")



    # PAGE HEADER
    with doc.create(MiniPage(align='c')):
        doc.append(LargeText(bold('Wafer 011417A')))
        doc.append(LineBreak())
        doc.append(MediumText(bold('Processing Report')))

    doc.append(Command('tableofcontents'))

    # process strings
    m0_dstr='01apr2017'
    m0_datetime=datetime.strptime(m0_dstr,'%d%b%Y')
    plot_filename = 'kitten.jpg'

    # NEW LAYER
    with doc.create(Section('Layer M0', numbering=SECTION_NUMBERING)):
        doc.append('Groundplane layer')
        doc.append(m0_datetime.strftime('%b %d, %Y'))

        # NEW LAYER STEP
        with doc.create(Subsection('Deposition',numbering=SECTION_NUMBERING)):
            doc.append('Test')

            # NEW PROCESS STEP
            with doc.create(Subsubsection('Tool status check', numbering=SECTION_NUMBERING)):
                doc.append('AYYLMAO')

                # A PLOT
                with doc.create(Figure(position='h!')) as stress_pic:
                    stress_pic.add_image(plot_filename, width='4in')
                    stress_pic.add_caption('The cat ate my wafer.')

    # Generate output PDF
    doc.generate_pdf('test', clean_tex=False)



