import random

from PyQt5.QtWidgets import *

app = QApplication([])
window = QWidget()
window.resize(700,500)








Menushka = QPushButton("Меню")
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
vidpovid = window.show()












answers = [ans1, ans2, ans3, ans4]
random.shuffle(answers)














main_line = QVBoxLayout()
h1 = QHBoxLayout()
h1.addWidget(Menushka)
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
window.setLayout(main_line)

main_line.addWidget(apple)



korobka.setLayout(group_line)

main_line.addWidget(korobka)

main_line.addWidget(odpovid)

app.exec()
