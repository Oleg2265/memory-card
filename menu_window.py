from PyQt5.QtWidgets import *

import database

def menu_window():
    window = QDialog()
    quest_lbl = QLabel("Введіть запитання")
    right_ans_lbl = QLabel("Правильна відповідь")
    quest_edit = QLineEdit()
    right_ans_lbl = QLineEdit()
    add_quest_btn = QPushButton("Добавити питання")





    main_line = QVBoxLayout()
    h1 = QHBoxLayout()
    h1.addWidget(quest_lbl)
    h1.addWidget(quest_edit)
    main_line.addLayout(h1)
    main_line.addWidget(add_quest_btn)

    def add_quest_func():
        a = {
            "Запитання": quest_edit.text(),
            "Правильна відповідь": "apple",
            "Неправильна 1": "жовте",
            "Неправильна 2": "banana",
            "Неправильна 3": "андромеда",
        }
        database.questions.append(a)


    add_quest_btn.clicked.connect(add_quest_func)

    window.setLayout(main_line)
    window.exec()