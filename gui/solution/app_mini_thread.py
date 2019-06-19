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
import threading
import numpy

from PyQt5 import Qt

import laue


# This class could go into laue.py:
# It does NOT depend on the GUI
class ProcessingThread(threading.Thread):
    def __init__(self, ncells, h, k, oversampling, callback):
        super(ProcessingThread, self).__init__()
        self.ncells = ncells
        self.h = h
        self.k = k
        self.oversampling = oversampling
        self.callback = callback

    def run(self):
        result = laue.laue_image(
            self.ncells, self.h, self.k, self.oversampling)
        self.callback(result)


class LaueFormWidget(Qt.QWidget):
    
    # This signal is used internally to react when the processing is done
    # A signal can be emitted from any thread, it is handled in the thread
    # the connected object belongs to (i.e., the one it has been created in).
    _sigProcessingDone = Qt.pyqtSignal(numpy.ndarray)

    def __init__(self, parent=None):
        super(LaueFormWidget, self).__init__(parent)
        self._processingThread = None  # Placeholder for the thread

        layout = Qt.QFormLayout(self)

        self._nCellsLineEdit = Qt.QLineEdit(self)
        layout.addRow("Number of unit cells:", self._nCellsLineEdit)

        self._oversamplingLineEdit = Qt.QLineEdit(self)
        layout.addRow("Oversampling:", self._oversamplingLineEdit)

        self._hLineEdit = Qt.QLineEdit(self)
        layout.addRow("H:", self._hLineEdit)

        self._kLineEdit = Qt.QLineEdit(self)
        layout.addRow("K:", self._kLineEdit)

        self._pushButton = Qt.QPushButton("Run and Save", self)
        self._pushButton.clicked.connect(self._runClicked)
        layout.addRow(self._pushButton)

        # Connect a method to handle the processing done
        self._sigProcessingDone.connect(self._processingDone)
        
    def _runClicked(self):
        self._pushButton.setEnabled(False)
        self._pushButton.setText("Processing...")

        # Retrieve parameters
        ncells = int(self._nCellsLineEdit.text())
        h = int(self._hLineEdit.text())
        k = int(self._kLineEdit.text())
        oversampling = int(self._oversamplingLineEdit.text())

        # Start processing thread
        # Use the signal emit method as a callback
        self._processingThread = ProcessingThread(
            ncells, h, k, oversampling, callback=self._sigProcessingDone.emit)
        self._processingThread.start()
        
    def _processingDone(self, result):
        self._processingThread = None

        # Open file dialog
        filename, selectedFilter = Qt.QFileDialog.getSaveFileName(
            self,
            "Save to",
            os.path.join(os.getcwd(), "result.npy"),
            "numpy array (*.npy)")

        if filename != '':
            # Save to file
            numpy.save(filename, result)

        self._pushButton.setEnabled(True)
        self._pushButton.setText("Run and Save")
        

if __name__ == '__main__':
    app = Qt.QApplication([])

    widget = LaueFormWidget()
    widget.show()

    app.exec_()
