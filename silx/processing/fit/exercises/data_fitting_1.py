import numpy
from silx.math.fit import leastsq

x = numpy.arange(10).astype(numpy.float64)
y = 0.001 * x**3 + 25.1 * x**2 + 1.2 * x - 25


### TODO: define model function### 
def poly2(x, ...):
    return ...

### TODO: define initial parameters ###
p0 = ...

### TODO: run fit
p, cov_matrix = ...

print("Parameters [a, b, c]: " + str(p))

# 4.
### TODO: print number of iterations and chisq for this fit ###
p, cov_matrix, info = ...
print(...)
print(...)
