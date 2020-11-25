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

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os
import yaml
import getopt


# qtFunctions carries out the custom slots defined in the ui python files
class qtFunctions(QtCore.QObject):

    # This code is the general use for all times a file directory will be
    # accessed
    @QtCore.pyqtSlot()
    def browseDir(self):
        dialog = QtCore.QFileDialog(self)
        dialog.setFileMode(QtWidgets.QFileDialog.Directory)
        dialog.setFileMode(QtWidgets.QFileDialog.List)
        dialog.Option.showDirsOnly()
        if dialog.exec_():
            dirName = dialog.selectedFiles()
            dialog.setDirectory(dirName)
            dialog.QLineEdit.setText(dirName)
            # TODO: Unit Tests
        pass

    # -This code opens the setupUi widget from the form.ui
    @QtCore.pyqtSlot()
    def openSetup(self):
        # Code here
        self.setupUi = Ui_SimianSetup(self)
        # NOTE pseudocode block:
        # call setupUi SimianSetupWidget from ui_setup.py
        # open the widget as a secondary window for SimianWrapper
        # keep the window open until closed with app.exec_()
        pass

    # -This code runs Kdiff3 directly by using the directory.
    # If no directory is given, error message will be processed
    # Otherwise.
    @QtCore.pyqtSlot()
    def runKdiff3(self, kDiff3FileDir):
        # Code here
        if kDiff3FileDir is None:
            qtFunctions.qerrorHandler(self, FileNotFoundError)
        pass

    # -This code runs Simian by calling the CLI arguments and using
    # simianFileDir for the directory that was is listed.
    # If no directory is given, error message will be processed
    # -The second effect will be producing the results by reading the CLI lines
    # directly from prompt
    @QtCore.pyqtSlot()
    def runSimian(self, simianFileDir):
        # Code here
        if simianFileDir is None:
            qtFunctions.errorHandler(self, FileNotFoundError)
        else:
            # yamlFile = open((os.path.join(os.pardir, 'settings.yaml')))
            with open((os.path.join(os.pardir, 'settings.yaml'))) as yamlFile:
                settingsFile = yaml.load(yamlFile, Loader=yaml.FullLoader)

                if settingsFile.get("SimianWorkFileDir") \
                        is None:
                    print("There are no results")
                    print(settingsFile.values())
                    # use defaults to render the results
                else:
                    print("There are results")
                    print(settingsFile.values())

                # TODO: if-else loop which checks for valid data
                # in savedDataArray
                # if there is saved settings, use those options from the array
                # else, use defaults

            # args = str(sys.argv)
            # nums = len(sys.argv)
            # yamlFile.close()

    # - This code functions to save the settings to file
    @QtCore.pyqtSlot()
    def saveSettings(self):
        with open((os.path.join(os.pardir, 'settings.yaml'))) as yamlFileSaved:

        # NOTE pseudocode block
        # with open yamlFile:
        #   call dictionary for simianFileOptionsSaved
        #   for each dictionary key/value pair in simianFileOptionsSaved:
        #     call widget boolean values to results
        #     save to file
        #   call dictionary for FileDirsSaved
        #   for each dictionary key/value pair in FileDirsSaved
        pass

    # - This code removes all values from simianFileOptionsSaved, resetting to
    # simianFileOptionsDefault
    @QtCore.pyqtSlot()
    def resetDefaults(self):
        with open((os.path.join(os.pardir, 'settings.yaml'))) as yamlFileSaved:
            with open((os.path.join(os.pardir, 'settings_defaults.yaml'))) \
                    as yamlFileDefault:
                settingsFileDefault = yaml.load(yamlFileDefault, Loader=yaml.FullLoader)
                settingsFileSaved = settingsFileDefault.copy()
                yaml.dump(settingsFileSaved, stream=yamlFileSaved)
        print("Default settings reset")

    # - This code is called for whenever an error is called by any means
    @QtCore.pyqtSlot()
    def errorHandler(self, ErrorEvent):
        # NOTE pseudocode block
        # call setupUi SimianErrorWidget from ui_error.py
        # open the widget as a secondary window for SimianWrapper
        # keep the window open until closed with app.exec_()
        # switch(error):
        # FileNotFoundError
        # text: "The directory" + files "was not found."
        # break
        # default:
        # break
        pass
