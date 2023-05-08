import sys
#import sh

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QLineEdit, QLabel, QWidget, QHBoxLayout



from random import choice


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



# Подкласс QMainWindow для настройки главного окна приложения
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        self.button_plus = QPushButton("+")
        self.button_minus = QPushButton("-") 

        self.label = QLabel()

        #self.setFixedSize(QSize(400, 300)) # неизменяемый размер окна
        self.input = QLineEdit()
        #self.input.textChanged.connect(self.label.setText) # подключение виджетов друг к другу напрямую
        self.mainlayout = QVBoxLayout()
        self.hlayout = QHBoxLayout()
        #layout.addWidget(self.input)
        self.hlayout.addWidget(self.start_game)
        self.hlayout.addWidget(self.setting_game)


        self.mainlayout.addLayout(self.hlayout)
        self.mainlayout.addWidget(self.input)
        self.mainlayout.addWidget(self.label)

        with open('/sys/class/backlight/intel_backlight/max_brightness', 'r') as fi:
            self.maxbn = int(fi.read().strip()) # читаем максимальную яркость
            self.label.setText(str(self.maxbn))


        self.button_plus.clicked.connect(self.plus)
        self.button_minus.clicked.connect(self.minus)







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


    def start_game(self):
        inc = 100

        for _ in range(100):
            print(123)



        print("some thing's")
        # with open('/sys/class/backlight/intel_backlight/brightness', 'r+') as f:
        #     bn = f.read().strip()
            
        #     f.seek(0)
        #     self.value = int(bn)
        #     self.value += inc

        #     if self.value <= self.maxbn:
        #         f.write(str(self.value))


        print(self.value)

    def setting_game(self):
        dec = 100 


        print(dec)


        print("Hello Anime")


        print("TEST")
        # with open('/sys/class/backlight/intel_backlight/brightness', 'r+') as f:
        #     bn = f.read().strip()

        #     f.seek(0)
        #     self.value = int(bn)
        #     self.value -= dec 

        #     if self.value >= 100:
        #         f.write(str(self.value))

        # print(self.value)





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






app = QApplication(sys.argv) # для передачи аргументов из командной строки

window = MainWindow() # создание объекта переопределённого объекта класса

window.show() # по умолчанию окно скрыто - показываем

app.exec()
