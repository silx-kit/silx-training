# it is not possible to share kernel with ipython so we need to launch it directly from python
from silx.gui import qt
from silx.gui.plot import Plot1D
app = qt.QApplication([])

p=Plot1D()
p.addCurve(range(20), range(20))
p.show()
# then play with the options button

app.exec_()