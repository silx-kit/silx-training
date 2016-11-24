#!/usr/bin/env python

import sys

from silx.gui import qt
from silx.gui import hdf5


def main(filenames):
    app = qt.QApplication([])

    window = qt.QSplitter()
    tree = hdf5.Hdf5TreeView(window)
    window.addWidget(tree)
    window.setVisible(True)

    model = tree.findHdf5TreeModel()
    for filename in filenames:
        #
        # TODO: Load each filename into the model tree
        #
        print("Load %s" % filename)

    app.exec_()

if __name__ == "__main__":
    main(sys.argv[1:])

main(sys.argv[1:])
