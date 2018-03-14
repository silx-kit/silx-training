
import silx.io
from silx.math.fit import leastsq
from silx.math.fit.functions import sum_gauss
from silx.math.fit.peaks import peak_search, guess_fwhm

from numpy.linalg.linalg import LinAlgError

with silx.io.open("data/31oct98.dat") as specfile:
    for scan in ["21.1", "22.1", "23.1", 
                 "24.1", "25.1", "26.1",
                 "27.1"]:
        measurement_group = specfile["/" + scan + "/measurement"]
        xdata = measurement_group["TZ3"]
        ydata = measurement_group["If2"]

        guessed_fwhm = guess_fwhm(ydata)
        peaks_indices = peak_search(ydata, guessed_fwhm)

        positions = [xdata[int(i)] for i in peaks_indices]
        heights = [ydata[int(i)] for i in peaks_indices]
         
        estimated_params = []
        for h, p in zip(heights, positions):
            estimated_params += [h, p, guessed_fwhm]
        
        try:
            fitted_params, cov_matrix = leastsq(model=sum_gauss, 
                                                xdata=xdata, ydata=ydata, 
                                                p0=estimated_params)
        except LinAlgError:
            print("Unable to fit scan %s" % scan)
        else:
            print("Fit results for scan %s:" % scan)
            for i in range(len(fitted_params) // 3):
                h, p, fwhm = fitted_params[3*i:3*i+3]
                print("\tPeak %d: heigth %f, position %f, fwhm %f" % (i, h, p, fwhm))
