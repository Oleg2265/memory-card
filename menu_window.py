from PyQt5.QtWidgets import *

import database

def menu_window():
    window = QDialog()
    quest_lbl = QLabel("Введіть запитання")
    right_ans_lbl = QLabel("Правильна відповідь")
    wrong_ans_lbl = QLabel("Неправильна відповідь")
    wrong_ans_lbl2 = QLabel("Неправильна відповідь")
    wrong_ans_lbl3 = QLabel("Неправильна відповідь")
    quest_edit = QLineEdit()
    right_ans_lbl1 = QLineEdit()
    non_right_ans = QLineEdit()
    non_right_ans2 = QLineEdit()
    non_right_ans3 = QLineEdit()
    add_quest_btn = QPushButton("Добавити питання")
    add_right_ans_btn = QPushButton("Добавити питання")
    add_wrong_ans_btn = QPushButton("додати не правильну відповідь")
    add_wrong_ans_btn2 = QPushButton("додати не правильну відповідь")
    add_wrong_ans_btn3 = QPushButton("додати не правильну відповідь")

    main_line = QVBoxLayout()
    h1 = QHBoxLayout()

    h1.addWidget(quest_lbl)
    h1.addWidget(quest_edit)

    h1.addWidget(right_ans_lbl)
    h1.addWidget(right_ans_lbl1)

    h1.addWidget(wrong_ans_lbl)
    h1.addWidget(non_right_ans)

    h1.addWidget(wrong_ans_lbl2)
    h1.addWidget(non_right_ans2)

    h1.addWidget(wrong_ans_lbl3)
    h1.addWidget(non_right_ans3)




    main_line.addLayout(h1)

    main_line.addWidget(add_quest_btn)



    def add_quest_func():
        a = {
            "Запитання": quest_edit.text(),
            "Правильна відповідь": right_ans_lbl1.text(),
            "Неправильна 1": non_right_ans2.text(),
            "Неправильна 2": non_right_ans.text(),
            "Неправильна 3": non_right_ans3.text(),
        }
        database.questions.append(a)


    add_quest_btn.clicked.connect(add_quest_func)

    window.setLayout(main_line)
    window.exec()