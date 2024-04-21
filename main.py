from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QListWidget, QVBoxLayout, QHBoxLayout,QFileDialog 

app = QApplication([])
win = QWidget()
win.resize(700, 500)
win.setWindowTitle('Easy Editor')






okno = QLabel('Добро пожаловать, в игру:Камень,ножницы, бумага')
schet = QLabel('Счёт')



bum_btn = QPushButton('бумага')
nsh_btn =  QPushButton('ножницы')
kam_btn = QPushButton('камень')




btns_line = QVBoxLayout()
main_line = QVBoxLayout()
v_line1 = QVBoxLayout()
v_line2 = QVBoxLayout()





btns_line.addWidget(bum_btn)
btns_line.addWidget(nsh_btn)
btns_line.addWidget(kam_btn)
v_line2.addWidget(okno)
v_line1.addWidget(schet)






v_line2.addLayout(btns_line)

main_line.addLayout(v_line1, 20)
main_line.addLayout(v_line2, 80)
win.setLayout(main_line)
win.show()
app.exec_()
