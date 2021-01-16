# Import everything from the tkinter module

from tkinter import *

# Initializing the Main Window(Container)

calculator = Tk()

# Assigning our Main Window A title

calculator.title("Simple Calculator")

# This is the screen that will serve as our display

inputScreen = Entry(calculator, borderwidth=5, width=35)

# Positioning the input screen on the Tkinter's Window grid

inputScreen.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# ARITHMETIC FUNCTIONS
""" This are the functions defining the functionality of our calculator"""


def button_click(number):
    """Displays the numbers pressed"""

    # inputScreen.delete(0,END) # initially for testing purposes
    # inputScreen.insert(0,number) # inserts from the front(0)
    inputScreen.insert(END, number)


def button_clear():
    """ Clears the input Screen( Display ) """
    inputScreen.delete(0, END)


def button_equals():
    """Triggers display of results"""

    second_num = inputScreen.get()
    inputScreen.delete(0, END)

    if math == "addition":
        inputScreen.insert(0, int(second_num) + int(firstNumber))
    if math == "multiplication":
        inputScreen.insert(0, int(second_num) * int(firstNumber))
    if math == "division":
        inputScreen.insert(0, int(firstNumber) / int(second_num))
    if math == "subtraction":
        inputScreen.insert(0, int(firstNumber) - int(second_num))
    if math == "square":
        inputScreen.insert(0, int(firstNumber) * int(firstNumber))


def button_add():
    """ Specifies addition and automatically captures the previously typed in number """

    fnum = inputScreen.get()
    global firstNumber
    global math
    math = "addition"
    firstNumber = int(fnum)
    inputScreen.delete(0, END)


def button_multiply():
    """Specifies multiplication and automatically captures the previously typed in number"""

    fnum = inputScreen.get()
    global firstNumber
    global math
    math = "multiplication"
    firstNumber = int(fnum)
    inputScreen.delete(0, END)


def button_division():
    """Specifies division and automatically captures the previously typed in number"""

    fnum = inputScreen.get()
    global firstNumber
    global math
    math = "division"
    firstNumber = int(fnum)
    inputScreen.delete(0, END)


def button_subtract():
    """Specifies subtraction and automatically captures the previously typed in number"""

    fnum = inputScreen.get()
    global firstNumber
    global math
    math = "subtraction"
    firstNumber = int(fnum)
    inputScreen.delete(0, END)

def button_squared():
    fnum = inputScreen.get()
    global firstNumber
    global math
    math = "square"
    firstNumber = int(fnum)


# Button declarations grouped as they will appear on the grid and their respective functions

""" Tkinter employs a grid geometry manager that organises widgets in a table-like structure in the parent widget(our Calculator). The master widget is split into rows and columns, and each part of the table can hold a widget. """

# We will now declare the buttons and assign them their respective functions

""" The button widget declaration will be done in this general format 

buttonName = Button(Master Widget, button label as text, padx (Additional padding left and right of the text), pady (Additional padding above and below the text), Command (Function or method to be called when the button is clicked.)

"""

buttonOne = Button(calculator, text="1", padx=40, pady=20, command=lambda: button_click(1))
buttonTwo = Button(calculator, text="2", padx=40, pady=20, command=lambda: button_click(2))
buttonThree = Button(calculator, text="3", padx=40, pady=20, command=lambda: button_click(3))

buttonFour = Button(calculator, text="4", padx=40, pady=20, command=lambda: button_click(4))
buttonFive = Button(calculator, text="5", padx=40, pady=20, command=lambda: button_click(5))
buttonSix = Button(calculator, text="6", padx=40, pady=20, command=lambda: button_click(6))

buttonSeven = Button(calculator, text="7", padx=40, pady=20, command=lambda: button_click(7))
buttonEight = Button(calculator, text="8", padx=40, pady=20, command=lambda: button_click(8))
buttonNine = Button(calculator, text="9", padx=40, pady=20, command=lambda: button_click(9))

buttonZero = Button(calculator, text="0", padx=40, pady=20, command=lambda: button_click(0))

buttonAdd = Button(calculator, text="+", padx=40, pady=20, command=button_add)
buttonEquals = Button(calculator, text="=", padx=90, pady=20, command=button_equals)
buttonSquare = Button(calculator, text="**", padx=40, pady=20, command=button_squared)
buttonClear = Button(calculator, text="Clear", padx=40, pady=20, command=button_clear)

buttonMultiply = Button(calculator, text="x", padx=42, pady=20, command=button_multiply)
buttonDivide = Button(calculator, text="/", padx=40, pady=20, command=button_division)
buttonSubtract = Button(calculator, text="-", padx=42, pady=20, command=button_subtract)

# Button positioning on the Tkinter Grid is done as below
""" row 0 is already occupied by our input screen. Grid Assignment starts from the Top Left"""

buttonOne.grid(row=3, column=0)
buttonTwo.grid(row=3, column=1)
buttonThree.grid(row=3, column=2)

buttonFour.grid(row=2, column=0)
buttonFive.grid(row=2, column=1)
buttonSix.grid(row=2, column=2)

buttonSeven.grid(row=1, column=0)
buttonEight.grid(row=1, column=1)
buttonNine.grid(row=1, column=2)

buttonZero.grid(row=4, column=0)

buttonAdd.grid(row=5, column=0)
buttonEquals.grid(row=5, column=1, columnspan=2)  # spans 2 columns
buttonSquare.grid(row=4, column=1, columnspan=1)
buttonClear.grid(row=4, column=2, columnspan=1)  # spans 1 columns
buttonSubtract.grid(row=6, column=0)
buttonMultiply.grid(row=6, column=1)
buttonDivide.grid(row=6, column=2)

calculator.mainloop()
""" mainloop() is an infinite loop used to run the application, wait for an event to occur and
process the event as long as the window is not closed. """
