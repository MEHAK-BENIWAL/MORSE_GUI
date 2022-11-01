from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QPushButton, QWidget, QLabel, QLineEdit,QVBoxLayout
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from time import sleep # Import the sleep function from the time module
import sys

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW) # Set pin 8 to be an output pin and set initial value to low (off)

button1 = 10
button2 = 12
button3 = 13
same_delay = 1  #one unit delay
letter_delay = 3*same_delay  #three unit delay
space_delay = 7*same_delay   #seven unit delay
next_line = 10*same_delay
letter_delay -= same_delay  #to account for delay in interpret function.

morseCode = {           #dictionary to store morse codes for various alphabets
    "a": "1233",
    "b": "2111",
    "c": "2121",
    "d": "2113",
    "e": "1333",
    "f": "1121",
    "g": "2213",
    "h": "1111",
    "i": "1133",
    "j": "1222",
    "k": "2123",
    "l": "1211",
    "m": "2233",
    "n": "2133",
    "o": "2223",
    "p": "1221",
    "q": "2212",
    "r": "1213",
    "s": "1113",
    "t": "2333",
    "u": "1123",
    "v": "1112",
    "w": "1223",
    "x": "2112",
    "y": "2122",
    "z": "2211",
    " ": "4333",
    # ".": "",
}

def letter(morseT):
    for i in range(0, len(morseT)):
        interpret(morseT[i])
def dot():
    print("dot")
    GPIO.output(button1, 1)
    sleep(same_delay)
    GPIO.output(button1, 0)
def dash():
    print("dash")
    GPIO.output(button1, 1)
    sleep(same_delay)    
    GPIO.output(button1, 0)

def interpret(i):
    if(i == '1'):
        dot()
        sleep(same_delay)
  
    elif(i == '2'):
        dash()
        sleep(same_delay)

    elif(i == '4'):
        sleep(space_delay)    #for space between names;

    else: pass

#Defining functions to toggle leds
def button1Press():
    print("Button1")
    textboxValue = textbox.text()
    blink_array(textboxValue)
    # GPIO.output(button1, not GPIO.input(button1))
# def button2Press():
#     print("Bitton2")
#     GPIO.output(button2, not GPIO.input(button2))
# def button3Press():
#     print("Button3")
#     GPIO.output(button3, not GPIO.input(button3))
def exit():
    print("Exit")
    GPIO.cleanup()

def blink_array(nameString):
    for i in range(0, len(nameString)):
        write_letter(nameString[i])

def write_letter(charr):
    letter(morseCode.get(charr))
        

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("LedControl")

layoutH = QHBoxLayout()
layoutV = QVBoxLayout()
textbox = QLineEdit()   #creating instance of a textbox
textbox.move(20, 20)
textbox.resize(280,40)

#declaring buttons for Leds
Wbutton1 = QPushButton("Blink Morse Code")
# Wbutton2 = QPushButton("Yellow")
# Wbutton3 = QPushButton("Green")
# Wbutton1.setStyleSheet("background-color : green")
# Wbutton2.setStyleSheet("background-color : blue")
# Wbutton3.setStyleSheet("background-color : green")
Wbutton1.clicked.connect(button1Press)
# Wbutton2.clicked.connect(button1Press)
# Wbutton3.clicked.connect(button1Press)

# adding buttons to the layout
layoutH.addWidget(Wbutton1)
# layoutH.addWidget(Wbutton2)
# layoutH.addWidget(Wbutton3)
window.setLayout(layoutV)
layoutV.addWidget(textbox)
layoutV.addLayout(layoutH)


window.show()
sys.exit(app.exec())