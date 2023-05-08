import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")


    def the_button_was_clicked(self):
        print("Clicked!")



app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
