from silx.math.fit import FitTheory
from silx.math.fit import FitManager

def poly3(x, a, b, c, d):
    return a * x**3 + b * x**2 + c*x + d

my_poly3_theory = FitTheory(function=poly3, parameters=["a", "b", "c", "d"])

fitman = FitManager()
fitman.addtheory("my poly", my_poly3_theory)
fitman.settheory("my poly")

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
print(fitman.chisq)
print(fitman.niter)
