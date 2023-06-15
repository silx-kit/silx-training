def is_power_of_two(value):
   """Returns True if value is a power of two.

   It supports numpy array of int of any dimensions and returns
   an array of bool of same dimensions.

   Limitation: Returns True for 0.
   """
   return (value & (value - 1)) == 0
