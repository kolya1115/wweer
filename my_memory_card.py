from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QRadioButton, QPushButton, QGroupBox 
from PyQt5.QtCore import Qt

from random import randint,  shuffle

class Question():
    
    def __init__(self, question, correct, wrong1, wrong2, wrong3):
        self.question = question
        self.correct = correct
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

questions = list() 
questions.append(Question('Вопрос 1: Сколько дней в году?',  '365',  '356',  '364', '366'))
questions.append(Question('Вопрос 2: Сколько месяцев в 3 годах?',  '36',  '34',  '31', '38'))      

app = QApplication([]) 
screen = QWidget() 
screen.setWindowTitle('Memory Card') 
screen.resize(400, 200) 
screen.show()

main_lain = QVBoxLayout()

rand = randint(0, len(questions) - 1)

text1 = QLabel(questions[rand].question)

# ======= GROUOBOX (RESULT)
result = QGroupBox('Результат')
result_line = QVBoxLayout()
result_lable = QLabel('')
result_line.addWidget(result_lable, alignment =Qt.AlignCenter)
result.setLayout(result_line)
result.hide()




# ======= GROUPBOX (BUTTONS)
buttons = QGroupBox('Варианты ответов')

h_line = QHBoxLayout()
v_line1 = QVBoxLayout()
v_line2 = QVBoxLayout()

button1 = QRadioButton(questions[rand].correct)
button2 = QRadioButton(questions[rand].wrong1)
button3 = QRadioButton(questions[rand].wrong2)
button4 = QRadioButton(questions[rand].wrong3)

buttons_list = list()
buttons_list.append(button1)
buttons_list.append(button2)
buttons_list.append(button3)
buttons_list.append(button4)
shuffle(buttons_list)

v_line1.addWidget(buttons_list[0])
v_line1.addWidget(buttons_list[1])
v_line2.addWidget(buttons_list[2])
v_line2.addWidget(buttons_list[3])

h_line.addLayout(v_line1)
h_line.addLayout(v_line2)


buttons.setLayout(h_line)
main_lain.addWidget(text1, alignment =Qt.AlignCenter)
main_lain.addWidget(result)
main_lain.addWidget(buttons, alignment =Qt.AlignCenter)

button5 = QPushButton('Ответить')
main_lain.addWidget(button5, alignment =Qt.AlignCenter)

screen.setLayout(main_lain)

def show_result():
    global if_correct
    buttons.hide()
    if is_correct:
        result_lable.setText('Абсолютно верно')
    else:
        result_lable.setText('Неверно')
    result.show()

def check_answer_func():
    global rand, buttons_list, is_correct
    if button5.text() == 'Ответить':
        button5.setText('Следующий вопрос')
        for i in buttons_list:
            if i.isChecked():
                if i.text() == questions[rand].correct:
                    is_correct = True
                else:
                    is_correct = False     
        show_result()
    elif button5.text() == 'Следующий вопрос':
        button5.setText('Ответить')
        is_correct = False
        rand = randint(0, len(questions) - 1)
        text1.setText(questions[rand].question)
        button1.setText(questions[rand].correct)
        button2.setText(questions[rand].wrong1)
        button3.setText(questions[rand].wrong2)
        button4.setText(questions[rand].wrong3)
        buttons_list = list()
        buttons_list.append(button1)
        buttons_list.append(button2)
        buttons_list.append(button3)
        buttons_list.append(button4)
        for i in buttons_list:
            i.setAutoExclusive(False)
            i.setChecked(False)
        for i in buttons_list:
            i.setAutoExclusive(True)
        shuffle(buttons_list)
        v_line1.addWidget(buttons_list[0])
        v_line1.addWidget(buttons_list[1])
        v_line2.addWidget(buttons_list[2])
        v_line2.addWidget(buttons_list[3])

        result.hide()
        buttons.show()


        
button5.clicked.connect(check_answer_func)

app.exec_()