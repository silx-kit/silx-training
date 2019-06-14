# coding: utf-8
#
# Copyright (c) 2019 European Synchrotron Radiation Facility
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
"""Convert a 2D array to an RGB pixmap"""


import numpy

from PyQt5 import Qt


def gray_log(data):
    """Returns the 2D data converted to an image.

    It uses an autoscale gray colormap and log normalization.

    :param numpy.ndarray data: Data array
    :return: The corresponding RGB image as a pixmap
    :rtype: QPixmap
    """
    # Get strictly positive range
    valid_data = data[numpy.logical_and(numpy.isfinite(data), data > 0.)]
    if valid_data.size:
        min_ = numpy.min(valid_data)
        max_ = numpy.max(valid_data)
    else:  # No finite strictly positive data
        min_ = 1.
        max_ = 10.

    # Log scale normalization
    normalized_data = 255 * ((numpy.log10(data) - numpy.log10(min_)) /
                             (numpy.log10(max_) - numpy.log10(min_)))

    # Convert to grayscale RGB array
    image = numpy.empty(normalized_data.shape + (3,), dtype=numpy.uint8)
    image[:] = normalized_data.astype(numpy.uint8)[..., numpy.newaxis]

    # Convert to QImage
    height, width, depth = image.shape
    qimage = Qt.QImage(
        image.data,
        width,
        height,
        image.strides[0],  # bytesPerLine
        Qt.QImage.Format_RGB888)

    qimage = qimage.copy()  # Making a copy of the image and its data

    # Convert to QPixmap and return
    return Qt.QPixmap.fromImage(qimage)

