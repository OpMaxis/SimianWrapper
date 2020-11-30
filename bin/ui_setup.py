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


from PyQt5 import QtCore, QtGui, QtWidgets
from qtFunctions import browseDir, saveSettings, resetDefaults
import sys


class Ui_SimianSetup(QtCore.QObject):

    def main():
        def setupUi(self, SimianSetup):
            SimianSetup.setObjectName("SimianSetup")
            SimianSetup.resize(980, 430)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(SimianSetup.sizePolicy().hasHeightForWidth())
            SimianSetup.setSizePolicy(sizePolicy)
            self.SimianSetupWidget = QtWidgets.QWidget(SimianSetup)
            self.SimianSetupWidget.setObjectName("SimianSetupWidget")
            self.gridLayout = QtWidgets.QGridLayout(self.SimianSetupWidget)
            self.gridLayout.setObjectName("gridLayout")
            self.DirToSimianLine = QtWidgets.QFrame(self.SimianSetupWidget)
            self.DirToSimianLine.setFrameShape(QtWidgets.QFrame.HLine)
            self.DirToSimianLine.setFrameShadow(QtWidgets.QFrame.Sunken)
            self.DirToSimianLine.setObjectName("DirToSimianLine")
            self.gridLayout.addWidget(self.DirToSimianLine, 2, 0, 1, 5)
            self.SimianThresholdLabel = QtWidgets.QLabel(self.SimianSetupWidget)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.SimianThresholdLabel.sizePolicy().hasHeightForWidth())
            self.SimianThresholdLabel.setSizePolicy(sizePolicy)
            self.SimianThresholdLabel.setObjectName("SimianThresholdLabel")
            self.gridLayout.addWidget(self.SimianThresholdLabel, 4, 2, 1, 1)
            self.SimianThresholdNumber = QtWidgets.QSpinBox(self.SimianSetupWidget)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.SimianThresholdNumber.sizePolicy().hasHeightForWidth())
            self.SimianThresholdNumber.setSizePolicy(sizePolicy)
            self.SimianThresholdNumber.setMinimum(2)
            self.SimianThresholdNumber.setObjectName("SimianThresholdNumber")
            self.gridLayout.addWidget(self.SimianThresholdNumber, 4, 3, 1, 1)
            self.OptionsBox = QtWidgets.QDialogButtonBox(self.SimianSetupWidget)
            self.OptionsBox.setOrientation(QtCore.Qt.Horizontal)
            self.OptionsBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close|QtWidgets.QDialogButtonBox.RestoreDefaults|QtWidgets.QDialogButtonBox.Save)
            self.OptionsBox.setCenterButtons(True)
            self.OptionsBox.setObjectName("OptionsBox")
            self.gridLayout.addWidget(self.OptionsBox, 5, 0, 1, 5)
            self.Kdiff3FileDirLabel = QtWidgets.QLabel(self.SimianSetupWidget)
            font = QtGui.QFont()
            font.setPointSize(12)
            font.setBold(False)
            font.setWeight(50)
            self.Kdiff3FileDirLabel.setFont(font)
            self.Kdiff3FileDirLabel.setObjectName("Kdiff3FileDirLabel")
            self.gridLayout.addWidget(self.Kdiff3FileDirLabel, 1, 0, 1, 2)
            self.SimianFileOptions = QtWidgets.QLabel(self.SimianSetupWidget)
            self.SimianFileOptions.setEnabled(True)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.SimianFileOptions.sizePolicy().hasHeightForWidth())
            self.SimianFileOptions.setSizePolicy(sizePolicy)
            font = QtGui.QFont()
            font.setPointSize(12)
            font.setBold(False)
            font.setWeight(50)
            self.SimianFileOptions.setFont(font)
            self.SimianFileOptions.setAlignment(QtCore.Qt.AlignCenter)
            self.SimianFileOptions.setObjectName("SimianFileOptions")
            self.gridLayout.addWidget(self.SimianFileOptions, 3, 0, 2, 2)
            self.Kdiff3SetupLayout = QtWidgets.QHBoxLayout()
            self.Kdiff3SetupLayout.setObjectName("Kdiff3SetupLayout")
            self.Kdiff3FileDirLine = QtWidgets.QLineEdit(self.SimianSetupWidget)
            self.Kdiff3FileDirLine.setEnabled(True)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.Kdiff3FileDirLine.sizePolicy().hasHeightForWidth())
            self.Kdiff3FileDirLine.setSizePolicy(sizePolicy)
            self.Kdiff3FileDirLine.setMaxLength(32767)
            self.Kdiff3FileDirLine.setObjectName("Kdiff3FileDirLine")
            self.Kdiff3SetupLayout.addWidget(self.Kdiff3FileDirLine)
            self.Kdiff3FileDirButton = QtWidgets.QPushButton(self.SimianSetupWidget)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.Kdiff3FileDirButton.sizePolicy().hasHeightForWidth())
            self.Kdiff3FileDirButton.setSizePolicy(sizePolicy)
            self.Kdiff3FileDirButton.setObjectName("Kdiff3FileDirButton")
            self.Kdiff3SetupLayout.addWidget(self.Kdiff3FileDirButton)
            self.gridLayout.addLayout(self.Kdiff3SetupLayout, 1, 2, 1, 3)
            self.simianFileDirLayout = QtWidgets.QHBoxLayout()
            self.simianFileDirLayout.setObjectName("simianFileDirLayout")
            self.simianFileDirLine = QtWidgets.QLineEdit(self.SimianSetupWidget)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.simianFileDirLine.sizePolicy().hasHeightForWidth())
            self.simianFileDirLine.setSizePolicy(sizePolicy)
            self.simianFileDirLine.setObjectName("simianFileDirLine")
            self.simianFileDirLayout.addWidget(self.simianFileDirLine)
            self.simianFileDirButton = QtWidgets.QPushButton(self.SimianSetupWidget)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.simianFileDirButton.sizePolicy().hasHeightForWidth())
            self.simianFileDirButton.setSizePolicy(sizePolicy)
            self.simianFileDirButton.setObjectName("simianFileDirButton")
            self.simianFileDirLayout.addWidget(self.simianFileDirButton)
            self.gridLayout.addLayout(self.simianFileDirLayout, 0, 2, 1, 3)
            self.simianFileDirLabel = QtWidgets.QLabel(self.SimianSetupWidget)
            font = QtGui.QFont()
            font.setPointSize(12)
            font.setBold(False)
            font.setUnderline(False)
            font.setWeight(50)
            font.setStrikeOut(False)
            font.setKerning(True)
            self.simianFileDirLabel.setFont(font)
            self.simianFileDirLabel.setObjectName("simianFileDirLabel")
            self.gridLayout.addWidget(self.simianFileDirLabel, 0, 0, 1, 2)
            self.SimianFileOptLayout = QtWidgets.QSplitter(self.SimianSetupWidget)
            self.SimianFileOptLayout.setOrientation(QtCore.Qt.Vertical)
            self.SimianFileOptLayout.setObjectName("SimianFileOptLayout")
            self.layoutWidget_2 = QtWidgets.QWidget(self.SimianFileOptLayout)
            self.layoutWidget_2.setObjectName("layoutWidget_2")
            self.SimianFileOptTop = QtWidgets.QHBoxLayout(self.layoutWidget_2)
            self.SimianFileOptTop.setContentsMargins(0, 0, 0, 0)
            self.SimianFileOptTop.setSpacing(0)
            self.SimianFileOptTop.setObjectName("SimianFileOptTop")
            self.line_3 = QtWidgets.QFrame(self.layoutWidget_2)
            self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
            self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
            self.line_3.setObjectName("line_3")
            self.SimianFileOptTop.addWidget(self.line_3)
            self.BalanceParentheses = QtWidgets.QCheckBox(self.layoutWidget_2)
            self.BalanceParentheses.setMinimumSize(QtCore.QSize(145, 0))
            self.BalanceParentheses.setChecked(False)
            self.BalanceParentheses.setObjectName("BalanceParentheses")
            self.SimianFileOptTop.addWidget(self.BalanceParentheses)
            self.line_14 = QtWidgets.QFrame(self.layoutWidget_2)
            self.line_14.setFrameShape(QtWidgets.QFrame.VLine)
            self.line_14.setFrameShadow(QtWidgets.QFrame.Sunken)
            self.line_14.setObjectName("line_14")
            self.SimianFileOptTop.addWidget(self.line_14)
            self.BalanceSquareBrackets = QtWidgets.QCheckBox(self.layoutWidget_2)
            self.BalanceSquareBrackets.setMinimumSize(QtCore.QSize(145, 0))
            self.BalanceSquareBrackets.setChecked(False)
            self.BalanceSquareBrackets.setObjectName("BalanceSquareBrackets")
            self.SimianFileOptTop.addWidget(self.BalanceSquareBrackets)
            self.line_2 = QtWidgets.QFrame(self.layoutWidget_2)
            self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
            self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
            self.line_2.setObjectName("line_2")
            self.SimianFileOptTop.addWidget(self.line_2)
            self.FailOnDupl = QtWidgets.QCheckBox(self.layoutWidget_2)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.FailOnDupl.sizePolicy().hasHeightForWidth())
            self.FailOnDupl.setSizePolicy(sizePolicy)
            self.FailOnDupl.setMinimumSize(QtCore.QSize(145, 0))
            self.FailOnDupl.setChecked(True)
            self.FailOnDupl.setObjectName("FailOnDupl")
            self.SimianFileOptTop.addWidget(self.FailOnDupl)
            self.line_9 = QtWidgets.QFrame(self.layoutWidget_2)
            self.line_9.setFrameShape(QtWidgets.QFrame.VLine)
            self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
            self.line_9.setObjectName("line_9")
            self.SimianFileOptTop.addWidget(self.line_9)
            self.IgnoreCharacters = QtWidgets.QCheckBox(self.layoutWidget_2)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.IgnoreCharacters.sizePolicy().hasHeightForWidth())
            self.IgnoreCharacters.setSizePolicy(sizePolicy)
            self.IgnoreCharacters.setMinimumSize(QtCore.QSize(145, 0))
            self.IgnoreCharacters.setChecked(False)
            self.IgnoreCharacters.setObjectName("IgnoreCharacters")
            self.SimianFileOptTop.addWidget(self.IgnoreCharacters)
            self.line_5 = QtWidgets.QFrame(self.layoutWidget_2)
            self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
            self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
            self.line_5.setObjectName("line_5")
            self.SimianFileOptTop.addWidget(self.line_5)
            self.IgnoreCharacterCase = QtWidgets.QCheckBox(self.layoutWidget_2)
            self.IgnoreCharacterCase.setMinimumSize(QtCore.QSize(145, 0))
            self.IgnoreCharacterCase.setChecked(True)
            self.IgnoreCharacterCase.setObjectName("IgnoreCharacterCase")
            self.SimianFileOptTop.addWidget(self.IgnoreCharacterCase)
            self.layoutWidget_3 = QtWidgets.QWidget(self.SimianFileOptLayout)
            self.layoutWidget_3.setObjectName("layoutWidget_3")
            self.SimianFileOptMid = QtWidgets.QHBoxLayout(self.layoutWidget_3)
            self.SimianFileOptMid.setContentsMargins(0, 0, 0, 0)
            self.SimianFileOptMid.setSpacing(0)
            self.SimianFileOptMid.setObjectName("SimianFileOptMid")
            self.line_17 = QtWidgets.QFrame(self.layoutWidget_3)
            self.line_17.setFrameShape(QtWidgets.QFrame.VLine)
            self.line_17.setFrameShadow(QtWidgets.QFrame.Sunken)
            self.line_17.setObjectName("line_17")
            self.SimianFileOptMid.addWidget(self.line_17)
            self.IgnoreCurlyBraces = QtWidgets.QCheckBox(self.layoutWidget_3)
            self.IgnoreCurlyBraces.setMinimumSize(QtCore.QSize(145, 0))
            self.IgnoreCurlyBraces.setChecked(False)
            self.IgnoreCurlyBraces.setObjectName("IgnoreCurlyBraces")
            self.SimianFileOptMid.addWidget(self.IgnoreCurlyBraces)
            self.line_7 = QtWidgets.QFrame(self.layoutWidget_3)
            self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
            self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
            self.line_7.setObjectName("line_7")
            self.SimianFileOptMid.addWidget(self.line_7)
            self.IgnoreIdent = QtWidgets.QCheckBox(self.layoutWidget_3)
            self.IgnoreIdent.setMinimumSize(QtCore.QSize(145, 0))
            self.IgnoreIdent.setChecked(False)
            self.IgnoreIdent.setObjectName("IgnoreIdent")
            self.SimianFileOptMid.addWidget(self.IgnoreIdent)
            self.line_6 = QtWidgets.QFrame(self.layoutWidget_3)
            self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
            self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
            self.line_6.setObjectName("line_6")
            self.SimianFileOptMid.addWidget(self.line_6)
            self.IgnoreIdentCase = QtWidgets.QCheckBox(self.layoutWidget_3)
            self.IgnoreIdentCase.setMinimumSize(QtCore.QSize(145, 0))
            self.IgnoreIdentCase.setChecked(True)
            self.IgnoreIdentCase.setObjectName("IgnoreIdentCase")
            self.SimianFileOptMid.addWidget(self.IgnoreIdentCase)
            self.line_12 = QtWidgets.QFrame(self.layoutWidget_3)
            self.line_12.setFrameShape(QtWidgets.QFrame.VLine)
            self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
            self.line_12.setObjectName("line_12")
            self.SimianFileOptMid.addWidget(self.line_12)
            self.IgnoreLiterals = QtWidgets.QCheckBox(self.layoutWidget_3)
            self.IgnoreLiterals.setMinimumSize(QtCore.QSize(145, 0))
            self.IgnoreLiterals.setChecked(False)
            self.IgnoreLiterals.setObjectName("IgnoreLiterals")
            self.SimianFileOptMid.addWidget(self.IgnoreLiterals)
            self.line_10 = QtWidgets.QFrame(self.layoutWidget_3)
            self.line_10.setFrameShape(QtWidgets.QFrame.VLine)
            self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
            self.line_10.setObjectName("line_10")
            self.SimianFileOptMid.addWidget(self.line_10)
            self.IgnoreNumbers = QtWidgets.QCheckBox(self.layoutWidget_3)
            self.IgnoreNumbers.setMinimumSize(QtCore.QSize(145, 0))
            self.IgnoreNumbers.setChecked(False)
            self.IgnoreNumbers.setObjectName("IgnoreNumbers")
            self.SimianFileOptMid.addWidget(self.IgnoreNumbers)
            self.layoutWidget_4 = QtWidgets.QWidget(self.SimianFileOptLayout)
            self.layoutWidget_4.setObjectName("layoutWidget_4")
            self.SimianFileOptBot = QtWidgets.QHBoxLayout(self.layoutWidget_4)
            self.SimianFileOptBot.setContentsMargins(0, 0, 0, 0)
            self.SimianFileOptBot.setSpacing(0)
            self.SimianFileOptBot.setObjectName("SimianFileOptBot")
            self.line_18 = QtWidgets.QFrame(self.layoutWidget_4)
            self.line_18.setFrameShape(QtWidgets.QFrame.VLine)
            self.line_18.setFrameShadow(QtWidgets.QFrame.Sunken)
            self.line_18.setObjectName("line_18")
            self.SimianFileOptBot.addWidget(self.line_18)
            self.IgnoreStringCase = QtWidgets.QCheckBox(self.layoutWidget_4)
            self.IgnoreStringCase.setMinimumSize(QtCore.QSize(145, 0))
            self.IgnoreStringCase.setChecked(True)
            self.IgnoreStringCase.setObjectName("IgnoreStringCase")
            self.SimianFileOptBot.addWidget(self.IgnoreStringCase)
            self.line_11 = QtWidgets.QFrame(self.layoutWidget_4)
            self.line_11.setFrameShape(QtWidgets.QFrame.VLine)
            self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
            self.line_11.setObjectName("line_11")
            self.SimianFileOptBot.addWidget(self.line_11)
            self.IgnoreStrings = QtWidgets.QCheckBox(self.layoutWidget_4)
            self.IgnoreStrings.setMinimumSize(QtCore.QSize(145, 0))
            self.IgnoreStrings.setChecked(False)
            self.IgnoreStrings.setObjectName("IgnoreStrings")
            self.SimianFileOptBot.addWidget(self.IgnoreStrings)
            self.line_15 = QtWidgets.QFrame(self.layoutWidget_4)
            self.line_15.setFrameShape(QtWidgets.QFrame.VLine)
            self.line_15.setFrameShadow(QtWidgets.QFrame.Sunken)
            self.line_15.setObjectName("line_15")
            self.SimianFileOptBot.addWidget(self.line_15)
            self.IgnoreSubtypeNames = QtWidgets.QCheckBox(self.layoutWidget_4)
            self.IgnoreSubtypeNames.setMinimumSize(QtCore.QSize(145, 0))
            self.IgnoreSubtypeNames.setChecked(False)
            self.IgnoreSubtypeNames.setObjectName("IgnoreSubtypeNames")
            self.SimianFileOptBot.addWidget(self.IgnoreSubtypeNames)
            self.line_8 = QtWidgets.QFrame(self.layoutWidget_4)
            self.line_8.setFrameShape(QtWidgets.QFrame.VLine)
            self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
            self.line_8.setObjectName("line_8")
            self.SimianFileOptBot.addWidget(self.line_8)
            self.IgnoreModifiers = QtWidgets.QCheckBox(self.layoutWidget_4)
            self.IgnoreModifiers.setMinimumSize(QtCore.QSize(145, 0))
            self.IgnoreModifiers.setChecked(True)
            self.IgnoreModifiers.setObjectName("IgnoreModifiers")
            self.SimianFileOptBot.addWidget(self.IgnoreModifiers)
            self.line_13 = QtWidgets.QFrame(self.layoutWidget_4)
            self.line_13.setFrameShape(QtWidgets.QFrame.VLine)
            self.line_13.setFrameShadow(QtWidgets.QFrame.Sunken)
            self.line_13.setObjectName("line_13")
            self.SimianFileOptBot.addWidget(self.line_13)
            self.IgnoreVariableNames = QtWidgets.QCheckBox(self.layoutWidget_4)
            self.IgnoreVariableNames.setMinimumSize(QtCore.QSize(145, 0))
            self.IgnoreVariableNames.setChecked(False)
            self.IgnoreVariableNames.setObjectName("IgnoreVariableNames")
            self.SimianFileOptBot.addWidget(self.IgnoreVariableNames)
            self.gridLayout.addWidget(self.SimianFileOptLayout, 3, 2, 1, 3)
            SimianSetup.setCentralWidget(self.SimianSetupWidget)
            self.statusbar = QtWidgets.QStatusBar(SimianSetup)
            self.statusbar.setObjectName("statusbar")
            SimianSetup.setStatusBar(self.statusbar)
            self.SimianThresholdLabel.setBuddy(self.SimianThresholdNumber)
            self.Kdiff3FileDirLabel.setBuddy(self.Kdiff3FileDirLine)
            self.simianFileDirLabel.setBuddy(self.simianFileDirLine)

            self.retranslateUi(SimianSetup)
            self.simianFileDirButton.clicked.connect(SimianSetup.browseDir)
            self.Kdiff3FileDirButton.clicked.connect(SimianSetup.browseDir)
            self.OptionsBox.clicked['QAbstractButton*'].connect(SimianSetup.saveSettings)
            self.OptionsBox.clicked['QAbstractButton*'].connect(SimianSetup.close)
            self.OptionsBox.clicked['QAbstractButton*'].connect(SimianSetup.resetDefaults)
            QtCore.QMetaObject.connectSlotsByName(SimianSetup)
            SimianSetup.setTabOrder(self.simianFileDirLine, self.simianFileDirButton)
            SimianSetup.setTabOrder(self.simianFileDirButton, self.Kdiff3FileDirLine)
            SimianSetup.setTabOrder(self.Kdiff3FileDirLine, self.Kdiff3FileDirButton)
            SimianSetup.setTabOrder(self.Kdiff3FileDirButton, self.BalanceParentheses)
            SimianSetup.setTabOrder(self.BalanceParentheses, self.BalanceSquareBrackets)
            SimianSetup.setTabOrder(self.BalanceSquareBrackets, self.FailOnDupl)
            SimianSetup.setTabOrder(self.FailOnDupl, self.IgnoreCharacters)
            SimianSetup.setTabOrder(self.IgnoreCharacters, self.IgnoreCharacterCase)
            SimianSetup.setTabOrder(self.IgnoreCharacterCase, self.IgnoreCurlyBraces)
            SimianSetup.setTabOrder(self.IgnoreCurlyBraces, self.IgnoreIdent)
            SimianSetup.setTabOrder(self.IgnoreIdent, self.IgnoreIdentCase)
            SimianSetup.setTabOrder(self.IgnoreIdentCase, self.IgnoreLiterals)
            SimianSetup.setTabOrder(self.IgnoreLiterals, self.IgnoreNumbers)
            SimianSetup.setTabOrder(self.IgnoreNumbers, self.IgnoreStringCase)
            SimianSetup.setTabOrder(self.IgnoreStringCase, self.IgnoreStrings)
            SimianSetup.setTabOrder(self.IgnoreStrings, self.IgnoreSubtypeNames)
            SimianSetup.setTabOrder(self.IgnoreSubtypeNames, self.IgnoreModifiers)
            SimianSetup.setTabOrder(self.IgnoreModifiers, self.IgnoreVariableNames)
            SimianSetup.setTabOrder(self.IgnoreVariableNames, self.SimianThresholdNumber)

        def retranslateUi(self, SimianSetup):
            _translate = QtCore.QCoreApplication.translate
            SimianSetup.setWindowTitle(_translate("SimianSetup", "SimianWrapper Setup"))
            self.SimianThresholdLabel.setToolTip(_translate("SimianSetup", "<html><head/><body><p>Matches will contain at least the specified number of lines. Must be at least 2.</p></body></html>"))
            self.SimianThresholdLabel.setText(_translate("SimianSetup", "Threshold"))
            self.Kdiff3FileDirLabel.setToolTip(_translate("SimianSetup", "<html><head/><body><p>Select a file within the directory to compare results from (optional).</p></body></html>"))
            self.Kdiff3FileDirLabel.setText(_translate("SimianSetup", "Kdiff3 Working File Directory"))
            self.SimianFileOptions.setToolTip(_translate("SimianSetup", "<html><head/><body><p>Select a file within the directory to compare results from (optional).</p></body></html>"))
            self.SimianFileOptions.setText(_translate("SimianSetup", "Simian File Options"))
            self.Kdiff3FileDirButton.setToolTip(_translate("SimianSetup", "<html><head/><body><p>Select the directory you have Kdiff3 installed in.</p></body></html>"))
            self.Kdiff3FileDirButton.setText(_translate("SimianSetup", "Directory Select"))
            self.simianFileDirButton.setToolTip(_translate("SimianSetup", "<html><head/><body><p>Select the directory that you have Simian installed in.</p></body></html>"))
            self.simianFileDirButton.setText(_translate("SimianSetup", "Directory Select"))
            self.simianFileDirLabel.setText(_translate("SimianSetup", "Simian Working File Directory"))
            self.BalanceParentheses.setToolTip(_translate("SimianSetup", "<html><head/><body><p>Ensures that expressions inside parenthesis that are split across multiple physical lines are considered as one.</p></body></html>"))
            self.BalanceParentheses.setText(_translate("SimianSetup", "Balance Parentheses"))
            self.BalanceSquareBrackets.setToolTip(_translate("SimianSetup", "<html><head/><body><p>Ensures that expressions inside square brackets that are split across multiple physical lines are considered as one. Defaults to false.</p></body></html>"))
            self.BalanceSquareBrackets.setText(_translate("SimianSetup", "Balance Square Brackets"))
            self.FailOnDupl.setToolTip(_translate("SimianSetup", "<html><head/><body><p>Causes the checker to fail the current process if duplication is detected.</p></body></html>"))
            self.FailOnDupl.setText(_translate("SimianSetup", "Fail on Duplication"))
            self.IgnoreCharacters.setToolTip(_translate("SimianSetup", "<html><head/><body><p>\'A\' and \'Z\'would both match.</p></body></html>"))
            self.IgnoreCharacters.setText(_translate("SimianSetup", "Ignore Characters"))
            self.IgnoreCharacterCase.setToolTip(_translate("SimianSetup", "<html><head/><body><p>\'A\' and \'a\'would both match.</p></body></html>"))
            self.IgnoreCharacterCase.setText(_translate("SimianSetup", "Ignore Character Case"))
            self.IgnoreCurlyBraces.setToolTip(_translate("SimianSetup", "<html><head/><body><p>Curly braces are ignored.</p><p><br/></p></body></html>"))
            self.IgnoreCurlyBraces.setText(_translate("SimianSetup", "Ignore Curly Braces"))
            self.IgnoreIdent.setToolTip(_translate("SimianSetup", "<html><head/><body><p>Completely ignores all identfiers.</p><p><br/></p></body></html>"))
            self.IgnoreIdent.setText(_translate("SimianSetup", "Ignore Identifiers"))
            self.IgnoreIdentCase.setToolTip(_translate("SimianSetup", "<html><head/><body><p>Matches identifiers irrespective of case. Eg. MyVariableName and myvariablename would both match.</p></body></html>"))
            self.IgnoreIdentCase.setText(_translate("SimianSetup", "Ignore Identifier Case"))
            self.IgnoreLiterals.setToolTip(_translate("SimianSetup", "<html><head/><body><p>\'A\', &quot;one&quot; and 27.8 would all match.</p></body></html>"))
            self.IgnoreLiterals.setText(_translate("SimianSetup", "Ignore Literals"))
            self.IgnoreNumbers.setToolTip(_translate("SimianSetup", "<html><head/><body><p>int x = 1; and int x = 576; would both match.</p></body></html>"))
            self.IgnoreNumbers.setText(_translate("SimianSetup", "Ignore Numbers"))
            self.IgnoreStringCase.setToolTip(_translate("SimianSetup", "<html><head/><body><p>&quot;Hello, World&quot; and &quot;HELLO, WORLD&quot; would both match.</p></body></html>"))
            self.IgnoreStringCase.setText(_translate("SimianSetup", "Ignore String Case"))
            self.IgnoreStrings.setToolTip(_translate("SimianSetup", "<html><head/><body><p>MyVariable and myvariablewould both match.</p></body></html>"))
            self.IgnoreStrings.setText(_translate("SimianSetup", "Ignore Strings"))
            self.IgnoreSubtypeNames.setToolTip(_translate("SimianSetup", "<html><head/><body><p>BufferedReader, StringReader and Reader would all match.</p></body></html>"))
            self.IgnoreSubtypeNames.setText(_translate("SimianSetup", "Ignore Subtype Names"))
            self.IgnoreModifiers.setToolTip(_translate("SimianSetup", "<html><head/><body><p>public, protected, static, etc.</p></body></html>"))
            self.IgnoreModifiers.setText(_translate("SimianSetup", "Ignore Modifiers"))
            self.IgnoreVariableNames.setToolTip(_translate("SimianSetup", "<html><head/><body><p>Completely ignores variable names (field, parameter and local). Eg. int foo = 1; and int bar = 1 would both match.</p></body></html>"))
            self.IgnoreVariableNames.setText(_translate("SimianSetup", "Ignore Variable Names"))

        app = QtWidgets.QApplication(sys.argv)
        SimianSetup = QtWidgets.QMainWindow()
        ui = Ui_SimianSetup()
        ui.setupUi(SimianSetup)
        SimianSetup.show()
        sys.exit(app.exec_())
