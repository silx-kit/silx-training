"""This module provides a pseudo-random generator."""  # Module docstring


import numpy


DEFAULT_SHIFTS = 13, 17, 5
"""Default triple for xorshift32."""  # Attribute docstring


def random_xorshift32(
    last_value: numpy.uint32, shifts: tuple[int, int, int]=None
) -> numpy.uint32:
    """Returns the next pseudo-random uint32 given previous value and shifts

    See Marsaglia, G. Xorshift RNGs: http://www.jstatsoft.org/v08/i14/paper

    :param last_value: Previously returned number or the seed.
    :param shift_triple: Bit shifts to use.
    :return: The generated random number.
    :raises ValueError: if x is not a numpy.uint32
    """  # Function docstring

    x = numpy.uint32(last_value)  # Work with 32bits integer
    a, b, c = shifts or XORSHIFT32_DEFAULT_SHIFTS
    x ^= x << a
    x ^= x >> b
    x ^= x << c
    return x


class RandomGenerator32:
    """Xorshift-based uint32 pseudo-random generator."""  # Class docstring

    DEFAULT_SHIFTS = 13, 17, 5
    """The default triple of shift."""  # Attribute docstring

    def __init__(self, seed, triple=None):
        """Initialize generator with the given seed.

        A triple for xorshift can be added.
        """

        self.triple = triple or self.DEFAULT_SHIFTS
        """The triple used by the instance."""  # Attribute docstring

        self._seed = numpy.uint32(seed)
        self._last_rand = self._seed

    def rand(self):
        """Returns a pseudo-random integer."""  # Method doctring

        self._last_rand = xorshift32(self._last_rand, self.triple)
        return self._last_rand

    @property
    def seed(self):
        """The initialization seed (read-only)."""  # Property docstring

        return self._seed
