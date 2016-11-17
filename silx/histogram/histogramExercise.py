
# coding: utf-8
from silx.gui import qt
global app


def computeradius(data, xcenter, ycenter):
    # TODO
    # ...
    pass


def main():
    # open and show data (convert it to h5 to be loaded)
    dataPath="data/Pilatus1M.hdf5"
    import h5py
    import numpy
    #select the cube values:
    f=h5py.File(dataPath)
    # then select the 'Data/qspace' datagroup (array containing the cubes of the isosurface )
    data=f['data']
    data = numpy.array(data, order='C', dtype='float32')


    ## Plot the data
    from silx.gui.plot import Plot2D

    plot=Plot2D()
    plot.setKeepDataAspectRatio(True)
    colormap = {
        'name': 'inferno',             
        'normalization': 'log',  
        'autoscale': True,       
        'vmin': 0.0,             
        'vmax': 1.0              
     }
    plot.setDefaultColormap(colormap)
    plot.addImage(data)
    plot.show()


    # do the azimutal integration
    radii=computeradius(data, xcenter=180, ycenter=260)


    # TODO create the histogram of the radii
    # ...


    # TODO : display the histogram of radii
    from silx.gui.plot import Plot1D 
    # p=Plot1D()
    # p.addCurve(...)
    # p.show()


    # TODO : compute azimutal integration using weights
    # ...

    # TODO: display the azimutal integration
    # ...

if __name__ == '__main__':
    app=qt.QApplication([])
    main()
    app.exec_()

