from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QListWidget, QVBoxLayout, QHBoxLayout
import random 
from time import sleep

app = QApplication([])
win = QWidget()
win.resize(700, 500)
win.setWindowTitle('Easy Editor')
st = 0
sb = 0
och = 0





okno = QLabel('Добро пожаловать, в игру:Камень,ножницы, бумага')
schet = QLabel('Счёт: ' + str(st))
ochi =  QLabel('Очки:' +str(och))
schet2 = QLabel('Счёт соперника : ' + str(sb))
magas = QPushButton('Магазин:')



bum_btn = QPushButton('бумага')
nsh_btn =  QPushButton('ножницы')
kam_btn = QPushButton('камень')
kir_btn = QPushButton('кирка')
kir_btn.hide()



btns_line = QVBoxLayout()
main_line = QVBoxLayout()
v_line1 = QVBoxLayout()
v_line2 = QVBoxLayout()





btns_line.addWidget(bum_btn)
btns_line.addWidget(nsh_btn)
btns_line.addWidget(kam_btn)
btns_line.addWidget(kir_btn)

v_line2.addWidget(okno)
v_line1.addWidget(schet)
v_line1.addWidget(ochi)
v_line1.addWidget(schet2)
v_line1.addWidget(magas)








v_line2.addLayout(btns_line)

main_line.addLayout(v_line1, 20)
main_line.addLayout(v_line2, 80)
win.setLayout(main_line)


list_play = ['Камень', 'Ножницы', 'Бумага']
def paper():
    global st
    global sb
    global och
    sleep(3)
    rand = random.choice(list_play)
    if rand == 'Камень':
        okno.setText('Выбор компьютера: ' + rand + '. Ваш выбор: бумага. Вы победили!')
        st+=1
        och+=5
        schet.setText('Счёт: ' + str(st))
        schet2.setText('Счёт соперника: ' + str(sb))
        ochi.setText('Очки:' +str(och))
        
    if rand == 'Ножницы':
        okno.setText('Выбор компьютера: ' + rand + '. Ваш выбор: бумага. Вы проиграли!')
        sb+=1
        och-=2
        schet.setText('Счёт: ' + str(st))
        schet2.setText('Счёт соперника: ' + str(sb))
        ochi.setText('Очки:' +str(och))
    if rand == 'Бумага':
        okno.setText('Выбор компьютера: ' + rand + '. Ваш выбор: бумага. У вас с соперником ничья!')




bum_btn.clicked.connect(paper)





def  scissors():
    global st
    global sb
    global och
    sleep(3)
    rand = random.choice(list_play)
    print(rand)
    if rand == 'Бумага':
        okno.setText('Выбор компьютера: ' + rand + '. Ваш выбор: ножницы. Вы победили!')
        st+=1
        och+=5
        schet.setText('Счёт: ' + str(st))
        schet2.setText('Счёт соперника: ' + str(sb))
        ochi.setText('Очки:' +str(och))
    if rand == 'Камень':
        okno.setText('Выбор компьютера: ' + rand + '. Ваш выбор: ножницы. Вы проиграли!')
        sb+=1
        och-=2
        schet.setText('Счёт: ' + str(st))
        schet2.setText('Счёт соперника: ' + str(sb))
        ochi.setText('Очки:' +str(och))
    if rand == 'Ножницы':
        okno.setText('Выбор компьютера: ' + rand + '. Ваш выбор: ножницы. У вас с соперником ничья!')


nsh_btn.clicked.connect(scissors)


def stone():
    global st
    global sb
    global och
    sleep(3)
    rand = random.choice(list_play)
    if rand == 'Ножницы':
        okno.setText('Выбор компьютера: ' + rand + '. Ваш выбор: камень. Вы победили!')
        st+=1
        och+=5
        schet.setText('Счёт: ' + str(st))
        schet2.setText('Счёт соперника: ' + str(sb))
        ochi.setText('Очки:' +str(och))
    if rand == 'Бумага':
        okno.setText('Выбор компьютера: ' + rand + '. Ваш выбор: камень. Вы проиграли!')
        sb+=1
        och-=2
        schet.setText('Счёт: ' + str(st))
        schet2.setText('Счёт соперника: ' + str(sb))
        ochi.setText('Очки:' +str(och))
    if rand == 'Камень':
        okno.setText('Выбор компьютера: ' + rand + '. Ваш выбор: камень. У вас с соперником ничья!')


kam_btn.clicked.connect(stone)


def kirka():
    global st
    global sb
    global och
    sleep(3)
    rand = random.choice(list_play)
    if rand == 'Ножницы':
        okno.setText('Выбор компьютера: ' + rand + '. Ваш выбор: кирка. Вы победили!')
        st+=1
        och+=5
        schet.setText('Счёт: ' + str(st))
        schet2.setText('Счёт соперника: ' + str(sb))
        ochi.setText('Очки:' +str(och))
    if rand == 'Бумага':
        okno.setText('Выбор компьютера: ' + rand + '. Ваш выбор: кирка. Вы проиграли!')
        sb+=1
        och-=2
        schet.setText('Счёт: ' + str(st))
        schet2.setText('Счёт соперника: ' + str(sb))
        ochi.setText('Очки:' +str(och))
        kir_btn.hide()
    if rand == 'Камень':
        okno.setText('Выбор компьютера: ' + rand + '. Ваш выбор: кирка. Вы победили')
        st+=1
        och+=5
        schet.setText('Счёт: ' + str(st))
        schet2.setText('Счёт соперника: ' + str(sb))
        ochi.setText('Очки:' +str(och))


kir_btn.clicked.connect(kirka)

win2 = QWidget()


kir=QLabel('Кирка: стоит 10 очков')
kyp=QPushButton ('Купить')

kir_line = QVBoxLayout()
kir_line.addWidget(kir)
kir_line.addWidget(kyp)

win2.setLayout(kir_line )





def magaz():
    win2.show()


magas.clicked.connect(magaz)

def buy_kir():
    global och
    if och >= 10:
        och -= 10
        ochi.setText('Очки: ' + str(och))
        kir_btn.show()
kyp.clicked.connect(buy_kir)


win.show()
app.exec_()
