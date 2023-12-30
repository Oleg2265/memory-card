import random

import bublik

from PyQt5.QtWidgets import *
import database
import menu_window

app = QApplication([])
window = QWidget()
window.resize(700,500)








Menushka = QPushButton("Меню")
redact_quest = QPushButton("Редактувати питання")
vidpochuty = QPushButton("відпочити")
apple = QLabel("Яблуко")
minutes = QLabel("Хвилини")
korobka = QGroupBox("Варіанти яблук")
ans1 = QRadioButton("Зелене")
ans2 = QRadioButton("Червоне")
ans3 = QRadioButton("жовте")
ans4 = QRadioButton("Андромеда")
spiner = QSpinBox()
odpovid = QPushButton("Відповісти")
next_quest = QPushButton("Наступне питання")
prev_quest = QPushButton("Минуле питання")
vidpovid = window.show()












answers = [ans1, ans2, ans3, ans4]
random.shuffle(answers)














main_line = QVBoxLayout()
h1 = QHBoxLayout()
h1.addWidget(Menushka)
h1.addWidget(redact_quest)
h1.addStretch(1)
h1.addWidget(vidpochuty)
h1.addWidget(spiner)

h1.addWidget(minutes)




group_line = QVBoxLayout()
h2 = QHBoxLayout()
group_line.addLayout(h2)
h3 = QHBoxLayout()
group_line.addLayout(h3)
h2.addWidget(answers[0])
h2.addWidget(answers[1])
h3.addWidget(answers[2])
h3.addWidget(answers[3])




main_line.addLayout(h1)
main_line.addWidget(next_quest)
main_line.addWidget(prev_quest)
window.setLayout(main_line)

main_line.addWidget(apple)


def set_question():
    num = database.question_number
    apple.setText(database.questions[num]["Запитання"])
    answers[0].setText(database.questions[num]["Правильна відповідь"])
    answers[1].setText(database.questions[num]["Неправильна 1"])
    answers[2].setText(database.questions[num]["Неправильна 2"])
    answers[3].setText(database.questions[num]["Неправильна 3"])
set_question()








def next_quest_func():
    database.question_number += 1
    set_question()

def pre_quest_func():
    database.question_number -= 1
    set_question()


def menu_show():
    window.hide()
    menu_window.menu_window()
    window.show()

def redact_show():
    window.hide()
    bublik.change_quest_window()
    window.show()
    set_question()

Menushka.clicked.connect(menu_show)

redact_quest.clicked.connect(redact_show)




next_quest.clicked.connect(next_quest_func)
prev_quest.clicked.connect(pre_quest_func)


korobka.setLayout(group_line)

main_line.addWidget(korobka)

main_line.addWidget(odpovid)

app.exec()
