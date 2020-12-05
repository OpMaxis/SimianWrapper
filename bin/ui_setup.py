# -*- coding: utf-8 -*-
#####################
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


from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import pyqtSlot, QObject, QStandardPaths
import sys
import os
import configparser


class Ui_SimianSetup(QtWidgets.QMainWindow):
    # Constructor for the initialization of the GUI elements.
    def __init__(self):
        # set the dialog to none for initialization
        self.dialog = None

        # set the dirpath which will be used by the file saving and restoring
        self.dirPath = resource_path(("settings.ini"))

        # UI initialization; dynamic and based off of the correspoinding .ui
        # file, meaning changing the GUI in Qt Designer will result in an
        # immediate change to the file.
        uiPath = '/ui'
        super(Ui_SimianSetup, self).__init__()
        uic.loadUi('setup.ui', self)

        ''' The following code block imports all the event handlers with custom
        functions, or data that is required for custom event handling.'''

        # connects the simianFileDirButton to browseFileSimian
        self.simianFileDirButton = \
            self.findChild(QtWidgets.QPushButton, 'simianFileDirButton')
        self.simianFileDirButton.clicked.connect(self.browseFileSimian)

        # connects the Kdiff3FileDirButton to browseFileKdiff3
        self.Kdiff3FileDirButton = \
            self.findChild(QtWidgets.QPushButton, 'Kdiff3FileDirButton')
        self.Kdiff3FileDirButton.clicked.connect(self.browseFileKdiff3)

        # calls the instance variable for the file Line so we can edit
        # it in browseFileSimian
        self.simianFileDirLine = \
            self.findChild(QtWidgets.QLineEdit, 'simianFileDirLine')

        # calls the kDiff3FileDirLine for use in browseFileKdiff3
        self.Kdiff3FileDirLine = \
            self.findChild(QtWidgets.QLineEdit, 'Kdiff3FileDirLine')

        # calls the button to saveSettings for the saveSettings method
        self.OptionsBox.clicked['QAbstractButton*'].connect(self.saveSettings)

        self.refreshData()
        # show the window
        self.show()

    def refreshData(self):
        # initialize a read_config for our file reader
        read_config = configparser.ConfigParser()
        # send it to read our pretdetermined path, one directory up
        read_config.read(self.dirPath)

        # create the file dir variables based on the .ini values
        kDiff3FileDir = read_config.get("fileDirsSaved", "kDiff3WorkFileDir")
        simianFileDir = read_config.get("fileDirsSaved", "simianWorkFileDir")

        # set the text to these values
        self.simianFileDirLine.setText(simianFileDir)
        self.Kdiff3FileDirLine.setText(kDiff3FileDir)

    # This code is the general use for all times a file directory will be
    # accessed
    @pyqtSlot()
    def browseFileSimian(self):
        # calls the dialog box to open
        self.dialog = QtWidgets.QFileDialog\
            .getOpenFileName(self, caption="Open File", filter='Executables(*.exe)')
        (fileName, setFilter) = self.dialog
        self.simianFileDirLine.setText(fileName)

    # This code is the general use for all times a file directory will be
    # accessed
    @pyqtSlot()
    def browseFileKdiff3(self):
        # calls the dialog box to open
        self.dialog = QtWidgets.QFileDialog\
            .getOpenFileName(self, caption="Open File", filter='Executables(*.exe)')
        (fileName, setFilter) = self.dialog
        self.Kdiff3FileDirLine.setText(fileName)

    # - This code functions to save the settings to file
    @pyqtSlot()
    def saveSettings(self):
        # call a write_config to open a ConfigParser object
        write_config = configparser.ConfigParser()
        # add a section corresponding to our FileDirsSaved section
        write_config.add_section('fileDirsSaved')
        # set the corresponding dirs to the text in the QLineEdit boxes
        write_config.set("fileDirsSaved", "kDiff3WorkFileDir", self.Kdiff3FileDirLine.text())
        write_config.set("fileDirsSaved", "simianWorkFileDir", self.simianFileDirLine.text())
        # open the iniFile...
        with open((self.dirPath), mode='w') as iniFile:
            # write the directories to file, then close it
            write_config.write(iniFile)


# Translate asset paths to useable format for PyInstaller
def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath('.'), relative_path)

# This code initializes the window with the specified ui file.
def main():
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_SimianSetup()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
