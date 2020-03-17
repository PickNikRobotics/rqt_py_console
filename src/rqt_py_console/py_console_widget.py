# Software License Agreement (BSD License)
#
# Copyright (c) 2012, Dorian Scholz
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following
#    disclaimer in the documentation and/or other materials provided
#    with the distribution.
#  * Neither the name of Willow Garage, Inc. nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

import os
from ament_index_python.resources import get_resource

from python_qt_binding import loadUi
from python_qt_binding.QtCore import qDebug, qWarning
from python_qt_binding.QtWidgets import QWidget
from python_qt_binding.QtGui import QIcon
from rqt_py_console.py_console_text_edit import PyConsoleTextEdit


class PyConsoleWidget(QWidget):

    def __init__(self, context=None):
        super(PyConsoleWidget, self).__init__()

        _, package_path = get_resource('packages', 'rqt_py_console')
        ui_file = os.path.join(
            package_path, 'share', 'rqt_py_console', 'resource', 'py_console_widget.ui')

        loadUi(ui_file, self, {'PyConsoleTextEdit': PyConsoleTextEdit})
        self.setObjectName('PyConsoleWidget')

        self.load_button.setIcon(QIcon.fromTheme('document-open'))
        self.save_button.setIcon(QIcon.fromTheme('document-save'))
        self.save_as_button.setIcon(QIcon.fromTheme('document-save-as'))

        self.load_button.clicked[bool].connect(self._handle_load_clicked)
        self.save_button.clicked[bool].connect(self._handle_save_clicked)
        self.save_as_button.clicked[bool].connect(self._handle_save_as_clicked)
        qWarning("yolo")
        print("Dafuq")

        my_locals = {
            'context': context
        }
        self.py_console.update_interpreter_locals(my_locals)
        self.py_console.print_message(
            'The poop variable "context" is set to the PluginContext of this plugin.')

        qWarning("brolo brolo brolo")

        qWarning("yolo")
        print("Dafuq")

        # self.py_console.exit.connect(context.close_plugin)

    def _handle_load_clicked(self):
        qWarning("error")
        qWarning(error)
        filenames = \
            QFileDialog.getOpenFileNames(self, self.tr('Load from Files'), '.',
                                         self.tr('EGSE Console Python Script {.py} (*.py)'))
        for filename in filenames[0]:
            self.load_bag(filename)

    def _handle_save_clicked(self):
        filename = \
            QFileDialog.getSaveFileName(self, self.tr('Save selected region to file...'), '.',
                                        self.tr('Python files {.py} (*.py)'))
    def _handle_save_as_clicked(self):
        filename = \
            QFileDialog.getSaveFileName(self, self.tr('Save selected region to file...'), '.',
                                        self.tr('Python files {.py} (*.py)'))
