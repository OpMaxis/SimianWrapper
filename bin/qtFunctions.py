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
from ui_error import Ui_ErrorDialog
from ui_form import Ui_SimianWindow
from ui_setup import Ui_SimianSetup
import sys
import os
import yaml
import getopt
import subprocess


# qtFunctions carries out the custom slots defined in the ui python files
class qtFunctions(QtCore.QObject):

    # Define a custom signal that carries the string of the file name
    opened = QtCore.pyqtSignal(str, name='fileDir')

    # This code is the general use for all times a file directory will be
    # accessed
    @QtCore.pyqtSlot()
    def browseDir(self):
        dialog = QtCore.QFileDialog(self)
        dialog.setFileMode(QtWidgets.QFileDialog.Directory)
        # dialog.setFileMode(QtWidgets.QFileDialog.List)
        dialog.Option.showDirsOnly()
        if dialog.exec_():
            dirName = dialog.selectedFiles()
            dialog.setDirectory(dirName)
            dialog.QLineEdit.setText(dirName)
            # TODO: Unit Tests
        pass

    # -This code opens the setupUi widget from the form.ui
    @QtCore.pyqtSlot()
    def openSetup(self, checked):
        # Code here
        if self.setupWindow is None:
            self.setupWindow = Ui_SimianSetup.setupUi(self.setupWindow)
            self.setupWindow = Ui_SimianSetup.retranslateUi(self.setupWindow)
        self.setupWindow.show()
        # NOTE pseudocode block:
        # call setupUi SimianSetupWidget from ui_setup.py
        # open the widget as a secondary window for SimianWrapper
        # keep the window open until closed with app.exec_()
        pass

    # -This code runs Kdiff3 directly by using the directory.
    # If no directory is given, error message will be processed
    # Otherwise.
    @QtCore.pyqtSlot()
    def runKdiff3(self):
        # Code here
        fileList = self.ResultsTable.selectedItems()
        file1 = fileList[0]
        file2 = fileList[1]
        file3 = fileList[2]
        with open((os.path.join(os.pardir, 'settings.yaml'))) as yamlFile:
            newFileName = yaml.load(yamlFile, Loader=yaml.FullLoader)
            compareFile = newFileName.get("outputFile")
            kDiff3FileDir = newFileName.get("kDiff3WorkFileDir")
            if kDiff3FileDir or file1 or file2 is None:
                qtFunctions.errorHandler(self, FileNotFoundError)
            elif Ui_SimianSetup.Kdiff3MergeButton.isChecked() and compareFile is not None:
                process = subprocess.Popen(str[kDiff3FileDir, file1, file2, file3, newFileName])
            elif Ui_SimianSetup.Kdiff3MergeButton.isChecked() and compareFile is None:
                process = subprocess.Popen(str[kDiff3FileDir, file1, file2, file3])
            elif not Ui_SimianSetup.Kdiff3MergeButton.isChecked():
                process = subprocess.Popen(str[kDiff3FileDir, file1, file2])
            else:
                qtFunctions.errorHandler(self, RuntimeError)
        pass

    # -This code runs Simian by calling the CLI arguments and using
    # simianFileDir for the directory that was is listed.
    # If no directory is given, error message will be processed
    # -The second effect will be producing the results by reading the CLI lines
    # directly from prompt
    @QtCore.pyqtSlot()
    def runSimian(self):
        self.openedFileDir = QtGui.QLineEdit()
        # Code here
        if self.openedFileDir is None:
            qtFunctions.errorHandler(self, FileNotFoundError)
        else:
            # yamlFile = open((os.path.join(os.pardir, 'settings.yaml')))
            with open((os.path.join(os.pardir, 'settings.yaml'))) as yamlFile:
                # safe_load_all calls a generator object which we iterate over
                settingsFile = yaml.safe_load_all(yamlFile)
                # This would call simianFileOptionsDefault, which we do not need
                settingsFile.__next__()
                # We save the second dictionary document
                simianFileOptionsSaved = settingsFile.__next__()
                # This is kdDiff3SavedSettings, which we do not need
                settingsFile.__next__()
                # we, however, need fileDirsSaved
                fileDirsSaved = settingsFile.__next__()
                # a for loop breaks the content because it will iterate over the other
                # dictionaries, and a while loop
                simianWorkFileDir = fileDirsSaved['fileDirsSaved'] \
                    .get('SimianWorkFileDir')
                if simianWorkFileDir is None:
                    qtFunctions.errorHandler(self, FileNotFoundError)
                    print("There are no results")
                    print(settingsFile.values())
                    # use defaults to render the results
                else:
                    print("There are results")
                    settingsList = simianFileOptionsSaved.get('simianFileOptionsSaved')
                    for value in settingsList.values():
                        if value is True:
                            # Convert True to + symbol for Simian
                            settingsList[value] = "+"
                        elif value is False:
                            # Convert False to - symbol for Simian
                            settingsList[value] = "-"
                        else:
                            # If the value is not truthy or falsy, move on
                            break
                        settingsList['simianFileOptionsSaved'].items()
                    executedArgs = subprocess.Popen(str[simianWorkFileDir, ,self.openedFileDir])
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
            settingsFile = yaml.load(yamlFileSaved, Loader=yaml.FullLoader)
            # safe_load_all calls a generator object which we iterate over
            settingsFile = yaml.safe_load_all(yamlFile)
            # We need to reference default file options for saveSettings
            simianFileOptionsDefault = settingsFile.__next__()
            # We save the second dictionary document for the saved settings
            simianFileOptionsSaved = settingsFile.__next__()
            # This is kdDiff3SavedSettings, which we do not need
            settingsFile.__next__()
            # we, however, need fileDirsSaved
            fileDirsSaved = settingsFile.__next__()
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
            # safe_load_all calls a generator object which we iterate over
            settingsFile = yaml.safe_load_all(yamlFileSaved)
            # We need to reference default file options for saveSettings
            simianFileOptionsDefault = settingsFile.__next__()
            # We save the second dictionary document for the saved settings
            simianFileOptionsSaved = settingsFile.__next__()
            # This is kdDiff3SavedSettings, which we do not need
            settingsFile.__next__()
            # we do not need to update fileDirsSaved, only
            # simianFileOptionsSaved
            settingsFile.__next__()
            simianFileOptionsSaved.update(simianFileOptionsDefault)
            # TODO: reset the boolean checked states and values according to
            # the saved values in simianFileOptionsSaved or
            # simianFileOptionsDefault, whichever turns out to be easier
            yaml.safe_dump(simianFileOptionsSaved, stream=yamlFileSaved)
        print("Default settings reset")

    # - This code is called for whenever an error is called by any means
    @QtCore.pyqtSlot()
    def errorHandler(self, ErrorEvent):
        if self.errorWidget.isVisible():
            self.errorWidget.hide()
        else:
            self.errorWidget = Ui_ErrorDialog.setupUi(self.errorWidget)
            self.errorWidget.retranslateUi(self.errorWidget)
            if ErrorEvent is FileNotFoundError:
                self.errorWidget.ErrorText.setText(_translate("ErrorDialog",
                    "Invalid directories. Please check your saved directories. "))
            else:
                self.ErrorText.setText(_translate("ErrorDialog", "An error has occurred. "))
            self.errorWidget.show()
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
