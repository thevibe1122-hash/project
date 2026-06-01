# Gui sm
import sys  
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel ,QPushButton,QLineEdit
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QIcon, QFont
from cash_back import *
import time
import random

class MainWindow(QMainWindow):
    def __init__(self):  
        super().__init__()  
        self.setWindowTitle("Slot Machine V") 
        self.setGeometry(600, 400, 900, 600)
        self.balance=100
        self.bet = 0
        self.betted = 0
        self.lable5=QLabel("",self)

        

        self.label0 =QLabel("Welcom to salah's casino!",self)
        self.label2=QLabel("$$$",self)

        self.label1=QLabel(f"{self.balance}$",self)
        self.label3=QLabel("",self)
        self.line = QLineEdit("10",self)
        self.lable4 = QLabel(f"{0:.2f}",self)

        
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_spin)
        self.spin_count = 0
        self.InitGUI()
        self.setWindowIcon(QIcon("C:/Users/user/Downloads/download.png"))

    def InitGUI(self):
        self.button = QPushButton("spin",self)
        self.button.setGeometry(699,300,130,40)
        self.button.setStyleSheet("font-size: 20x;"
                            "background-color : grey;"
                            "Color : white")
        self.button.clicked.connect(self.onClick) # connect the button to the onClick function
        self.lable5.setGeometry(0,0,900,600)
        self.label0.setGeometry(0,0,900,100)
        self.label1.setGeometry(775,20,100,50)
        self.label2.setGeometry(250,150,400,300)
        self.line.setGeometry(0,100,100,40)
        self.label2.setStyleSheet("font-size: 60px;"
                            "background-color: silver;"
                            "Color : Green;"
                            "border: 10px solid grey;" #add border
                            "border-radius: 15px;")#curved border
        self.label3.setGeometry(0,500,900,100)
        self.lable4.setGeometry(800,100,100,40)

        self.label1.setStyleSheet("font-size: 30px;"
                            "background-color: black;"
                            "border: 5px solid grey;"
                            "border-radius: 15px;"
                            "Color : Green")
        
        self.label3.setStyleSheet("font-size: 40px;"
                            "background-color: white;"
                            "Color : Green")
       
        self.lable5.setStyleSheet("font-size: 40px;"
                            "background-color: #11081f;"
                            )
        self.label0.setStyleSheet("font-size: 40px;"
                            "background-color: silver;"
                            "Color : black")
        
        self.lable4.setStyleSheet("font-size: 20px;"
                            "background-color: black;"
                            "border: 5px solid grey;"
                            "Color : Green")

        self.line.setStyleSheet("font-size: 20px;"
                                "background-color: white;"
                                "border: 5px solid grey;"
                                "color: black")
        self.line.setPlaceholderText("Enter ur name")
        
        self.label0.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.label1.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.label2.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.label3.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.line.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.line.textChanged.connect(self.set_bet)
        
    def set_bet(self):
        self.bet = self.line.text()
        if self.bet.isdigit():
            if int(self.bet) > self.balance:
                self.lable4.setText("not enough money")
                self.lable4.setGeometry(720,100,200,40)
                self.betted = 0
                pass
            else:
                self.lable4.setText(f"bet = {int(self.bet)}$")
                self.lable4.setGeometry(785,100,115,40)
                self.betted = int(self.bet)
    
        else:
            self.lable4.setText(f"bet = 0$")
            self.betted = 0
        
    def spin(self):
        self.button.setEnabled(False)
        self.label3.setText("")  # Clear result label while spinning
        self.spin_count = 0
        self.timer.start(100)

    def update_spin(self):
        
        self.symbole = ["🍉","🍋","🔔"]
        self.a = random.choice(self.symbole)
        self.b = random.choice(self.symbole)
        self.c = random.choice(self.symbole)
        self.label2.setText(self.a + self.b + self.c)
        self.label1.setText(f"{self.balance}$")
        self.spin_count += 1

            
        if self.spin_count >= 10:
            self.timer.stop()
            self.button.setEnabled(True)
            
            # Check win/loss condition once the spin finishes
            if self.a == self.b == self.c:
                self.label3.setText("You won! 🎉")
                self.label3.setStyleSheet("font-size: 40px;"
                                "background-color: silver;"
                                "Color : Green")
                self.balance += cash_back(self.a,self.betted)
                self.label1.setText(f"{self.balance}$")

            else:
                self.label3.setText("You lost! 😢")
                self.label3.setStyleSheet("font-size: 40px;"
                                "background-color: silver;"
                                "Color : red")
                
            if self.balance < self.betted:  
                self.line.setText("0")
            
            if self.balance == 0:
                self.button.setText("Restart")
                

            
                                

    def onClick(self):
        balanced = 1
        
        if self.balance <= 0:
                self.button.setText("Spin")
                self.balance = 100
                self.label1.setText(f"{self.balance}$")
                balanced = 0
                self.betted = 10
                self.line.setText("10")
                self.label3.setText("Game restarted")
                self.label3.setStyleSheet("font-size: 40px;"
                                "background-color: silver;"
                                "Color : black")
                pass 
        if self.betted <= 0 and balanced ==1:
            self.label3.setText("bet cannot be 0")
            self.label3.setStyleSheet("font-size: 40px;"
                                "background-color: silver;"
                                "Color : red")
        elif balanced == 0:
            balanced = 1
        else:
            self.spin()
            self.balance -= self.betted
            



def main():
    app = QApplication(sys.argv)  
    window = MainWindow()  
    window.show()  
    sys.exit(app.exec_())

if __name__ == "__main__":  
    main()

