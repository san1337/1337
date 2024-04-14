from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QListWidget, QVBoxLayout, QHBoxLayout,QFileDialog 

app = QApplication([])
win = QWidget()
win.resize(700, 500)
win.setWindowTitle('Easy Editor')






okno = QLabel('Добро пожаловать, в игру:Камень,ножницы, бумага')

left_btn = QPushButton('запуск игры')
right_btn = QPushButton('выключение игры')
mirror_btn = QPushButton('счёт')
blur_btn = QPushButton('бумага')
bw_btn = QPushButton('ножницы')
kam_btn = QPushButton('камень')




btns_line = QHBoxLayout()
main_line = QHBoxLayout()
v_line1 = QVBoxLayout()
v_line2 = QVBoxLayout()



btns_line.addWidget(left_btn)
btns_line.addWidget(right_btn)
btns_line.addWidget(mirror_btn)
btns_line.addWidget(blur_btn)
btns_line.addWidget(bw_btn)
btns_line.addWidget(kam_btn)
v_line2.addWidget(okno)






v_line2.addLayout(btns_line)

main_line.addLayout(v_line1, 20)
main_line.addLayout(v_line2, 80)
win.setLayout(main_line)
win.show()
app.exec_()
