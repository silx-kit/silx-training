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


class IntLineEdit(Qt.QLineEdit):
    def __init__(self, bottom, parent=None):
        super(IntLineEdit, self).__init__(parent)
        validator = Qt.QIntValidator()
        validator.setBottom(bottom)
        self.setValidator(validator)
        self.setValue(bottom)
        
    def value(self):
        text = self.text()
        if not text:
            return 0
        else:
            return int(text)

    def setValue(self, value):
        self.setText(str(value))

        
class LaueFormWidget(Qt.QWidget):
    def __init__(self, parent=None):
        super(LaueFormWidget, self).__init__(parent)
        layout = Qt.QFormLayout(self)

        self._nCellsLineEdit = IntLineEdit(2, self)
        layout.addRow("Number of unit cells:", self._nCellsLineEdit)

        self._oversamplingLineEdit = IntLineEdit(2, self)
        layout.addRow("Oversampling:", self._oversamplingLineEdit)

        self._hLineEdit = Qt.QLineEdit(self)
        self._hLineEdit.setValidator(Qt.QDoubleValidator())
        layout.addRow("H:", self._hLineEdit)

        self._kLineEdit = Qt.QLineEdit(self)
        self._kLineEdit.setValidator(Qt.QDoubleValidator())
        layout.addRow("K:", self._kLineEdit)

        pushButton = Qt.QPushButton("Run and Save", self)
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
        ncells = self._nCellsLineEdit.value()
        h = int(self._hLineEdit.text())
        k = int(self._kLineEdit.text())
        oversampling = self._oversamplingLineEdit.value()

        # Run computation
        result = laue.laue_image(ncells, h, k, oversampling)

        # Save to file
        numpy.save(filename, result)


if __name__ == '__main__':
    app = Qt.QApplication([])

    widget = LaueFormWidget()
    widget.show()

    app.exec_()
