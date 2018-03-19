
import silx.io
from silx.math.fit import leastsq
from silx.math.fit.functions import sum_gauss
from silx.math.fit.peaks import peak_search, guess_fwhm

from numpy.linalg.linalg import LinAlgError

with silx.io.open("data/31oct98.dat") as specfile:
    for scan in ["21.1", "22.1", "23.1", 
                 "24.1", "25.1", "26.1",
                 "27.1"]:
        print("Processing scan %s" % scan)
        measurement_group = specfile["/" + scan + "/measurement"]
        xdata = measurement_group["TZ3"][()]
        ydata = measurement_group["If2"][()]

        guessed_fwhm = guess_fwhm(ydata) * ((xdata[-1] - xdata[0]) / len(xdata))
        peaks_indices = peak_search(ydata, guessed_fwhm, sensitivity=10)

        print("\tFound %d peaks" % len(peaks_indices))

        positions = [xdata[int(i)] for i in peaks_indices]
        heights = [ydata[int(i)] for i in peaks_indices]
         
        estimated_params = []
        constraints = []
        for h, p in zip(heights, positions):
            estimated_params += [h, p, guessed_fwhm]
            constraints += [[], [], []]
        
        try:
            fitted_params, cov_matrix = leastsq(model=sum_gauss, 
                                                xdata=xdata, ydata=ydata, 
                                                p0=estimated_params)
        except LinAlgError:
            print("\tUnable to fit the data")
        else:
            print("\tFit results:")
            for i in range(len(fitted_params) // 3):
                h, p, fwhm = fitted_params[3*i:3*i+3]
                print("\t\tPeak %d: heigth %f, position %f, fwhm %f" % (i, h, p, fwhm))
