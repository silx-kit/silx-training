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
from imageplot import ImagePlot


class LaueFormWidget(Qt.QWidget):
    def __init__(self, parent=None):
        super(LaueFormWidget, self).__init__(parent)
        layout = Qt.QFormLayout(self)

        self._nCellsLineEdit = Qt.QLineEdit(self)
        layout.addRow("Number of unit cells:", self._nCellsLineEdit)

        self._oversamplingLineEdit = Qt.QLineEdit(self)
        layout.addRow("Oversampling:", self._oversamplingLineEdit)

        self._hLineEdit = Qt.QLineEdit(self)
        layout.addRow("H:", self._hLineEdit)

        self._kLineEdit = Qt.QLineEdit(self)
        layout.addRow("K:", self._kLineEdit)

        pushButton = Qt.QPushButton("Run and Save", self)
        pushButton.clicked.connect(self.compute)
        layout.addRow(pushButton)
        
        layout.addRow(Qt.QLabel("Preview:"))
        self._plot = ImagePlot()
        layout.addRow(self._plot)

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
        
        # Display preview result
        self._plot.setData(result)

        # Save to file
        numpy.save(filename, result)


if __name__ == '__main__':
    app = Qt.QApplication([])

    widget = LaueFormWidget()
    widget.show()

    app.exec_()
