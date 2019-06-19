# coding: utf-8
#
# Copyright (c) 2019 European Synchrotron Radiation Facility
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import os
import numpy

from PyQt5 import Qt

import laue


class LaueFormWidget(Qt.QWidget):
    def __init__(self, parent=None):
        super(LaueFormWidget, self).__init__(parent)
        layout = Qt.QFormLayout(self)
        
        tooltip = "Number of unit cells of the 2D cristal in both dimension"
        self._nCellsLineEdit = Qt.QLineEdit(self)
        self._nCellsLineEdit.setToolTip(tooltip)
        label = Qt.QLabel("Number of unit cells:")
        label.setToolTip(tooltip)
        layout.addRow(label, self._nCellsLineEdit)

        tooltip = "The number of sampling point for each unit cells (at least 2)"
        self._oversamplingLineEdit = Qt.QLineEdit(self)
        self._oversamplingLineEdit.setToolTip(tooltip)
        label = Qt.QLabel("Oversampling:")
        label.setToolTip(tooltip)
        layout.addRow(label, self._oversamplingLineEdit)

        tooltip = "<b>H</b> Miller index around which to do the sampling"
        self._hLineEdit = Qt.QLineEdit(self)
        self._hLineEdit.setToolTip(tooltip)
        label = Qt.QLabel("H:")
        label.setToolTip(tooltip)
        layout.addRow(label, self._hLineEdit)

        tooltip = "<b>K</b> Miller index around which to do the sampling"
        self._kLineEdit = Qt.QLineEdit(self)
        self._kLineEdit.setToolTip(tooltip)
        label = Qt.QLabel("K:")
        label.setToolTip(tooltip)
        layout.addRow(label, self._kLineEdit)

        pushButton = Qt.QPushButton("Run and Save", self)
        pushButton.setToolTip(
            "Run the computation with current parameters and\nsave result to a file")
        pushButton.clicked.connect(self.compute)
        layout.addRow(pushButton)

    def compute(self):
        # Open file dialog
        filename, selectedFilter = Qt.QFileDialog.getSaveFileName(
            self,
            "Save to",
            os.path.join(os.getcwd(), "result.npy"),
            "numpy array (*.npy)")

        if filename == '':
            return  # Cancelled

        # Retrieve parameters
        ncells = int(self._nCellsLineEdit.text())
        h = int(self._hLineEdit.text())
        k = int(self._kLineEdit.text())
        oversampling = int(self._oversamplingLineEdit.text())

        # Run computation
        result = laue.laue_image(ncells, h, k, oversampling)

        # Save to file
        numpy.save(filename, result)


if __name__ == '__main__':
    app = Qt.QApplication([])

    widget = LaueFormWidget()
    widget.show()

    app.exec_()
