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
        isAtomic = len(data.shape) == 0
        isCurve = len(data.shape) == 1 and numpy.issubdtype(data.dtype, numpy.number)
        isImage = len(data.shape) == 2 and numpy.issubdtype(data.dtype, numpy.number)
        if isAtomic:
            self.showAsString(data.value)
        elif isCurve:
            self.show1d(data)
        elif isImage:
            self.show2d(data)
        else:
            self.showAsString(data.value)


TREE_WIDGET = None
VIEWER_WIDGET = None


def onTreeActivated():
    selectedObjects = list(TREE_WIDGET.selectedH5Nodes())
    if len(selectedObjects) == 0:
        print("Nothing selected")
    elif len(selectedObjects) > 1:
        print("Too much things selected")
    else:
        obj = selectedObjects[0]
        if obj.ntype == h5py.Dataset:
            isImage = len(obj.shape) == 2 and numpy.issubdtype(obj.dtype, numpy.number)
            if isImage:
                corrected = computeCorrectedImage(obj.h5py_object)
                if corrected is None:
                    VIEWER_WIDGET.show(obj.h5py_object)
                else:
                    VIEWER_WIDGET.show(corrected)
            else:
                VIEWER_WIDGET.show(obj.h5py_object)
        else:
            VIEWER_WIDGET.showAsString("Path: " + obj.local_name)


BACKGROUND = None
FLATFIELD = None


def computeCorrectedImage(raw):
    if FLATFIELD is None:
        return None
    if BACKGROUND is None:
        return None

    return numpy.array((raw.value - BACKGROUND.value), dtype=numpy.float32) / (FLATFIELD.value - BACKGROUND.value)


def setBackground(dataset):
    global BACKGROUND
    BACKGROUND = dataset


def setFlatField(dataset):
    global FLATFIELD
    FLATFIELD = dataset


def populateContextMenu(event):
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
    action.triggered.connect(lambda: setBackground(obj.h5py_object))
    action.setEnabled(isImage)
    menu.addAction(action)

    # Action to pick the background
    action = qt.QAction("Pick this value as flat field", event.source())
    action.triggered.connect(lambda: setFlatField(obj.h5py_object))
    action.setEnabled(isImage)
    menu.addAction(action)


def main(filenames):
    global VIEWER_WIDGET, TREE_WIDGET
    app = qt.QApplication([])

    window = qt.QSplitter()
    TREE_WIDGET = hdf5.Hdf5TreeView(window)
    VIEWER_WIDGET = DataViewer(window)
    window.addWidget(TREE_WIDGET)
    window.addWidget(VIEWER_WIDGET)
    window.setStretchFactor(1, 1)
    window.setVisible(True)

    # connect activated (dbl-click, return key) to a callback
    TREE_WIDGET.activated.connect(onTreeActivated)
    TREE_WIDGET.addContextMenuCallback(populateContextMenu)

    for filename in filenames:
        TREE_WIDGET.findHdf5TreeModel().insertFile(filename)

    app.exec_()


main(sys.argv[1:])
