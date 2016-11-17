
import numpy
from silx.math.fit import leastsq

from silx.math.fit import FitTheory
from silx.math.fit import FitManager

x = numpy.arange(10).astype(numpy.float64)
y = 0.001 * x**3 + 25.1 * x**2 + 1.2 * x - 25

# TODO: define a degree-3 polynome function
def poly3(...):
    return ...

# TODO: create a FitTheory
my_poly3_theory = FitTheory(...)

fitman = FitManager()
# TODO: add the new theory to fitman, select it
...


fitman.setdata(x, y)

# FitManager.estimate() returns an array of initial parameters
p0 = fitman.estimate()
# ... and as we didn't define an estimation function, it will be an array of ones.
print("Estimated parameters: ", p0)

# FitManager.runfit() returns the same data as leastsq(..., full_output=True) 
p, cov, info = fitman.runfit()

print("Parameters [a, b, c, d]: " + str(p))

for param in fitman.fit_results:
    print("parameter %s: %f" % (param["name"], param["fitresult"]))

# 4.

# TODO: print chisq and niter, by finding them in fitman's attributes
...
