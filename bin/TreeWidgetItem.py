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

from PyQt5 import QtWidgets

'''TreeWidgetItem reimplements the sorting algorithm so that it can properly
sort integers and floats by modifying the lessthan, or __lt__ method'''


class TreeWidgetItem(QtWidgets.QTreeWidgetItem):
    # initialization as a QTreeWidgetItem with no parent at base
    def __init__(self, parent=None):
        QtWidgets.QTreeWidgetItem.__init__(self, parent)

    # method override of __lt__
    def __lt__(self, otherItem):
        # define the column sorter
        column = self.treeWidget().sortColumn()
        # try catch block which checks if the value in the columns are floats
        try:
            # if so, return the float sorter, rather than a string sorter
            return float(self.text(column)) < float(otherItem.text(column))
        # if the TreeWidgetItems throw a value error,
        # use string sorting as usual
        except ValueError:
            return self.text(column) < otherItem.text(column)
