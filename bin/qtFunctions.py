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
import os
import yaml
import subprocess


# qtFunctions carries out the custom slots defined in the ui python files
class qtFunctions(QtCore.QObject):

    # This code is the general use for all times a file directory will be
    # accessed
    @QtCore.pyqtSlot()
    def browseDir(self):
        # calls the dialog box to open
        dialog = QtCore.QFileDialog(self)

        # sets the dialog file open option to Directory, only allowing
        # directory selects
        dialog.setFileMode(QtWidgets.QFileDialog.Directory)

        # dialog.setFileMode(QtWidgets.QFileDialog.List)
        # set the dialog to only show directories, not files
        dialog.Option.showDirsOnly()
        # if the dialog is running...
        if dialog.exec_():
            # set the directory name to the currently selected file
            dirName = dialog.selectFile(dialog.fileSelected())

            # set the directory to that directory name
            dialog.setDirectory(dirName)
            dialog.QLineEdit.setText(dirName)
            # TODO: Unit Tests: additionally, make sure the
            # line change reflects to the QLineEdit.text
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

        # create a file list from the selected items on the resultsTable
        fileList = self.ResultsTable.selectedItems()
        file1 = fileList[0]
        file2 = fileList[1]
        file3 = fileList[2]
        with open((os.path.join(os.pardir, 'settings.yaml'))) as yamlFile:
            # This would call simianFileOptionsDefault, which we do not need
            yamlFile.__next__()

            # This would call simianFileOptionsSaved, which we do not need
            yamlFile.__next__()

            # we, however, need fileDirsSaved
            fileDirsSaved = yamlFile.__next__()

            # compareFile is the QLineEdit text from the kDiff3 File Options
            outputFile = self.QtGui.QLineEdit.text()

            # kDiff3FileDir is called from the yamlFile
            # in the nested dictionary
            kDiff3FileDir = fileDirsSaved['fileDirsSaved']\
                .get("kDiff3WorkFileDir")

            # ifKdiff3FileDir is not set, or there are no selected items
            # in the list...
            if kDiff3FileDir is None or not bool(fileList):

                # Call the error handler
                qtFunctions.errorHandler(self, FileNotFoundError)

            # if there were less than 2 items selected, or more than 3 items..
            if fileList.len() > 2 or fileList.len() < 3:

                # call ErrorHandler with an UnboundLocalError()
                qtFunctions.errorHandler(self, UnboundLocalError)

            # if the selected item list is composed of 2 items...
            if fileList.len() == 2:

                # if the merge button is checked...
                if self.Kdiff3MergeButton.isChecked():

                    # if there is no supplied output file, assume a merger
                    if outputFile is None:
                        subprocess.run([kDiff3FileDir, file1, file2, '-m'])

                    # else, run kDiff3 with the output file being generated
                    else:
                        subprocess.run([kDiff3FileDir, file1, file2, '-o',
                                        outputFile])

                # if the merge button is not checked,
                # just do a compare operation
                else:
                    subprocess.run([kDiff3FileDir, file1, file2])

            # else, if the file list length is 3...
            elif fileList.len() == 3:

                # check if the merge button is checked...
                if self.Kdiff3MergeButton.isChecked():

                    # if there is no outputFile, assume a merger...
                    if outputFile is None:
                        subprocess.run([kDiff3FileDir, file1, file2, file3,
                                        '-m'])

                    # else, run kDiff3 with the output file being generated
                    else:
                        subprocess.run([kDiff3FileDir, file1, file2, file3,
                                        '-o', outputFile])

                # if there is no merge button checked, just run a compare
                else:
                    subprocess.run([kDiff3FileDir, file1, file2, file3])

            # else, if an unknown error occurs...
            else:
                # declare RuntimeError()
                qtFunctions.errorHandler(self, RuntimeError)

    # -This code runs Simian by calling the CLI arguments and using
    # simianFileDir for the directory that was is listed.
    # If no directory is given, error message will be processed
    # -The second effect will be producing the results by reading the CLI lines
    # directly from prompt
    @QtCore.pyqtSlot()
    def runSimian(self):
        # Initialize combinedArgs as an empty list, which will be populated
        # later
        combinedArgs = list()

        # openedFileDir corresponds to the main window's FileDirectoryText
        # QLineEdit
        openedFileDir = self.FileDirectoryText.text()
        # If there is no file directory to run simian on, end early with error
        if self.openedFileDir is None:
            qtFunctions.errorHandler(self, FileNotFoundError)
        # otherwise, run through runSimian
        else:
            # with statement that opens the settings.yaml file
            with open((os.path.join(os.pardir, 'settings.yaml'))) as yamlFile:
                # safe_load_all calls a generator object which we iterate over
                settingsFile = yaml.safe_load_all(yamlFile)
                # This would call simianFileOptionsDefault, which we do not need
                settingsFile.__next__()
                # We save the second dictionary document
                simianFileOptionsSaved = settingsFile.__next__()
                # we, however, need fileDirsSaved
                fileDirsSaved = settingsFile.__next__()
                # a for loop breaks the content because it will iterate over
                # the other dictionaries, and a while loop would cause
                # local encapsulaton which we do not want

            # get the workfileDirectory of Simian by looking through
            # the subdirectory fileDirsSaved
            simianWorkFileDir = fileDirsSaved['fileDirsSaved'] \
                .get('SimianWorkFileDir')
            # If the workfileDirectory has not been defined yet, end early
            if simianWorkFileDir is None:
                qtFunctions.errorHandler(self, FileNotFoundError)
            # Otherwise, continue onwards
            else:
                # create a dictionary of simianFileOptionsSaved that only
                # grabs the subdirectory to save typing in the future
                simianNestedDict = simianFileOptionsSaved
                ['simianFileOptionsSaved']

                # For the key value pairs in the nested dictionary...
                for key, value in simianNestedDict.items():

                    # if the value is truthy, update the value pair to be
                    # + with space
                    if value is True:
                        updatedValue = simianNestedDict[key] = '+'
                        combinedArgs.append('-' + key + updatedValue)

                    # else, if the value is falsy, update the value pair to be
                    # - with space
                    elif value is False:
                        updatedValue = simianNestedDict[key] = '-'
                        combinedArgs.append('-' + key + updatedValue)

                    # if the value is not a truthy or falsy value...
                    # see threshold, which is an integer
                    else:
                        # append the threshold separately, changing the int
                        # to a string value for compatability
                        combinedArgs.append('-' + key + '=' + str(value))
                        break
                    # insert the simianWorkFileDir, which will be the
                    # executing process where simian.exe will be located
                    combinedArgs.insert(0, simianWorkFileDir)
                    # put the openedFileDir at the end of the argument list
                    combinedArgs.append(openedFileDir)

                    # contentText stores the output gathered from
                    # Simian.exe with combinedArgs, with the additional
                    # parameters setting the file to save as a string
                    # with utf-8 encoding
                    contentText = \
                        subprocess.check_output(combinedArgs, text=True, encoding="utf-8")
                    # Remove the copyright from Simian's output
                    stringWithoutSimian = contentText.split("\n", 4)[4]

                    # remove the ending output, leaving only valid results
                    stringWithoutOutput = stringWithoutSimian.split('\n')[:-4]

                    # split the stringWithoutOutput into a
                    # list of string objects

                    listOfResults = stringWithoutOutput.splitlines()

                    # make an empty List out of foundResults
                    # that will be populated
                    foundResults = []

                    # initialize a counter for the list in order to organize
                    # results
                    i = 0
                    # if there are no results for duplicates from Simian...
                    # NOTE: This outcome also occurs if the openedFileDir is
                    # invalid. This behavior is native to Simian's processing.
                    if 'Found 0 duplicate lines in 0 blocks in 0 files' \
                            in stringWithoutSimian:
                        # end early, setting foundNumber to 0
                        foundNumber = 0
                        # insert a single column into the list
                        foundResults.insert(i, '{foundNumber} Results')

                        # add this item to the resultsTable
                        self.ResultsTable.addItems(foundResults)

                    # else, if there are duplicates
                    else:
                        # while we have not fully traversed the listOfResults..
                        while i < len(listOfResults):
                            # pop the current item
                            lineString = listOfResults.pop(i)
                            # If the line corresponds to a found line...
                            if 'Found' in lineString and \
                                    'following files:' in lineString:

                                # get the foundNumber by splitting and getting
                                # the value of the second object, which will
                                # always be the number
                                foundNumber = int(lineString.split(' ')[1])
                                # fingerprint = lineString.split(' ')[6]

                                # insert the number of found results into
                                # the current index
                                foundResults.insert(i, foundNumber)
                            # else, if this line is stating the files that
                            # Simian is detecting duplicates between...
                            elif 'Between lines' in lineString:
                                # call a helper method to parse the path
                                foundFileName = parsePath(lineString)
                                # insert a nested result within the index
                                # of our foundNumber
                                foundResults['{i}'].insert(
                                    {i, foundFileName})
                            # else, if an error happens
                            else:
                                # we currently don't know what error would
                                # cause this, but throw an error handler window
                                qtFunctions.errorHandler(self, RuntimeError)
                            # increment i at the end
                            i += 1
                        # when we have finished generating the list, sort
                        # with a helper method to sort by the highest number of
                        # results to the lowest results
                        foundResults.sort(reverse=True, key=sortList(foundNumber))

                        # add this list entirely to the ResultsTable QListWidget
                        self.ResultsTable.addItems(foundResults)


# helper method for runSimian to find the path
def parsePath(string):
    # initialize count to 0
    count = 0
    # while we haven't found a string that resembles a path...
    while True:
        # increase the count
        count += 1
        # split each string from the start to the end, from the first string
        newString = string.split(string[:count], 1)
        # if a path is deemed to exist from this file...
        if os.path.exists(newString[1]):
            # get the new string
            return newString
            # break from the loop to terminate the otherwise infinite result
            break


# sorter for the foundResults list in runSimian
def sortList(sorter):
    return sorter['foundNumber']

    # - This code functions to save the settings to file
    @QtCore.pyqtSlot()
    def saveSettings(self):
        with open((os.path.join(os.pardir, 'settings.yaml'))) as yamlFileSaved:
            # safe_load_all calls a generator object which we iterate over
            settingsFile = yaml.safe_load_all(yamlFileSaved)

            # this would call simianFileOptionsDefault, which we do not need
            settingsFile.__next__()

            # We save the second dictionary document for the saved settings
            simianFileOptionsSaved = settingsFile.__next__()

            # we save fileDirsSaved to save these results to file
            fileDirsSaved = settingsFile.__next__()

            # for each QCheckBox located in the main window...
            for checkstate in self.findChildren(QtWidgets.QCheckBox):
                # set the value of True or False based on the checkbox
                newValue = checkstate.isChecked()

                # get a tuple to form an iterator through each
                # simianFileOptionsSaved dictionary key:value pair
                simianTuples = simianFileOptionsSaved['simianFileOptionsSaved']\
                    .items()

                # unpack the tuple object; we are interested in simianKey,
                # and thus have no use for the original value, only unpacking
                # it to avoid errors
                (simianKey, originalValue) = simianTuples

                # Update the simianFileOptionsSaved with the new checked state
                simianFileOptionsSaved['simianFileOptionsSaved']\
                    .update(simianKey, newValue)

            # since threshold is the only non-checkbox value, we can check it
            # independently and do not need to unpack the key:value pair here
            # as a tuple
            newThresholdValue = self.SimianThresholdNumber.value()

            # update the threshold with the new threshold value from the
            # QSpinBox
            simianFileOptionsSaved['simianFileOptionsSaved']\
                .update('threshold', newThresholdValue)

            # Update the fileDirsSaved from simianWorkFileDir
            # from simianFileDirLine's text box
            fileDirsSaved['fileDirsSaved']\
                .update('simianWorkFileDir', self.simianFileDirLine.text())

            # Update the fileDirsSaved from kDiff3WorkFileDir
            # from kDiff3FileDirLine's text box
            fileDirsSaved['fileDirsSaved']\
                .update('kDiff3WorkFileDir', self.kDiff3FileDirLine.text())

            yaml.safe_dump(simianFileOptionsSaved, stream=yamlFileSaved)
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
            # we do not need to update fileDirsSaved, only
            # simianFileOptionsSaved
            settingsFile.__next__()
            # for each QCheckBox located in the main window...
            for checkstate in self.findChildren(QtWidgets.QCheckBox):
                # get a tuple to form an iterator through each
                # simianFileOptionsDefault dictionary key:value pair
                simianTuples = simianFileOptionsDefault['simianFileOptionsDefault']\
                    .items()

                # unpack the tuple object; we are interested in simianKey,
                # and thus have no use for the original value, only unpacking
                # it to avoid errors
                (simianKey, originalValue) = simianTuples
                # set the value of True or False based on the checkbox
                checkstate.setChecked(originalValue)

            # since threshold is the only non-checkbox value, we can check it
            # independently and do not need to unpack the key:value pair here
            # as a tuple
            self.SimianThresholdNumber\
                .setValue(simianFileOptionsDefault['simianFileOptionsDefault']
                            .get('threshold'))

        simianFileOptionsSaved['simianFileOptionsSaved']\
            .update(simianFileOptionsDefault)['simianFileOptionsDefault']
        # TODO: reset the boolean checked states and values according to
        # the saved values in simianFileOptionsSaved or
        # simianFileOptionsDefault, whichever turns out to be easier
        yaml.safe_dump(simianFileOptionsSaved, stream=yamlFileSaved)

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
            if ErrorEvent is UnboundLocalError:
                self.errorWidget.ErrorText.setText(_translate("ErrorDialog",
                    "You either selected less than 2 files or more than 3 files. \
                        Please check your selected files in the Simian Table. "))
            else:
                self.errorWidget.ErrorText.setText(_translate("ErrorDialog", "An error has occurred. "))
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
