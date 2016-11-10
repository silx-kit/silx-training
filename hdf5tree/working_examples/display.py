#!/usr/bin/env python

import sys

from silx.gui import qt
from silx.gui import hdf5


TREE_WIDGET = None


def main(filenames):
    global TREE_WIDGET
    app = qt.QApplication([])

    window = qt.QSplitter()
    TREE_WIDGET = hdf5.Hdf5TreeView(window)
    window.addWidget(TREE_WIDGET)
    window.setVisible(True)

    model = TREE_WIDGET.findHdf5TreeModel()
    for filename in filenames:
        model.insertFile(filename)

    app.exec_()


main(sys.argv[1:])
