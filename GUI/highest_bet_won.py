import json
import sys, os
from PyQt5.QtWidgets import QApplication, QMainWindow ,QPushButton,QLineEdit,QLabel
from PyQt5.QtCore import Qt, pyqtSignal, QEventLoop



file_path= "highscore.json"


reset ={"name" : 0}

class HighscoreWindow(QMainWindow):
    closed = pyqtSignal() #pyqtSignal is used to send a signal to the main window when the highscore window is closed ( this helps the other thread to know that the highscore window is closed and it can continue)

    def __init__(self):  
        super().__init__()   
        self.name = ""
        self.setGeometry(600, 400, 600, 600)
        self.lable = QLabel("you broke the record",self)
        self.lable.setGeometry(0,0,600,70)
        self.lable.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.lable.setStyleSheet("font-size: 40px;"
                                "background-color: silver;"
                                "Color : black")

        self.line = QLineEdit(self)
        self.line.setGeometry(150,70,300,50)
        self.line.setStyleSheet("font-size: 20px;"
                                "background-color: white;"
                                "Color : black")
        self.line.setPlaceholderText("Enter ur name ")
        self.line.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        self.button = QPushButton("submmit", self)
        self.button.setGeometry(200,130,200,50)
        self.button.setStyleSheet("font-size: 20px;"
                                "background-color: grey;"
                                "Color : white")
        self.button.clicked.connect(self.onClick)

    def onClick(self):
        self.name = self.line.text()
        self.close()
        
    def show_name(self):
        return self.name 

#
    def closeEvent(self, event):
        self.closed.emit() #emit is used to send the signal
        event.accept() # event.accept() is used to accept the event and close the window

        


def load_high_score():
    default_score = {"name": 0}
    try:
        with open(file_path, 'r') as file:
            high_score = json.load(file)
            if not isinstance(high_score, dict) or not high_score:
                raise ValueError("Invalid format")
            return high_score
    except (FileNotFoundError, json.JSONDecodeError, ValueError):
        try:
            with open(file_path, "w") as file:
                json.dump(default_score, file, indent=4)
        except Exception:
            pass
        return default_score


def write_high_score(score):
    high_score = load_high_score()

    for i in high_score.values():

            if int(i) < int(score):

                app = QApplication.instance() #this is to prevent the error of creating multiple instances of the application
                if not app: #if there is no instance of the application, create one
                    app = QApplication(sys.argv)  
                window = HighscoreWindow()  
                window.show()  
                
                loop = QEventLoop() #this is to prevent the error of creating multiple instances of the application
                window.closed.connect(loop.quit) # connect the closed signal to the quit method
                loop.exec_() # execute the loop

                name = window.line.text() # get the name from the line edit

                new_high_score = {name : score}
                with open(file_path,"w") as file:
                    json.dump(new_high_score,file,indent=4)
                high_score = new_high_score
                break
            else:
                break

    return high_score        
    
def show_high_score():
    high_score = load_high_score()
    a=list(high_score.values())
    b=list(high_score.keys())
    return f"current high score is {a[0]} by {b[0]}"


def get_data_file_path(filename):
    if getattr(sys, 'frozen', False):
        # Running as bundled exe
        base_dir = os.path.join(os.environ.get('APPDATA', os.path.expanduser('~')), 'SlotMachineV')
        os.makedirs(base_dir, exist_ok=True)
        return os.path.join(base_dir, filename)
    else:
        # Running as script
        return filename

# Then replace every occurrence of "highscore.json" with:
file_path = get_data_file_path("highscore.json")

        

def main():
    
    high_score = {"name": 0}
    
    try:
        with open(file_path,"x") as file:
            json.dump(high_score,file,indent=4)
    except FileExistsError:
        pass


    score = input("enter your score ")
    print(write_high_score(score))
    print(show_high_score())




if __name__ == "__main__":  
    main()

