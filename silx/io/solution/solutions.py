#!/usr/bin/env python

import numpy
import silx.io
from silx.gui import qt
from silx.gui import hdf5
import silx.gui.data.DataViewerFrame


def main_ex1():

    import silx.io
    h5 = silx.io.open("data/ID16B_diatomee.h5")

    from silx.gui import hdf5
    tree = hdf5.Hdf5TreeView()
    model = tree.findHdf5TreeModel()
    model.insertH5pyObject(h5)
    tree.setVisible(True)

    print(h5["/data/0000"])

    import silx.gui.data.DataViewerFrame
    viewer = silx.gui.data.DataViewerFrame.DataViewerFrame()
    viewer.setData(h5["/data/0000"])
    viewer.setVisible(True)

    return tree, viewer

###############################################################

def main_ex2():

    def correctedImage(data, background, flatfield):
        data = numpy.array(data, dtype=numpy.float32)
        flatfield = numpy.array(flatfield, dtype=numpy.float32)
        return (data - background) / (flatfield - background)

    import silx.io
    h5 = silx.io.open("data/ID16B_diatomee.h5")
    data = h5["/data/0000"][...]
    background = h5["/background/0000"][...]
    flatfield = h5["/flatfield/0000"][...]

    corrected = correctedImage(data, background, flatfield)

    import silx.gui.data.DataViewerFrame
    viewer = silx.gui.data.DataViewerFrame.DataViewerFrame()
    viewer.setData(corrected)
    viewer.setVisible(True)
    return viewer

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

        self.tree.activated.connect(self.onTreeActivated)

        return splitter

    def onTreeActivated(self):
        selectedObjects = list(self.tree.selectedH5Nodes())
        if len(selectedObjects) == 0:
            self.viewer.setData("Nothing selected")

        elif len(selectedObjects) > 1:
            self.viewer.setData("Too much things selected")

        obj = selectedObjects[0]
        self.viewer.setData(obj)

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
        return h5data.file["/background/0000"][...]

    def getFlatField(self, h5data):
        """
        :param h5data: H5py dataset selected from the group /data/
        """
        # return self.getFlatField1(h5data)
        # return self.getFlatField2(h5data)
        return self.getFlatField3(h5data)

    def getFlatField1(self, h5data):
        return h5data.file["/flatfield/0000"][...]

    def getFlatField2(self, h5data):
        index = int(h5data.name.split("/")[-1])
        if index < 250:
            return h5data.file["/flatfield/0000"][...]
        else:
            return h5data.file["/flatfield/0500"][...]

    def getFlatField3(self, h5data):
        index = int(h5data.name.split("/")[-1])
        flatfield0 = h5data.file["/flatfield/0000"][...]
        flatfield500 = h5data.file["/flatfield/0500"][...]
        coef = index / 500.0
        return flatfield0 * (1.0 - coef) + flatfield500 * coef


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
