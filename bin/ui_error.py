# -*- coding: utf-8 -*-

# SimianWrapper: A GUI Wrapper for the Simian Similarity Analyzer,
# created by Simon Harris, featuring Kdiff3 integration to live-view files.
# Copyright (C) 2020 Francisco Serrano
#
# This program is free software: you can redistribute it
# and/or modify it under the terms of the GNU General Public License as
# published  by the Free Software Foundation, either version 3 of the License,
# or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY;
# without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
# PARTICULAR PURPOSE. See the GNU General Public License for more details.
# https://www.gnu.org/licenses/gpl-3.0.en.html
#################

# from globalFunctions import errorHandler
from PyQt5 import QtCore, QtGui, QtWidgets, uic
import sys
import os


class Ui_ErrorDialog(QtWidgets.QDialog):
    # Constructor for the initialization of the GUI elements.
    def __init__(self):
        # UI initialization; dynamic and based off of the correspoinding .ui
        # file, meaning changing the GUI in Qt Designer will result in an
        # immediate change to the file.
        super(Ui_ErrorDialog, self).__init__()
        uic.loadUi('./ui/error.ui', self)

        ''' The following code block imports all the event handlers with custom
        functions, or data that is required for custom event handling.'''

        self.ErrorText = \
            self.findChild(QtWidgets.QLabel, 'ErrorText')

        self.show()


# This code initializes the window with the specified ui file.
def main():
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_ErrorDialog()
    sys.exit(app.exec_())
