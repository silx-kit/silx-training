#!/usr/bin/env python

import sys
import numpy
import h5py

from silx.gui import qt
from silx.gui import plot
from silx.gui import hdf5


class DataViewer(qt.QStackedWidget):
    """Widget to display any kind of data"""

    def __init__(self, parent):
        """Constructor"""
        super(DataViewer, self).__init__(parent)

        self.__plot1d = plot.Plot1D()
        self.__plot2d = plot.Plot2D()
        self.__text = qt.QLabel()
        self.__text.setAlignment(qt.Qt.AlignCenter)

        self.__index1d = self.addWidget(self.__plot1d)
        self.__index2d = self.addWidget(self.__plot2d)
        self.__indexText = self.addWidget(self.__text)
        self.setCurrentIndex(self.__indexText)

    def showAsString(self, data):
        """Display a data using text"""
        if isinstance(data, h5py.Dataset):
            data = data.value
        self.__text.setText(str(data))
        self.setCurrentIndex(self.__indexText)

    def show1d(self, data):
        """Display a data using silx Plot1D"""
        self.__plot1d.clear()
        self.__plot1d.addCurve(legend="data", x=range(len(data)), y=data)
        self.setCurrentIndex(self.__index1d)

    def show2d(self, data):
        """Display a data using silx Plot2D"""
        self.__plot2d.clear()
        self.__plot2d.addImage(legend="data", data=data)
        self.setCurrentIndex(self.__index2d)

    def show(self, data):
        """Display a data using the widget which fit the best"""
        if isinstance(data, (numpy.ndarray, h5py.Dataset)):
            isAtomic = len(data.shape) == 0
            isCurve = len(data.shape) == 1 and numpy.issubdtype(data.dtype, numpy.number)
            isImage = len(data.shape) == 2 and numpy.issubdtype(data.dtype, numpy.number)
            if isAtomic:
                self.showAsString(data)
            elif isCurve:
                self.show1d(data)
            elif isImage:
                self.show2d(data)
            else:
                self.showAsString(data)
        else:
            self.showAsString(data)


class Viewer(qt.QMainWindow):
    """An HDF5 viewer"""

    def __init__(self, parent=None):
        qt.QMainWindow.__init__(self, parent)
        self.setWindowTitle("HDF5 viewer")

        # create a tree and a DataViewer separated by a splitter
        splitter = qt.QSplitter()
        self.tree = hdf5.Hdf5TreeView(splitter)
        self.dataViewer = DataViewer(splitter)
        splitter.addWidget(self.tree)
        splitter.addWidget(self.dataViewer)
        splitter.setStretchFactor(1, 1)
        splitter.setVisible(True)
        self.setCentralWidget(splitter)

        # connect activated (dbl-click, return key) to a callback
        self.tree.activated.connect(self.onTreeActivated)
        # connect the tree to the context menu
        self.tree.addContextMenuCallback(self.populateContextMenu)

        self.background = None
        self.flatfield = None

    def appendFile(self, filename):
        self.tree.findHdf5TreeModel().insertFile(filename)

    def computeCorrectedImage(self, raw):
        if self.flatfield is None:
            raise RuntimeError("Flatfield is not defined")
        if self.background is None:
            raise RuntimeError("Background is not defined")

        raw = numpy.array(raw, dtype=numpy.float32)
        flatfield = numpy.array(self.flatfield.value, dtype=numpy.float32)
        background = self.background.value
        return (raw - background) / (flatfield - background)

    def setBackground(self, dataset):
        self.background = dataset

    def setFlatField(self, dataset):
        self.flatfield = dataset

    def onTreeActivated(self):
        selectedObjects = list(self.tree.selectedH5Nodes())
        if len(selectedObjects) == 0:
            self.dataViewer.showAsString("Nothing selected")
            return
        elif len(selectedObjects) > 1:
            self.dataViewer.showAsString("Too many things selected")
            return
        else:
            obj = selectedObjects[0]
            if obj.ntype == h5py.Dataset:
                isImage = len(obj.shape) == 2 and numpy.issubdtype(obj.dtype, numpy.number)
                if isImage:
                    try:
                        corrected = self.computeCorrectedImage(obj.h5py_object)
                        self.dataViewer.show(corrected)
                    except:
                        self.dataViewer.show(obj.h5py_object)
                else:
                    self.dataViewer.show(obj.h5py_object)
            else:
                self.dataViewer.showAsString("Path: " + obj.local_name)

    def populateContextMenu(self, event):
        """Called to populate the context menu

        :param silx.gui.hdf5.Hdf5ContextMenuEvent event: Event
            containing expected information to populate the context menu
        """

        selectedObjects = list(event.source().selectedH5Nodes())
        if len(selectedObjects) == 0:
            return
        if len(selectedObjects) > 1:
            return
        obj = selectedObjects[0]
        # obj = event.hoveredObject()

        if obj.ntype is not h5py.Dataset:
            return

        menu = event.menu()

        isNumber = obj.shape == tuple() and numpy.issubdtype(obj.dtype, numpy.number)
        isImage = len(obj.shape) == 2 and numpy.issubdtype(obj.dtype, numpy.number)

        # Action to pick the image
        action = qt.QAction("Pick this value as background", event.source())
        action.triggered.connect(lambda: self.setBackground(obj.h5py_object))
        action.setEnabled(isImage)
        menu.addAction(action)

        # Action to pick the background
        action = qt.QAction("Pick this value as flat field", event.source())
        action.triggered.connect(lambda: self.setFlatField(obj.h5py_object))
        action.setEnabled(isImage)
        menu.addAction(action)

def main(filenames):
    app = qt.QApplication([])
    viewer = Viewer()
    for filename in filenames:
        viewer.appendFile(filename)
    viewer.setVisible(True)
    app.exec_()


main(sys.argv[1:])
