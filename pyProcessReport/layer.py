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

class Layer(object):

    def __init__(self, layer_id, layer_comment):

        self.layer_id = layer_id
        self.layer_comment = layer_comment

        self.process = {}
        self.num_process = 0
        self.images = {}

    def get_id(self):
        return self.layer_id

    def get_comment(self):
        return self.layer_comment

    def add_process(self, layer_process):
        layer_process.verify_required()
        self.process[self.num_process] = layer_process
        self.num_process += 1

    def add_image(self, file, caption):
        self.images[file] = caption

    def get_images(self):
        return self.images

    def get_num_processes(self):
        return self.num_process

    def get_processes(self):
        return self.process