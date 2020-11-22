# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os
import yaml
import getopt


# This code is the general use for all times a file directory will be accessed
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

# -This code runs Simian by calling the CLI arguments and using simianFileDir
# for the directory that was is listed. If no directory is given, error message
# will be processed
# -The second effect will be producing the results by reading the CLI lines
# directly from prompt
def runSimian(self, simianFileDir):
    # Code here
    if simianFileDir is None:
        errorHandler(self, FileNotFoundError)
    else:
        # yamlFile = open((os.path.join(os.pardir, 'settings.yaml')))
        with open((os.path.join(os.pardir, 'settings.yaml'))) as yamlFile:
            data = yaml.load(yamlFile, Loader=yaml.FullLoader)
            # TODO: if-else loop which checks for valid data in savedDataArray
            # if there is saved settings, use those options from the array
            # else, use defaults

        # args = str(sys.argv)
        # nums = len(sys.argv)
        # yamlFile.close()
    pass


# -This code runs Kdiff3 directly by using the directory.
# If no directory is given, error message will be processed
# Otherwise.
def runKdiff3(self, kDiff3FileDir):
    # Code here

    if kDiff3FileDir is None:
        errorHandler(self, FileNotFoundError)
    pass


# -This code opens the setupUi widget from the form.ui
def openSetup(self):
    # Code here
    self.setupUi = Ui_SimianSetup(self)

    # NOTE pseudocode block:
    # call setupUi SimianSetupWidget from ui_setup.py
    # open the widget as a secondary window for SimianWrapper
    # keep the window open until closed with app.exec_()
    pass


# - This code functions to save the settings to file
def saveSettings(self):
    # NOTE pseudocode block
    # with open yamlFile:
    #   call dictionary for simianFileOptionsSaved
    #   for each dictionary key/value pair in simianFileOptionsSaved:
    #     call widget boolean values to results
    #     save to file
    #   call dictionary for FileDirsSaved
    #   for each dictionary key/value pair in FileDirsSaved
    pass


# - This code is called for whenever an error is called by any means
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
