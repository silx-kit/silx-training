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

from PyQt5 import Qt, uic

import laue  # Simulation code: No dependency on the GUI code


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


class LaueMainWindow(Qt.QMainWindow):

    _sigProcessingDone = Qt.pyqtSignal(numpy.ndarray)

    def __init__(self, *args, **kwargs):
        super(LaueMainWindow, self).__init__(*args, **kwargs)
        uifile = os.path.join(os.path.dirname(__file__), 'laue_app.ui')
        uic.loadUi(uifile, self)
        self._resultData = None
        self._processingThread = None

        self._sigProcessingDone.connect(self._processingDone)

        self._saveAction.triggered.connect(self._save)
        app = Qt.QApplication.instance()
        self._quitAction.triggered.connect(app.quit)

        self._nCellsLineEdit.textChanged.connect(self._updateOutputSize)  # or editingFinished

        self._oversamplingLineEdit.textChanged.connect(
            self._updateOutputSize)  # or editingFinished

        self._pushButton.clicked.connect(self._runClicked)

        self._saveButton.clicked.connect(self._save)

        # Init output size
        self._updateOutputSize()

    def result(self):
        if self._resultData is None:
            return None
        else:
            return numpy.array(self._resultData, copy=True)

    def _updateOutputSize(self, *args):
        ncells = self._nCellsLineEdit.value()
        oversampling = self._oversamplingLineEdit.value()
        array_size = laue.laue_array_size(ncells, oversampling)
        self._outputSizeLabel.setText("%dx%d" % (array_size, array_size))

    def _runClicked(self, checked=False):
        self._pushButton.setEnabled(False)
        self._saveButton.setEnabled(False)
        self._saveAction.setEnabled(False)
        self.statusBar().showMessage("Processing...")

        ncells = self._nCellsLineEdit.value()
        h = self._hLineEdit.value()
        k = self._kLineEdit.value()
        oversampling = self._oversamplingLineEdit.value()

        self._processingThread = ProcessingThread(
            ncells, h, k, oversampling,self._sigProcessingDone.emit)
        self._processingThread.start()

    def _processingDone(self, result):
        self._resultData = result
        self._processingThread = None

        self._resultPlot.setData(self._resultData)

        self._saveButton.setEnabled(True)
        self._saveAction.setEnabled(True)

        self._pushButton.setEnabled(True)
        self.statusBar().showMessage("Done")

    def _save(self):
        filename, selectedFilter = Qt.QFileDialog.getSaveFileName(
            self,
            "Save to",
            os.path.join(os.getcwd(), "result.npy"),
            "numpy array (*.npy)")
        if filename != '':
            numpy.save(filename, self._resultData)
            self.statusBar().showMessage("Saved to %s" % filename)


if __name__ == "__main__":
    app = Qt.QApplication([])

    window = LaueMainWindow()
    window.setAttribute(Qt.Qt.WA_DeleteOnClose)
    window.show()

    app.exec_()
    del app
