def poly3(x, a, b, c, d):
    return a * x**3 + b*x**2 + c*x + d

p0 = [1., 1., 1., 1.]

p, cov_matrix = leastsq(poly3, x, y, p0)

print("Parameters [a, b, c, d]: " + str(p))

# 4.
p, cov_matrix, info = leastsq(poly3, x, y, p0, full_output=True)
print(info["reduced_chisq"])
print(info["niter"])
