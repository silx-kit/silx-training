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


from PyQt5 import Qt


class IntLineEdit(Qt.QLineEdit):
    """LineEdit widget for integer

    :param Union[int,None] bottom: Minimum of accepted range
    :param Union[int,None] top: Maximum of accepted range
    :param QWidget parent:
    """
    def __init__(self, parent=None, bottom=None, top=None):
        super(IntLineEdit, self).__init__(parent)
        validator = Qt.QIntValidator(self)
        if bottom is not None:
            validator.setBottom(bottom)
        if top is not None:
            validator.setTop(top)
        self.setValidator(validator)
        self.editingFinished.connect(self._cleanDisplayedValue)

    def _defaultValue(self):
        """Returns a default value based on bottom and top"""
        bottom = self.validator().bottom()
        if bottom != numpy.iinfo(numpy.int32).min:
            default = bottom
        else:
            top = self.validator().top()
            if top != numpy.iinfo(numpy.int32).max:
                default = top
            else:
                default = 0
        return default

    def _cleanDisplayedValue(self):
        """Remove leading 0 if any"""
        self.setValue(self.value())

    def value(self):
        """Returns the current value

        :rtype: int
        """
        text = self.text()
        if text == '':
            return self._defaultValue()
        else:
            return int(text)

    def setValue(self, value):
        """Set the displayed value

        :param int value:
        """
        self.setText(str(value))

