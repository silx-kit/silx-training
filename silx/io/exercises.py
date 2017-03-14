#!/usr/bin/env python

import numpy
import silx.io
from silx.gui import qt
from silx.gui import hdf5
import silx.gui.data.DataViewerFrame


def main_ex1():

    #
    # EXERCISE: Open the file 'data/ID16B_diatomee.h5'
    #

    h5 = ...

    #
    # EXERCISE: Display the file into the HDF5 tree
    #

    from silx.gui import hdf5
    tree = hdf5.Hdf5TreeView()
    model = tree.findHdf5TreeModel()
    ...
    tree.setVisible(True)

    #
    # EXERCISE: Access to one frame of the image
    #

    print(...)

    #
    # EXERCISE: Display it with the data viwer
    #
    import silx.gui.data.DataViewerFrame
    viewer = silx.gui.data.DataViewerFrame.DataViewerFrame()
    ...
    viewer.setVisible(True)


def main_ex2():

    def correctedImage(data, background, flatfield):
        data = numpy.array(data, dtype=numpy.float32)
        flatfield = numpy.array(flatfield, dtype=numpy.float32)
        return (data - background) / (flatfield - background)

    #
    # EXERCISE: Reach one data frame, a background and a flatfield from 'data/ID16B_diatomee.h5'
    #

    ...

    #
    # EXERCISE: Compute the corrected image
    #

    ...

    #
    # EXERCISE: Display it with the data viewer
    #

    ...

###############################################################


class ViewerEx3(qt.QMainWindow):

    def __init__(self, parent=None):
        qt.QMainWindow.__init__(self, parent)
        widget = self.createCentralWidget()
        self.setCentralWidget(widget)

    def createCentralWidget(self):
        splitter = qt.QSplitter(self)

        # the tree
        self.tree = silx.gui.hdf5.Hdf5TreeView(self)
        # the data viewer
        self.viewer = silx.gui.data.DataViewerFrame.DataViewerFrame(self)

        splitter.addWidget(self.tree)
        splitter.addWidget(self.viewer)
        splitter.setStretchFactor(1, 1)

        #
        # EXERCISE: Connect the callback onTreeActivated (bellow)
        #           to a mouse event from the tree
        #

        return splitter

    def onTreeActivated(self):

        #
        # EXERCISE: Reach selected objects from the tree
        #

        #
        # EXERCISE: Provide it to the data viewer
        #
        pass

    def appendFile(self, filename):
        model = self.tree.findHdf5TreeModel()
        model.insertFile(filename)
        print("Load %s" % filename)

def main_ex3():
    from silx.gui import qt
    viewer = ViewerEx3()
    viewer.appendFile('data/ID16B_diatomee.h5')
    viewer.setVisible(True)
    return viewer

###############################################################

class ViewerEx4(ViewerEx3):

    def onTreeActivated(self):
        selectedObjects = list(self.tree.selectedH5Nodes())
        if len(selectedObjects) == 0:
            self.viewer.setData("Nothing selected")

        elif len(selectedObjects) > 1:
            self.viewer.setData("Too much things selected")

        else:
            obj = selectedObjects[0]
            node = obj.h5py_object

            if "/data/" in node.name:
                # That's a data from the /data group
                data = self.computeCorrectedImage(node)
                self.viewer.setData(data)
            else:
                # Other data is displayed in a normal way
                self.viewer.setData(obj)

    def computeCorrectedImage(self, h5data):
        """
        :param h5data: H5py dataset selected from the group /data/
        """
        background = self.getBackground(h5data)
        flatfield = self.getFlatField(h5data)

        raw = numpy.array(h5data, dtype=numpy.float32)
        flatfield = numpy.array(flatfield, dtype=numpy.float32)
        background = background[...]
        return (raw - background) / (flatfield - background)

    def getBackground(self, h5data):
        """
        :param h5data: H5py dataset selected from the group /data/
        """

        #
        # EXERCISE: Return the background image from the dataset
        #

        return None

    def getFlatField(self, h5data):
        """
        :param h5data: H5py dataset selected from the group /data/
        """

        #
        # EXERCISE: Return the flatfield image from the dataset
        #
        #           1) you can return a flatfield by default
        #           2) you can return the closest flat field according to the index of the data
        #           3) you can return an interpolation of the 2 flatfields according to the index of the data

        return None


def main_ex4():
    viewer = ViewerEx4()
    viewer.appendFile('data/ID16B_diatomee.h5')
    viewer.setVisible(True)
    return viewer

###############################################################

if __name__ == "__main__":
    def raise_param_error():
        raise Exception('One an only one argument is expected (ex1, ex2, ex3, or ex4). ')

    import sys
    if len(sys.argv) != 2:
        raise_param_error()

    from silx.gui import qt
    app = qt.QApplication([])

    arg = sys.argv[1]
    if arg == 'ex1':
        mem = main_ex1()
    elif arg == 'ex2':
        mem = main_ex2()
    elif arg == 'ex3':
        mem = main_ex3()
    elif arg == 'ex4':
        mem = main_ex4()
    else:
        raise_param_error()

    app.exec_()
