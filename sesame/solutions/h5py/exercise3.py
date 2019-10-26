# coding: utf-8

"""
Exercise 3
"""

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



def compute_flatfield(flat1, flat2, coef):
    """
    Compute a new flat field between two provided ones,
    using a linear interpolation.

    A `coef` of 0.0 will return `flat1`,
    a coef of 1.0 will return `flat2`.
    """
    coef = numpy.clip(coef, 0.0, 1.0)
    flat1 = flat1.astype(numpy.float32)
    flat2 = flat2.astype(numpy.float32)
    return flat1 * (1.0 - coef) + flat2 * (coef)


with h5py.File("data/ID16B_diatomee.h5", "r") as h5:

    # Load the data always needed

    dark = h5["/background/0000"][...].astype(numpy.float32)
    flat1 = h5["/flatfield/0000"][...].astype(numpy.float32)
    flat2 = h5["/flatfield/0500"][...].astype(numpy.float32)

    with h5py.File("exercise3.h5", "w") as h5out:

        data_group = h5["/data"]

        # Compute the result image per image

        for name in data_group:
            # Read the raw data
            raw = data_group[name][...]

            # Compute the flat field
            coef = int(name) / 500.0
            flat = compute_flatfield(flat1, flat2, coef)

            # Apply the correction
            normalized = flatfield_correction(raw, flat, dark)

            # Save the result
            h5out[name] = normalized

# Check the saved result
import collections
result = collections.OrderedDict()
with h5py.File("exercise3.h5", "r") as h5out:
    for name in h5out:
        result[name] = h5out[name][...]
imshowmany(result)

