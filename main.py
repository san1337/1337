from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QListWidget, QVBoxLayout, QHBoxLayout,QFileDialog
import random 

app = QApplication([])
win = QWidget()
win.resize(700, 500)
win.setWindowTitle('Easy Editor')
st = 0
sb = 0





okno = QLabel('Добро пожаловать, в игру:Камень,ножницы, бумага')
schet = QLabel('Счёт: ' + str(st))
schet2 =QLabel('Счёт соперника : ' + str(sb))



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


list_play = ['Камень', 'Ножницы', 'Бумага']
def paper():
    global st
    global sb
    rand = random.choice(list_play)
    if rand == 'Камень':
        okno.setText('Выбор компьютера: ' + rand + '. Ваш выбор: бумага. Вы победили!')
        st+=1
        schet.setText('Счёт: ' + str(st))
    if rand == 'Ножницы':
        okno.setText('Выбор компьютера: ' + rand + '. Ваш выбор: бумага. Вы проиграли!')
        sb+=1
        schet.setText('Счёт: ' + str(st))
    if rand == 'Бумага':
        okno.setText('Выбор компьютера: ' + rand + '. Ваш выбор: бумага. У вас с соперником ничья!')


        








bum_btn.clicked.connect(paper)


def  scissors():
    rand = random.choice(list_play)
    okno.setText('Выбор компьютера: ' + rand + '. Ваш выбор: ножницы')


nsh_btn.clicked.connect(scissors)

def stone():
    rand = random.choice(list_play)
    okno.setText('Выбор компьютера: ' + rand + '. Ваш выбор: камень')


kam_btn.clicked.connect(stone)



win.show()
app.exec_()
