#!/usr/bin/env python

import sys

from silx.gui import qt
from silx.gui import hdf5


TREE_WIDGET = None


def main(filenames):
    global DATA_WIDGET, TREE_WIDGET
    app = qt.QApplication([])

    window = qt.QSplitter()
    TREE_WIDGET = hdf5.Hdf5TreeView(window)
    window.addWidget(TREE_WIDGET)
    window.setVisible(True)

    for filename in filenames:
        #
        # TODO: Load each filename into the tree
        #
        pass

    app.exec_()


main(sys.argv[1:])
