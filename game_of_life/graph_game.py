import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QLineEdit, QLabel, QWidget, QHBoxLayout
from PyQt6.QtCore import QSize, Qt, QCoreApplication
from subprocess import call
from random import choice
from random import randint
from time import sleep
import game



window_titles = [
    'My App',
    'My App',
    'Still My App',
    'Still My App',
    'What on earth',
    'What on earth',
    'This is surprising',
    'This is surprising',
    'Something went wrong'
]



#with sh.contrib.sudo:
#    print(ls('/root'))

class AnotherWindow(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()

        self.l1 = QVBoxLayout()
        self.l2 = QVBoxLayout()
        self.setFixedSize(QSize(200,150))
        self.line_edit_width = QLineEdit()
        self.line_edit_height = QLineEdit()
        self.label1 = QLabel("Ширина:")
        self.label2 = QLabel("Высота:")
        self.button1 = QPushButton("Применить") 
        
        
        self.button1.clicked.connect(self.exit)


        self.l1.addWidget(self.label1)
        self.l1.addWidget(self.line_edit_width)
        self.l2.addWidget(self.label2)
        self.l2.addWidget(self.line_edit_height)
        self.layout.addLayout(self.l1)
        self.layout.addLayout(self.l2)
        self.layout.addWidget(self.button1)
        self.setLayout(self.layout)
    
    def exit(self):
        global cols, rows
        
        cols = int(self.line_edit_width.text())
        rows = int(self.line_edit_height.text())


        self.close()

# Подкласс QMainWindow для настройки главного окна приложения
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Клеточный автомат")
        # Создали 2 кнопки
        self.button_start = QPushButton("Старт")
        self.button_setting = QPushButton("Настройки") 
        self.button_exit = QPushButton("Выход") 
        # self.label = QLabel()
        self.setFixedSize(QSize(400, 150)) # неизменяемый размер окна
        # self.input = QLineEdit()
        # self.input.textChanged.connect(self.label.setText) # подключение виджетов друг к другу напрямую
        self.mainlayout = QVBoxLayout()
        # self.hlayout = QHBoxLayout()
        # layout.addWidget(self.input)
        # self.hlayout.addWidget(self.button_start)
        # self.hlayout.addWidget(self.button_setting)
        # self.mainlayout.addLayout(self.hlayout)
        self.mainlayout.addWidget(self.button_start)
        self.mainlayout.addWidget(self.button_setting)
        self.mainlayout.addWidget(self.button_exit)
        # with open('/sys/class/backlight/intel_backlight/max_brightness', 'r') as fi:
        #     self.maxbn = int(fi.read().strip()) # читаем максимальную яркость
        #     self.label.setText(str(self.maxbn))
        self.button_start.clicked.connect(self.start)
        self.button_setting.clicked.connect(self.setting)
        self.button_exit.clicked.connect(self.exit)
        #self.setMouseTracking(True)
        #self.label.setMouseTracking(True)
        #self.button_is_checked = True  # don't use for now
        self.container = QWidget()
        #self.container.setMouseTracking(True) # Чтобы события клика, перемещания и двойного клика регистрировались без зажатой кнопки мыши
        self.container.setLayout(self.mainlayout)
        self.setCentralWidget(self.container)
        #self.setCentralWidget(self.label)
        #self.setCentralWidget(self.label)
        #self.button.setCheckable(True) # убираю необходимость вручную выключать кнопку
        #self.button.setChecked(self.button_is_checked)
        #self.button.released.connect(self.the_button_was_released) # если кнопка отпущена
        #self.windowTitleChanged.connect(self.the_window_title_changed) # пoлключаем сигнал, который будет происходить при изменении заголовка окна
        # сигнал выше срабатывает только когда заголовок отличен от предыдущего 
        #self.setMaximumSize(QSize(400, 300))
        # Устанавливаем центральный виджет Window.
        #self.setCentralWidget(self.button)

    def setting(self, checked):
        self.w = AnotherWindow()
        self.w.show()

    def start(self):
        # print("start ")
        # call('python3 glifeg',shell=True)
        # call(['python3', 'glifeg'])
        game.run(cols=cols, rows=rows)
        # pass

        

    def exit(self):
        # QApplication.quit() 
        # sys.exit( app.exec_() )
        # QApplication.quit()
        # sys.exit(0)
        # QCoreApplication.closeAllWindows()
        # QCoreApplication.quit()
        self.close()



    # 4 - переопределённых метода для работы с мышью
    def mouseMoveEvent(self, event):
        print(event.button())
        self.label = event.position()
        print(event.position().PyQt6)
        #if event.buttons() == Qt.NoButton:
        #    print("Simple mouse motion")
        #elif event.buttons() == Qt.LeftButton:
        #    print("Left click drag")
        #elif event.buttons() == Qt.RightButton:
        #    print("Right click drag")

        #self.setMouseTracking(True)
        #self.label.setText("мышка перемещается")


    def mousePressEvent(self, e):
        #self.label.setText("произошёл клик")
        pass


    def mouseReleaseEvent(self, e):
        #self.label.setText("отпустили мышку")
        pass


    def mouseDoubleClick(self, e):
        #self.label.setText("кликнули двойным щелчком")
        pass



    
    def the_button_was_released(self): # собственно сами слоты(обработчики) сигналов(событий)
        self.button_is_checked = self.button.isChecked()

        print(self.button_is_checked)

    def the_window_title_changed(self, window_title):
        print("Заголовок окна изменён: %s" % window_title)
        if window_title == 'Что-то пошло не так':
            self.button.setDisabled(True)

    def the_button_was_clicked(self):
        print("Кнопка нажата!")

        #self.setWindowTitle("Моя первая программа на PyQt6")
        #self.button.setText("Программа")
        
        new_title = choice(window_titles)
        self.setWindowTitle(new_title)

        #self.button.setEnabled(False)
        

    def the_button_was_toggled(self, checked):
        self.button_is_checked = checked

        print(self.button_is_checked)




if __name__=='__main__':
    cols=rows=10
    app = QApplication(sys.argv) # для передачи аргументов из командной строки
    window = MainWindow() # создание объекта переопределённого объекта класса
    window.show() # по умолчанию окно скрыто - показываем
    app.exec()
    # sys.exit( app.exec() )