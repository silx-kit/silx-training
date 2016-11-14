import numpy
from silx.math.fit import leastsq

x = numpy.arange(10).astype(numpy.float64)
y = 0.001 * x**3 + 25.1 * x**2 + 1.2 * x - 25


def poly2(x, a, b, c):
    return a * x**2 + b*x + c

p0 = [1., 1., 1.]

p, cov_matrix = leastsq(poly2, x, y, p0)

print("Parameters [a, b, c]: " + str(p))

# 4.
p, cov_matrix, info = leastsq(poly2, x, y, p0, full_output=True)
print(info["reduced_chisq"])
print(info["niter"])
