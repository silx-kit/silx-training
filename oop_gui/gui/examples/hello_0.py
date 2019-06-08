from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow

app = QApplication([])

main_window = QMainWindow()

first_widget = QLabel('hello world !!!', parent=main_window)
main_window.setCentralWidget(first_widget)
main_window.show()
app.exec_()