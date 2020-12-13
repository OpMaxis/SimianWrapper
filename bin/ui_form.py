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

from PyQt5 import QtCore, QtWidgets, uic
from PyQt5.QtCore import pyqtSlot
from TreeWidgetItem import TreeWidgetItem
from ui_setup import Ui_SimianSetup
from ui_error import Ui_ErrorDialog
import sys
import os
import subprocess
import configparser


class Ui_SimianWindow(QtWidgets.QMainWindow):
    # Constructor for the initialization of the GUI elements.
    def __init__(self):
        # initialize the secondary windows to SimianWindow as none
        self.Ui_SimianSetup = None
        self.Ui_ErrorDialog = None
        # initialize the file dialog to none
        self.dialog = None

        # set the dirpath which will be used by the file saving and restoring
        self.dirPath = "settings.ini"

        # UI initialization; dynamic and based off of the correspoinding .ui
        # file, meaning changing the GUI in Qt Designer will result in an
        # immediate change to the file.
        super(Ui_SimianWindow, self).__init__()
        uic.loadUi('./ui/form.ui', self)

        ''' The following code block imports all the event handlers with custom
        functions, or data that is required for custom event handling.'''

        # connects the FileDirectoryButton to browseDir method
        self.FileDirectoryButton = \
            self.findChild(QtWidgets.QToolButton, 'FileDirectoryButton')
        self.FileDirectoryButton.clicked.connect(self.browseDir)

        # connects the launch Button to runSimian method
        self.simianLaunchButton = \
            self.findChild(QtWidgets.QPushButton, 'simianLaunchButton')
        self.simianLaunchButton.clicked.connect(self.runSimian)

        # connect the simianSetup button to the openSetup method
        self.simianSetupButton = \
            self.findChild(QtWidgets.QPushButton, 'simianSetupButton')
        self.simianSetupButton.clicked.connect(self.openSetup)

        # connect the openKdiff3Button to the runKdiff3 method
        self.openKdiff3Button = \
            self.findChild(QtWidgets.QPushButton, 'openKdiff3Button')
        self.openKdiff3Button.clicked.connect(self.runKdiff3)

        # call the FileDirectoryText to be used by browseDir
        self.FileDirectoryText = \
            self.findChild(QtWidgets.QLineEdit, 'FileDirectoryText')
        # connects a text change event to the method to enforce suffixes
        self.FileDirectoryText.textChanged.connect(self.enforceLineEditSuffix)

        # call the Kdiff3OutputLine to be used by runKdiff3
        self.Kdiff3OutputLine = \
            self.findChild(QtWidgets.QLineEdit, 'Kdiff3OutputLine')

        # show the window
        self.show()

    # This code called when a file directory will be accessed
    @QtCore.pyqtSlot()
    def browseDir(self):
        # calls the dialog box to open with the existing directory
        self.dialog = str(QtWidgets.QFileDialog.getExistingDirectory(self))
        self.FileDirectoryText.setText(self.dialog)

    # -This code opens the setupUi widget from the form.ui
    @pyqtSlot()
    def openSetup(self):
        if self.Ui_SimianSetup is None:
            self.Ui_SimianSetup = Ui_SimianSetup()
        self.Ui_SimianSetup.show()

    # -This code runs Kdiff3 directly by using the directory.
    # If no directory is given, error message will be processed
    # Otherwise.
    @pyqtSlot()
    def runKdiff3(self):

        # create a file list from the selected items on the resultsTable
        listOfResults = self.ResultsTable.selectedItems()
        for item in listOfResults:
            if item.columnCount == 2:
                # Call the error handler
                if self.Ui_ErrorDialog is None:
                    self.Ui_ErrorDialog = Ui_ErrorDialog()
                self.Ui_ErrorDialog.ErrorText\
                    .setText("You have selected an item in an invalid column.")
                self.Ui_ErrorDialog.show()

        # set a list of three items from the selected items
        # file1 = str()
        # file2 = str()
        # file3 = str()
        # for i in range(len(listOfResults)):
        #     if not str(os.path.exists(listOfResults[i].text)):
        #         if self.Ui_ErrorDialog is None:
        #             self.Ui_ErrorDialog = Ui_ErrorDialog()
        #         self.Ui_ErrorDialog.ErrorText\
        #             .setText("You must select valid file paths.")
        #         self.Ui_ErrorDialog.show()

        # call a read_config object to read from file
        read_config = configparser.ConfigParser()
        # read according to the assigned dirPath
        read_config.read(self.dirPath)

        # kDiff3FileDir is called read_config with the option corresponding
        # to the result
        kDiff3FileDir = read_config.get("fileDirsSaved", "kDiff3WorkFileDir")

        # compareFile is the QLineEdit text from the kDiff3 File Options
        outputFile = self.Kdiff3OutputLine.text()

        # ifKdiff3FileDir is not set, or there are no selected items
        # in the list...
        if kDiff3FileDir is None:
            # raise FileNotFoundError("Your Kdiff3 Working File directory is invalid.")
            # Call the error handler
            if self.Ui_ErrorDialog is None:
                self.Ui_ErrorDialog = Ui_ErrorDialog()
            self.Ui_ErrorDialog.ErrorText\
                .setText("Your Kdiff3 Working File directory is invalid.")
            self.Ui_ErrorDialog.show()
        # else if the list is empty due to no selections...
        elif not bool(listOfResults):
            # raise IndexError("You must select items in the table.")
            if self.Ui_ErrorDialog is None:
                self.Ui_ErrorDialog = Ui_ErrorDialog()
            self.Ui_ErrorDialog.ErrorText\
                .setText("You must select items in the table.")
            self.Ui_ErrorDialog.show()
        # if there were less than 2 items selected, or more than 3 items..
        # elif len(listOfResults) != 2 or len(listOfResults) != 3:
        # #     # raise UnboundLocalError("You must select 2 or 3 items to compare or merge.")
        #     if self.Ui_ErrorDialog is None:
        #         self.Ui_ErrorDialog = Ui_ErrorDialog()
        #     self.Ui_ErrorDialog.ErrorText\
        #         .setText("You must select 2 or 3 items to compare or merge.")
        #     self.Ui_ErrorDialog.show()
            # call ErrorHandler with an UnboundLocalError()
            # globalFunctions.errorHandler(self, UnboundLocalError)
        # if the length of the list of results is between the acceptable range...
        else:
            # if the selected item list is composed of 2 items...
            if len(listOfResults) == 2:

                # # set a list of two items from the selected items
                file1 = listOfResults[0].text(0)
                file2 = listOfResults[1].text(0)

                if not os.path.isfile(file1) or \
                        not os.path.isfile(file2):
                    if self.Ui_ErrorDialog is None:
                        self.Ui_ErrorDialog = Ui_ErrorDialog()
                    self.Ui_ErrorDialog.ErrorText\
                        .setText("You must select valid files.")
                    self.Ui_ErrorDialog.show()
                # if the merge button is checked...
                elif self.Kdiff3MergeButton.isChecked():

                    # if there is no supplied output file, assume a merger
                    if outputFile is None:
                        subprocess.run([kDiff3FileDir, file1, file2, '-m'])

                    # else, run kDiff3 with the output file being generated
                    else:
                        subprocess.run([kDiff3FileDir, file1, file2, '-o',
                                        outputFile])

                # if the merge button is not checked,
                # just do a compare operation
                elif not self.Kdiff3MergeButton.isChecked():
                    subprocess.run([kDiff3FileDir, file1, file2])

            # else, if the file list length is 3...
            elif len(listOfResults) == 3:
                file1 = listOfResults[0].text(0)
                file2 = listOfResults[1].text(0)
                file3 = listOfResults[2].text(0)

                if not os.path.isfile(file1) or not os.path.isfile(file2) or not os.path.isfile(file3):
                    if self.Ui_ErrorDialog is None:
                        self.Ui_ErrorDialog = Ui_ErrorDialog()
                    self.Ui_ErrorDialog.ErrorText\
                        .setText("You must select valid files.")
                    self.Ui_ErrorDialog.show()


                # check if the merge button is checked...
                elif self.Kdiff3MergeButton.isChecked():

                    # if there is no outputFile, assume a merger...
                    if outputFile is None:
                        subprocess.run([kDiff3FileDir, file1, file2, file3,
                                        '-m'])

                    # else, run kDiff3 with the output file being generated
                    else:
                        subprocess.run([kDiff3FileDir, file1, file2, file3,
                                        '-o', outputFile])

                # if there is no merge button checked, just run a compare
                elif not self.Kdiff3MergeButton.isChecked():
                    subprocess.run([kDiff3FileDir, file1, file2, file3])

        # # else, if an unknown error occurs...
        # else:
        #     # raise RuntimeError() and tell them we don't know what happened
        #     if self.Ui_ErrorDialog is None:
        #         self.Ui_ErrorDialog = Ui_ErrorDialog()
        #     self.Ui_ErrorDialog.ErrorText\
        #         .setText("An unknown error has occurred.")
        #     self.Ui_ErrorDialog.show()
            # errorHandler(self, RuntimeError)

    # This method forces the postfix of /* onto the file to satisfy the
    # demands of subprocess's arguments
    @pyqtSlot()
    def enforceLineEditSuffix(self):
        # get the current text
        text = self.FileDirectoryText.text()

        # if that text doesn't end with the asterisks
        if not text.endswith('/*'):

            # block other signals from accessing FileDirectoryText
            self.FileDirectoryText.blockSignals(True)
            # modify the text to have the original text, plus the asterisks
            self.FileDirectoryText.setText(text + '/*')

            # allow it to be edited by other signals again
            self.FileDirectoryText.blockSignals(False)

    # -This code runs Simian by calling the CLI arguments and using
    # simianFileDir for the directory that was is listed.
    # If no directory is given, error message will be processed
    # -The second effect will be producing the results by reading the CLI lines
    # directly from prompt
    @pyqtSlot()
    def runSimian(self):
        # Initialize combinedArgs as an empty list, which will be populated
        # later
        combinedArgs = list()

        # call a read_config object to read from file
        read_config = configparser.ConfigParser()
        # read according to the assigned dirPath
        read_config.read(self.dirPath)

        # simianWorkFileDir is called read_config with the option corresponding
        # to the result
        simianWorkFileDir = read_config.get("fileDirsSaved", "simianWorkFileDir")

        # If the workfileDirectory has not been defined yet, end early
        if simianWorkFileDir is None:
            # raise FileNotFoundError('Your directory for Simian is invalid. Please check your setup options.')
            if self.Ui_ErrorDialog is None:
                self.Ui_ErrorDialog = Ui_ErrorDialog()
            self.Ui_ErrorDialog.ErrorText\
                .setText('Your directory for Simian is invalid. Please check your setup options.')
            self.Ui_ErrorDialog.show()
        # Otherwise, continue onwards
        else:

            # insert the simianWorkFileDir, which will be the
            # executing process where simian.exe will be located
            combinedArgs.insert(0, simianWorkFileDir)
            # put the openedFileDir at the end of the argument list
            combinedArgs.append('-failOnDuplication-')
            # combinedArgs.append()
            combinedArgs.append(self.FileDirectoryText.text())

            # contentText stores the output gathered from
            # Simian.exe with combinedArgs, with the additional
            # parameters setting the file to save as a string
            # with utf-8 encoding
            contentText = \
                subprocess.check_output(combinedArgs, text=True, encoding="utf-8", stderr=subprocess.STDOUT)
            # Split the text into multiple lines of
            stringList = contentText.splitlines()

            # if there are no results for duplicates from Simian...
            # NOTE: This outcome also occurs if the openedFileDir is
            # invalid. This behavior is native to Simian's processing.
            if 'Found 0 duplicate lines in 0 blocks in 0 files' \
                    in stringList:
                # make an empty dict out of foundResults
                # that will be populated
                foundResults = dict()
                # end early, setting foundNumber to 0
                foundNumber = 0
                # insert a single column into the list
                # foundResults.append(QTreeWidgetItem(None, QStringList(QString())))
                foundResults.update({"Number of Results": 0})

                # clear the table prematurely
                self.ResultsTable.clear()

                # add this item to the resultsTable
                fillWidget(self.ResultsTable, foundResults)

            # else, if there are duplicates
            else:
                # make an empty dict out of foundResults
                # that will be populated
                foundResults = dict()

                # for a full iteration through all strings from the output
                for x in range(len(stringList)):

                    # iterate through each lineString as an individual line
                    lineString = stringList[x]

                    # If the line corresponds to a found line...
                    if 'in the following files:' in lineString:

                        # get the foundNumber by splitting and getting
                        # the value of the second object, which will
                        # always be the number
                        foundNumber = int(lineString.split(' ')[1])

                        # fingerprint splits at the seventh string, where it
                        # always will be present
                        fingerprint = lineString.split(' ')[6]

                        # Add the fingerprint and number into the dictionary
                        # at the base, foundNumber as a list which holds a set.
                        # that set holds our foundFileNames
                        # (a set so that duplicate results are ignored)
                        foundResults[fingerprint] = (foundNumber, set())

                    # if this line is stating the files that
                    # Simian is detecting duplicates between...
                    if 'Between lines' in lineString:

                        # parse the path by splitting by spaces,
                        # but critically stopping the split
                        # before we would hit the file name,
                        # where there could be spaces in the Directory
                        # which throw off results
                        foundFileName = lineString.split(' ', 7)[7]

                        # insert a nested result within the set
                        # of our foundNumber,
                        # which will always be the second number
                        foundResults[fingerprint][1].add(foundFileName)

                # clear the widget before loading new results
                self.ResultsTable.clear()

                # sort the widget by the second column, in descending order
                self.ResultsTable.sortItems(1, 1)

                # add this list entirely to the ResultsTable QListWidget
                fillWidget(self.ResultsTable, foundResults)


# sorter for the foundResults list in runSimian
def sortList(sorter):
    return sorter['foundNumber']

# CUT errorHandler; did not function  as expected when called in replacement of the
# def errorHandler(self, argument):
#     if self.Ui_ErrorDialog is None:
#         self.Ui_ErrorDialog = Ui_ErrorDialog()
#     switcher = {
#         1: self.Ui_ErrorDialog.ErrorText
#         .setText("Your Kdiff3 Working File directory is invalid."),
#         2: self.Ui_ErrorDialog.ErrorText
#         .setText("You must select items in the table."),
#         3: self.Ui_ErrorDialog.errorText
#         .setText("You must select 2 or 3 items to compare or merge."),
#         4: self.Ui_ErrorDialog.errorText
#         .setText("You have selected an invalid set of values to open in Kdiff3."),
#         5: self.Ui_ErrorDialog.ErrorText\
#         .setText('Your directory for Simian is invalid. Please check your setup options.'),
#     }
#     switcher.get(argument,
#         self.Ui_ErrorDialog.ErrorText.setText("An unknown error occurred."))
#     self.Ui.ErrorDialog.show()


# This method is used in runSimian to generate results from the gathered dictionary
def fillTreeItems(item, value):
    # it = QtWidgets.QTreeWidgetItemIterator(value,
    #             flags=QtWidgets.QTreeWidgetItemIterator.HasChildren)
    # it2 = QtWidgets.QTreeWidgetItemIterator(value)

    def newItem(parent, key, val):
        # create a custom TreeWidgetItem with integer/float sorting
        child = TreeWidgetItem()

        # if the passed in value is a dictionary object...
        if isinstance(value, dict):

            # set the child TreeWidgetItem first column to the fingerprint key
            child.setText(0, key)

            # set the child TreeWidgetItem second column to the number of dupes
            child.setText(1, str(val[0]))

        # if the passed in sequence is a tuple...
        if isinstance(value, tuple):
            # recursive call to go through the nested values of the dictionary
            # fillTreeItems(child, val)
            # traverse deeper into the list's second item, the set

            # # if the passed in sequence is a set...
            # if isinstance(value, set):
            # for each value in the set...
            # set the text to each item from the set
            pass
        if isinstance(value, set):
            child.setText(0, key)
        # add the child to the parent QTreeWidget
        # if isinstance(value, :

        parent.addChild(child)
        # automatically expand the column
        child.setExpanded(True)

        # recursive call to go through the nested values of the dictionary
        fillTreeItems(child, val)

    # recursion escape clause, terminates the recursion
    # if there are no more items
    if value is None:
        return
    # else, if the initial passed in value is a dictionary ...
    elif isinstance(value, dict):

        # for each key - value pair in the dictionary
        for key, val in value.items():

            # call the newItem initialization method (not recursion)
            newItem(item, str(key), val)

    # else if the value is another sequence object from Python's library...
    elif isinstance(value, (list, tuple, set)):
        # for each value in the sequence...
        for val in value:
            # set the key to the string value if it is not a Python object
            # else, set it to the string formatted name value
            key = (str(val) if not isinstance(val, (dict, list, tuple, set))
                    else '[%s]' % type(val).__name__)

            # call the newItem initialization method (not recursion)
            newItem(item, key, val)
    # # if the value is neither, run the value through as a raw string
    # else:
    #     newItem(item, str(value))

# This method calls the save function from configparser to save the loaded file
# as the window closes
def saveOnExit(self, event):
        # call a write_config to open a ConfigParser object
        write_config = configparser.ConfigParser()
        # add a section corresponding to our FileDirsSaved section
        write_config.add_section('fileDirsSaved')
        # set the corresponding dir to the text in the QLineEdit boxes
        write_config.set("fileDirsSaved", "pickedfile", self.FileDirectoryText.text())
        # open the iniFile...
        with open((self.dirPath), mode='w') as iniFile:
            # write the directories to file, then close it
            write_config.write(iniFile)
        #
        super(Ui_SimianWindow, self).saveOnExit(event)



# This method is used as a helper method to launch fillTreeItems(item, sequence)
def fillWidget(widget, value):
    # calls tree items at the baseline
    fillTreeItems(widget.invisibleRootItem(), value)



def main():
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_SimianWindow()
    saveOnExit(self.FileDirectoryText, sys.exit(app.exec_()))


if __name__ == '__main__':
    main()
