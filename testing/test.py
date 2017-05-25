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
        simple_page_number
    from pylatex.utils import bold, italic
except ImportError:
    raise ImportError('Please install PyLaTeX (available via pip).')

SECTION_NUMBERING = True


if __name__ == '__main__':
    geometry_options = {"tmargin": "1in", "lmargin": "1in"}
    doc = Document(geometry_options=geometry_options)

    header=PageStyle('header')
    with header.create(Foot("R")):
        header.append(simple_page_number())

    datestr=datetime.now().strftime('%b %d, %Y')
    with header.create(Foot("L")):
        header.append('Report Generated: ' + datestr)

    doc.preamble.append(header)
    doc.change_document_style("header")

    with doc.create(MiniPage(align='c')):
        doc.append(LargeText(bold('Wafer 011417A')))
        doc.append(LineBreak())
        doc.append(MediumText(bold('Processing Report')))

    m0_dstr='01apr2017'
    m0_datetime=datetime.strptime(m0_dstr,'%d%b%Y')

    with doc.create(Section('Layer M0', numbering=SECTION_NUMBERING)):
        doc.append('Groundplane layer')
        doc.append(m0_datetime.strftime('%b %d, %Y'))

        with doc.create(Subsection('Deposition',numbering=SECTION_NUMBERING)):
            doc.append('Test')

            with doc.create(Subsubsection('Tool status check', numbering=SECTION_NUMBERING)):
                doc.append('AYYLAO')

    doc.generate_pdf('test', clean_tex=False)



