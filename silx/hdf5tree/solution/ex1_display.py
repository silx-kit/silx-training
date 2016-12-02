#!/usr/bin/env python

import sys

from silx.gui import qt
from silx.gui import hdf5


def main(filenames):
    app = qt.QApplication([])

    tree = hdf5.Hdf5TreeView()
    tree.setVisible(True)

    model = tree.findHdf5TreeModel()
    for filename in filenames:
        model.insertFile(filename)

    app.exec_()


main(sys.argv[1:])
