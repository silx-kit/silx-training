
# coding: utf-8

# # Histogram vs Histogram_lut

import numpy
from silx.math.histogram import Histogramnd, HistogramndLut
from silx.gui.plot import Plot1D, Plot2D
from silx.gui import qt

app = qt.QApplication([])

def createDataSet():
    "create some data with noise."
    shape = (400, 400)
    xcenter = shape[0]/2
    ycenter = shape[1]/2
    t = numpy.zeros(shape)
    y, x=numpy.ogrid[:t.shape[0], :t.shape[1]]
    r=1.0+numpy.sin(numpy.sqrt((x-xcenter)**2+(y-ycenter)**2)/8.0)
    return r + numpy.random.rand(shape[0], shape[1])

data = createDataSet()
p = Plot2D()
p.addImage(legend='dataExample', data=data)
p.show()

# ## Exercise : use Histogramnd to compute azimutal integration
# 
# ### we 

# In[ ]:

def computeradius(data):
    "compute raddi to center for each pixel"
    xcenter=data.shape[0]/2
    ycenter=data.shape[1]/2
    y, x=numpy.ogrid[:data.shape[0], :data.shape[1]]
    r=numpy.sqrt((x-xcenter)**2+(y-ycenter)**2)
    return r


radii = computeradius(data)
# TODO : plot radii data into a Plot2D widget
# ...


# ### plot the histogram of the radii
# 
# documentation :
# 
#    - http://pythonhosted.org/silx/modules/math/histogram.html

nb_bins = int(numpy.ceil(radii.max()))
histo_range = [0, nb_bins]
# TODO : compute the histogram of the radii distribution
# ...

# TODO : plot the histogram into a Plot1D widget
# ...


# ### compute azimutal integration
# 
# goal : get the mean contribution of each pixels for each radius

# step 1 : get the contribution of each pixels for each radius

nb_bins = int(numpy.ceil(radii.max()))
histo_range = [0, nb_bins]
# TODO : compute the weighted histogram of the contribution of pixel for each radius
# ...


# step 2 : get the mean and plot it
# 

# TODO : display the histogram, the weighted_histogram and the normalized histogram (weighted_histogram/histogram)
# into a Plot1D widget
# ...


# # Exercice : compute the azimutal integration over n images
# we want to reproduced the same action but over a stack of image :
#     - pixel distance two the center is not evolving
#     - only pixel values are

dataset = [ createDataSet() for i in range(10) ]


# ## First way : using Histogramnd

def computeDataSetHisto():
    # TODO : create the function returning the histogram accumulating the contribution
    # of pixels for all images in the dataset using Histogramnd
    # ...
    pass


# plot It
# plotDataSetHistoNd = Plot1D()
# histogramDS = computeDataSetHisto()
# binscenter=(histogramDS.edges[0][1:] + histogramDS.edges[0][0:-1]) / 2.0
# plotDataSetHistoNd.addCurve(x=binscenter, y=histogramDS.weighted_histo/histogramDS.histo, color='red')
# plotDataSetHistoNd.show()


# ## second way : using HistogramndLut

# In[ ]:

def computeDataSetHistoLut():      
    # TODO : create the function returning the histogram accumulating the contribution
    # of pixels for all images in the dataset using HistogramndLut
    # ...
    pass


# In[ ]:

# plot It
# plotDataSetHistoLut = Plot1D()
# histogramLut = computeDataSetHistoLut()
# plotDataSetHistoLut.addCurve(binscenter, y=histogramLut.weighted_histo()/histogramDS.histo, color='red')
# plotDataSetHistoLut.show()

app.exec_()