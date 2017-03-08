
import contextlib
import sys
import unittest


# Parametric Test Base Class ##################################################

if sys.hexversion >= 0x030400F0:  # Python >= 3.4
    class ParametricTestCase(unittest.TestCase):
        pass

else:
    class ParametricTestCase(unittest.TestCase):
        """TestCase with subTest support for Python < 3.4.
    
        Add subTest method to support parametric tests.
        API is the same, but behavior differs:
        If a subTest fails, the following ones are not run.
        """

        _subTestMsg = None  # Class attribute to provide a default value

        @contextlib.contextmanager
        def subTest(self, msg=None, **params):
            """Use as unittest.TestCase.subTest method in Python >= 3.4."""
            # Format arguments as: '[msg] (key=value, ...)'
            paramStr = ', '.join(['%s=%s' % (k, v) for k, v in params.items()])
            self._subTestMsg = '[%s] (%s)' % (msg or '', paramStr)
            yield
            self._subTestMsg = None

        def shortDescription(self):
            shortDesc = super(ParametricTestCase, self).shortDescription()
            # Append subTest message to shortDescription
            desc = ' '.join(
                [msg for msg in (shortDesc, self._subTestMsg) if msg])

            return desc if desc else None
