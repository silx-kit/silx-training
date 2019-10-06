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

import laue  # Simulation code: No dependency on the GUI code
from imageplot import ImagePlot


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


class IntLineEdit(Qt.QLineEdit):
    """LineEdit widget for integer

    :param Union[int,None] bottom: Minimum of accepted range
    :param Union[int,None] top: Maximum of accepted range
    :param QWidget parent:
    """
    def __init__(self, parent=None, bottom=None, top=None):
        super(IntLineEdit, self).__init__(parent)
        validator = Qt.QIntValidator(self)
        if bottom is not None:
            validator.setBottom(bottom)
        if top is not None:
            validator.setTop(top)
        self.setValidator(validator)
        self.editingFinished.connect(self._cleanDisplayedValue)

    def _defaultValue(self):
        """Returns a default value based on bottom and top"""
        bottom = self.validator().bottom()
        if bottom != numpy.iinfo(numpy.int32).min:
            default = bottom
        else:
            top = self.validator().top()
            if top != numpy.iinfo(numpy.int32).max:
                default = top
            else:
                default = 0
        return default

    def _cleanDisplayedValue(self):
        """Remove leading 0 if any"""
        self.setValue(self.value())

    def value(self):
        """Returns the current value

        :rtype: int
        """
        text = self.text()
        if text == '':
            return self._defaultValue()
        else:
            return int(text)

    def setValue(self, value):
        """Set the displayed value

        :param int value:
        """
        self.setText(str(value))


class HorizontalLine(Qt.QFrame):
    def __init__(self, *args, **kwargs):
        super(HorizontalLine, self).__init__(*args, **kwargs)

        self.setFrameShape(Qt.QFrame.HLine)
        self.setFrameShadow(Qt.QFrame.Sunken)


class LaueMainWindow(Qt.QMainWindow):

    _sigProcessingDone = Qt.pyqtSignal(numpy.ndarray)

    def __init__(self, *args, **kwargs):
        super(LaueMainWindow, self).__init__(*args, **kwargs)
        self._resultData = None
        self._processingThread = None

        self._sigProcessingDone.connect(self._processingDone)

        self.setWindowTitle("Laue simulation of a square 2D cristal")

        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu("File")
        self._saveAction = fileMenu.addAction("Save", self._save, shortcut=Qt.QKeySequence.Save)
        self._saveAction.setEnabled(False)
        fileMenu.addSeparator()
        app = Qt.QApplication.instance()
        fileMenu.addAction("Quit", app.quit, shortcut=Qt.QKeySequence.Quit)

        centralWidget = Qt.QWidget(self)
        layout = Qt.QFormLayout(centralWidget)

        self._nCellsLineEdit = IntLineEdit(parent=centralWidget, bottom=1)
        self._nCellsLineEdit.setValue(10)
        self._nCellsLineEdit.setAlignment(Qt.Qt.AlignRight)
        self._nCellsLineEdit.textChanged.connect(self._updateOutputSize)  # or editingFinished
        layout.addRow("Number of unit cells:", self._nCellsLineEdit)

        self._oversamplingLineEdit = IntLineEdit(parent=centralWidget, bottom=1)
        self._oversamplingLineEdit.setValue(5)
        self._oversamplingLineEdit.setAlignment(Qt.Qt.AlignRight)
        self._oversamplingLineEdit.textChanged.connect(
            self._updateOutputSize)  # or editingFinished
        layout.addRow("Oversampling:", self._oversamplingLineEdit)

        layout.addRow(HorizontalLine())

        self._hLineEdit = IntLineEdit(parent=centralWidget, bottom=0)
        self._hLineEdit.setValue(0)
        self._hLineEdit.setAlignment(Qt.Qt.AlignRight)
        layout.addRow("H:", self._hLineEdit)

        self._kLineEdit = IntLineEdit(parent=centralWidget, bottom=0)
        self._kLineEdit.setValue(0)
        self._kLineEdit.setAlignment(Qt.Qt.AlignRight)
        layout.addRow("K:", self._kLineEdit)

        self._pushButton = Qt.QPushButton("Run", centralWidget)
        self._pushButton.clicked.connect(self._runClicked)
        layout.addRow(self._pushButton)

        layout.addRow(HorizontalLine())

        self._outputSizeLabel = Qt.QLabel(centralWidget)
        self._outputSizeLabel.setTextInteractionFlags(
            Qt.Qt.TextSelectableByMouse)  # Allow copy
        self._outputSizeLabel.setAlignment(Qt.Qt.AlignRight)
        layout.addRow("Output size:", self._outputSizeLabel)

        label = Qt.QLabel("Result preview:", centralWidget)
        layout.addRow(label)

        self._resultPlot = ImagePlot()
        layout.addRow(self._resultPlot)

        self._saveButton = Qt.QPushButton("Save", centralWidget)
        self._saveButton.clicked.connect(self._save)
        self._saveButton.setEnabled(False)
        layout.addRow(self._saveButton)

        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)

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
