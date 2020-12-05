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

from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import pyqtSlot, QStandardPaths
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
        self.dirPath = resource_path(("settings.ini"))

        # UI initialization; dynamic and based off of the correspoinding .ui
        # file, meaning changing the GUI in Qt Designer will result in an
        # immediate change to the file.
        uiPath = '/ui'
        super(Ui_SimianWindow, self).__init__()
        uic.loadUi('form.ui', self)

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
        newList = []

        # for the number of results on the selected items, append it to the end of the list
        for x in listOfResults:
            newList.append(x)

        file1 = newList[0]
        file2 = newList[1]

        newFile1 = file1.text()
        newFile2 = file2.text()
        # if the list of results is less than 3, set file3 to none
        if len(listOfResults) < 3:
            file3 = None
        else:
            file3 = newList[2]
            newFile3 = file3.text()

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
            pass
        # else if the list is empty due to no selections...
        elif not bool(newList):
            # raise IndexError("You must select items in the table.")
            if self.Ui_ErrorDialog is None:
                self.Ui_ErrorDialog = Ui_ErrorDialog()
            self.Ui_ErrorDialog.ErrorText\
                .setText("You must select items in the table.")
            self.Ui_ErrorDialog.show()
        # if there were less than 2 items selected, or more than 3 items..
        elif len(newList) > 2 or len(newList) < 3:
            # raise UnboundLocalError("You must select 2 or 3 items to compare or merge.")
            if self.Ui_ErrorDialog is None:
                self.Ui_ErrorDialog = Ui_ErrorDialog()
            self.Ui_ErrorDialog.ErrorText\
                .setText("You must select 2 or 3 items to compare or merge.")
            self.Ui_ErrorDialog.show()
            # call ErrorHandler with an UnboundLocalError()
            # globalFunctions.errorHandler(self, UnboundLocalError)
            pass
        else:
            # if the selected item list is composed of 2 items...
            if len(newList) == 2:

                # if the merge button is checked...
                if self.Kdiff3MergeButton.isChecked():

                    # if there is no supplied output file, assume a merger
                    if outputFile is None:
                        subprocess.run([kDiff3FileDir, newFile1, newFile2, '-m'])

                    # else, run kDiff3 with the output file being generated
                    else:
                        subprocess.run([kDiff3FileDir, newFile1, newFile2, '-o',
                                        outputFile])

                # if the merge button is not checked,
                # just do a compare operation
                else:
                    subprocess.run([kDiff3FileDir, newFile1, newFile2])

            # else, if the file list length is 3...
            elif len(newList) == 3:

                # check if the merge button is checked...
                if self.Kdiff3MergeButton.isChecked():

                    # if there is no outputFile, assume a merger...
                    if outputFile is None:
                        subprocess.run([kDiff3FileDir, newFile1, newFile2, newFile3,
                                        '-m'])

                    # else, run kDiff3 with the output file being generated
                    else:
                        subprocess.run([kDiff3FileDir, newFile1, newFile2, newFile3,
                                        '-o', outputFile])

                # if there is no merge button checked, just run a compare
                else:
                    subprocess.run([kDiff3FileDir, newFile1, newFile2, newFile3])

            # else, if an unknown error occurs...
            else:
                # raise RuntimeError() and tell them we don't know what happened
                if self.Ui_ErrorDialog is None:
                    self.Ui_ErrorDialog = Ui_ErrorDialog()
                self.Ui_ErrorDialog.ErrorText\
                    .setText("An unknown error has occurred.")
                self.Ui_ErrorDialog.show()
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
            self.FileDirectoryText.setText(text +'/*')

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
            combinedArgs.append(self.FileDirectoryText.text())

            # contentText stores the output gathered from
            # Simian.exe with combinedArgs, with the additional
            # parameters setting the file to save as a string
            # with utf-8 encoding
            try:
                contentText = \
                    subprocess.check_output(combinedArgs, text=True, encoding="utf-8", stderr=subprocess.STDOUT)
            except subprocess.CalledProcessError as e:
                raise RuntimeError("command '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output))
            else:
                # Split the text into multiple lines of
                stringList = contentText.split("\n")


                # if there are no results for duplicates from Simian...
                # NOTE: This outcome also occurs if the openedFileDir is
                # invalid. This behavior is native to Simian's processing.
                if 'Found 0 duplicate lines in 0 blocks in 0 files' \
                        in stringList:
                    # make an empty List out of foundResults
                    # that will be populated
                    foundResults = []
                    # end early, setting foundNumber to 0
                    foundNumber = 0
                    # insert a single column into the list
                    # foundResults.append(QTreeWidgetItem(None, QStringList(QString())))
                    foundResults.append("0 results.")

                    # If the table has results from a prior result
                    if self.ResultsTable.count() > 0:
                        # clear the table prematurely
                        self.ResultsTable.clear()

                    # add this item to the resultsTable
                    self.ResultsTable.addItems(foundResults)

                # else, if there are duplicates
                else:
                    # make an empty List out of foundResults
                    # that will be populated
                    foundResults = []
                    foundNumber = int()
                    # initialize a counter for the list in order to organize
                    # results
                    i = 0
                    # while we have not fully traversed the listOfResults..
                    while i < len(stringList):
                        # pop the current item
                        lineString = stringList.pop(i)
                        # increment i after the pop
                        i += 1
                        # If the line corresponds to a found line...
                        if 'in the following files:' in lineString:

                            # get the foundNumber by splitting and getting
                            # the value of the second object, which will
                            # always be the number
                            foundNumber = int(lineString.split(' ')[1])
                            # fingerprint = lineString.split(' ')[6]

                            # insert the number of found results into
                            # the current index
                            # foundResults.append(i, foundNumber)
                            lineString = stringList.pop(i)
                            i +=1

                        # else, if this line is stating the files that
                        # Simian is detecting duplicates between...
                        if 'Between lines' in lineString:
                            # parse the path by splitting by spaces,
                            # but critically stopping the split
                            # before we would hit the file name,
                            # where there could be spaces in the Directory
                            # which throw off results
                            foundFileName = lineString.split(' ', 7)[7]

                            # insert a nested result within the index
                            # of our foundNumber
                            foundResults.append(foundFileName + f'[{foundNumber}]')

                                # self.ResultsTable.addItem(lineString)

                    # when we have finished generating the list, sort
                    # with a helper method to sort by the highest number of
                    # results to the lowest results
                    # foundResults.sort(reverse=True, key=sortList(foundNumber))

                    # If the table has results from a prior result
                    if self.ResultsTable.count() > 0:
                        # clear the table prematurely
                        self.ResultsTable.clear()

                    # add this list entirely to the ResultsTable QListWidget
                    self.ResultsTable.addItems(foundResults)
                    self.ResultsTable.sortItems()


# sorter for the foundResults list in runSimian
def sortList(sorter):
    return sorter['foundNumber']


# Translate asset paths to useable format for PyInstaller
def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath('.'), relative_path)


def main():
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_SimianWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
