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

        self._nCellsSpinBox = Qt.QSpinBox(self)
        self._nCellsSpinBox.setMinimum(2)
        layout.addRow("Number of unit cells:", self._nCellsSpinBox)

        self._oversamplingSpinBox = Qt.QSpinBox(self)
        self._oversamplingSpinBox.setMinimum(2)
        layout.addRow("Oversampling:", self._oversamplingSpinBox)

        self._hDoubleSpinBox = Qt.QDoubleSpinBox(self)
        layout.addRow("H:", self._hDoubleSpinBox)

        self._kDoubleSpinBox = Qt.QDoubleSpinBox(self)
        layout.addRow("K:", self._kDoubleSpinBox)

        pushButton = Qt.QPushButton("Run and Save", self)
        pushButton.clicked.connect(self.compute)
        layout.addRow(pushButton)
        
        self._sizeLabel = Qt.QLabel('')
        layout.addRow("Output size:", self._sizeLabel)
        self._updateSizeLabel()  # Initialize displayed size

        self._nCellsSpinBox.valueChanged.connect(self._updateSizeLabel)
        self._oversamplingSpinBox.valueChanged.connect(self._updateSizeLabel)
        
    def _updateSizeLabel(self, value=None):
        ncells = int(self._nCellsSpinBox.value())
        oversampling = int(self._oversamplingSpinBox.value())
        size = laue.laue_array_size(ncells, oversampling)
        self._sizeLabel.setText("%dx%d" % (size, size))

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
        ncells = int(self._nCellsSpinBox.value())
        h = int(self._hDoubleSpinBox.value())
        k = int(self._kDoubleSpinBox.value())
        oversampling = int(self._oversamplingSpinBox.value())

        # Run computation
        result = laue.laue_image(ncells, h, k, oversampling)

        # Save to file
        numpy.save(filename, result)


if __name__ == '__main__':
    app = Qt.QApplication([])

    widget = LaueFormWidget()
    widget.show()

    app.exec_()
