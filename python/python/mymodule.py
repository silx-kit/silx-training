# coding: utf-8

"""This is a simple demonstration library"""

__authors__ = ["Pierre Knobel", "Jerome Kieffer", "Henri Payno",
               "Armando Sole", "Valentin Valls", "Thomas Vincent"]
__date__ = "17/11/2016"
__license__ = "MIT"


def sqrt(x):
    "Return the square root of x"
    return x**0.5


def polynom(a, b, c):
    """Compute the polygon of order two
    :param a:a value of the polynom
    :type a: float
    :param b: b value of the polynom
    :type b: float
    :param c: c value of the polynom
    :type c: float """
    delta = pow2(b) - 4.0 * a * c
    solutions = []
    if delta > 0:
        solutions.append((-b + sqrt(delta)) / (2.0 * a))
        solutions.append((-b - sqrt(delta)) / (2.0 * a))
    elif delta == 0:
        solutions.append(-b/(2.0*a))
    return solutions


def pow2(x):
    """Return the square of x
    :param x: input value
    :type x: float"""
    return x*x


def test():
    """Test the library"""
    assert(pow2(2.0) == 4.0)
    print("All OK")


if __name__ == '__main__':
    print("Running unit tests")
    test()
