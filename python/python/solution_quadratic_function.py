# coding: utf-8

"""
Contain solution for the quadratic equation exercise
"""

__authors__ = [
    "Pierre Knobel",
    "Jerome Kieffer",
    "Henri Payno",
    "Pierre Paleo",
    "Armando Sole",
    "Valentin Valls",
    "Thomas Vincent",
]
__date__ = "18/09/2018"
__license__ = "MIT"


def sqrt(x):
    """Return square root of x"""
    return x ** (0.5)


def polynom(a, b, c):
    """Compute solutions for the quadratic equation a*x^2 + b*x + c = 0"""
    delta = b * b - 4.0 * a * c

    if delta < 0:
        return []

    if delta == 0:
        return [-b / (2.0 * a)]

    return [(-b - sqrt(delta)) / (2.0 * a), (-b + sqrt(delta)) / (2.0 * a)]
