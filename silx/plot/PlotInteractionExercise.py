
# coding: utf-8

from silx.gui.plot.actions import PlotAction
from silx.math.histogram import Histogramnd 
from silx.gui.plot import Plot1D
from silx.gui import qt

import h5py
import numpy


class ComputeHistogramAction(PlotAction):
    """Computes the intensity distribution on the current image

    :param plot: :class:`.PlotWidget` instance on which to operate
    :param parent: See :class:`QAction`
    """
    def __init__(self, plot, parent=None):
        # PlotAction.__init__(...)
        # TODO ...
        pass

    def computeIntensityDistribution(self):
        """Get the active image and compute the image 
        intensity distribution"""
        # By inheriting from PlotAction, we get access to attribute 
        # self.plot
        # which is a reference to the PlotWindow
        # TODO ...
        pass


def showH5ls(_datapath):
    """show the h5ls window to explore the file"""
    from silx.io.utils import h5ls
    h5ls(_datapath)


def plotHistogram(image):
    """display the pixel intensity distribution"""

    ## create the histogramnd 
    # - using silx.math.histogram.Histogramnd
    # 
    # - http://www.silx.org/doc/silx/dev/modules/math/histogram.html

    from silx.math.histogram import Histogramnd
    histo, w_histo, edges = Histogramnd(image.flatten(), n_bins=256, histo_range=[0,256])
    plot=Plot1D()
    # ... TODO : plot the histogram1D using silx.gui.plot.Plot1d

    return plot

def main():

    app=qt.QApplication([])

    ## load data from data/lena.hdf5
    datapath='data/lena.hdf5'
    f=h5py.File(datapath)
    image=numpy.array(f['lena'], dtype='float32')

    showH5ls(datapath)

    plotimage=plotHistogram(image)

    # create a PlotAction which plot the histogram for the current image
    # 
    # - using silx.gui.plot.PlotActions.PlotAction
    # 
    # - doc@ http://www.silx.org/doc/silx/dev/modules/gui/plot/actions/examples.html
    #     

    myaction=ComputeHistogramAction(image)
    ## Add this action into the toolBar of the window
    #  TODO ... 
    toolBar=plotimage.toolBar()
    # TODO ...


    # show automatically the histogram when the image change
    # 
    # - using plotImage.sigActiveImageChanged.connect(plotHisto)
    # TODO ...

    plotimage.show()
    app.exec_()

main()