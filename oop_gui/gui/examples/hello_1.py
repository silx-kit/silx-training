from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout

app = QApplication([])

main_window = QMainWindow()

first_widget = QWidget(parent=main_window)
first_widget.setLayout(QHBoxLayout())

for word in ('hello world !!!'.split(' ')):
    label = QLabel(word, parent=first_widget)
    first_widget.layout().addWidget(label)
main_window.setCentralWidget(first_widget)
main_window.show()
app.exec_()