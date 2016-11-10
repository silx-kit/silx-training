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

    #
    # TODO: Reach selected objects from the tree
    #

    #
    # TODO: If it is a dataset, show it in the viewer
    #
    pass


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

    #
    # TODO: Connect onTreeActivated the tree event
    #

    app.exec_()


main(sys.argv[1:])
