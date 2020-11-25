# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'setup.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
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

from qtFunctions import errorHandler
from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class Ui_ErrorDialog(object):
    def setupUi(self, ErrorDialog):
        ErrorDialog.setObjectName("ErrorDialog")
        ErrorDialog.resize(260, 100)
        self.ErrorText = QtWidgets.QLabel(ErrorDialog)
        self.ErrorText.setGeometry(QtCore.QRect(0, 0, 260, 50))
        self.ErrorText.setAlignment(QtCore.Qt.AlignCenter)
        self.ErrorText.setObjectName("ErrorText")
        self.buttonBox = QtWidgets.QDialogButtonBox(ErrorDialog)
        self.buttonBox.setGeometry(QtCore.QRect(10, 70, 156, 23))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.retranslateUi(ErrorDialog)
        QtCore.QMetaObject.connectSlotsByName(ErrorDialog)

    def retranslateUi(self, ErrorDialog):
        _translate = QtCore.QCoreApplication.translate
        ErrorDialog.setWindowTitle(_translate("ErrorDialog", "Dialog"))
        self.ErrorText.setText(_translate("ErrorDialog", "An error has occurred. "))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ErrorDialog = QtWidgets.QDialog()
    ui = Ui_ErrorDialog()
    ui.setupUi(ErrorDialog)
    ErrorDialog.show()
    sys.exit(app.exec_())
