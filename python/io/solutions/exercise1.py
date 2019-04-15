# coding: utf-8

"""
Exercise 1
"""

import h5py

# Read the data

import numpy

def flatfield_correction(raw, flat, dark):
    """
    Apply a flat-field correction to a raw data using a flat and a dark.
    """
    # Make sure that the computation is done using float
    # to avoid type overflow or lose of precision
    raw = raw.astype(numpy.float32)
    flat = flat.astype(numpy.float32)
    dark = dark.astype(numpy.float32)
    # To the computation
    return (raw - dark) / (flat - dark)

def imshowmany(*args, **kwargs):
    """
    Dispaly as image all array provided as argument.
    
    The image title is defined using the argument name.
    """
    from matplotlib import pyplot
    if len(kwargs) == 0:
        import collections
        kwargs = collections.OrderedDict()
    for i, arg in enumerate(args):
        if isinstance(arg, dict):
            kwargs.update(arg)
        else:
            kwargs["arg" + i]

    fig = pyplot.figure()
    columns = 3
    nbrows = len(kwargs) // columns + 1
    nbcols = len(kwargs) // nbrows
    for i, (key, value) in enumerate(kwargs.items()):
        a = fig.add_subplot(nbrows, nbcols, i + 1)
        imgplot = plt.imshow(value)
        a.set_title(key)




with h5py.File("data/ID16B_diatomee.h5", "r") as h5:
    raw = h5["/data/0000"][...]
    dark = h5["/background/0000"][...]
    flat = h5["/flatfield/0000"][...]

# Compute the result

normalized = flatfield_correction(raw, flat, dark)

# Save the result

with h5py.File("exercise1.h5", "w") as h5out:
    h5out["result"] = normalized

# Check the saved result

with h5py.File("exercise1.h5", "r") as h5out:
    saved = h5out["result"][...]
imshowmany(Before=raw, After=saved)

