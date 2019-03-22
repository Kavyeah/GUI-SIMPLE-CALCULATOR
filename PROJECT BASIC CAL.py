#Python program to  create calculator using Tkinter
from tkinter import *
expression = ""    # globally declare the expression variable
def press(num):                    # Function to update expression
    # point out the global expression variable
    global expression
 
    # concatenation of string
    expression = expression + str(num)
 
    # update the expression by using set method
    equation.set(expression)

def equalpress():        # Function to evaluate the final expression
    # Try and except statement is used
    # for handling the errors like zero
    # division error etc.
 
    # Put that code inside the try block
    # which may generate the error
    try:
 
        global expression
 
        # eval function evaluate the expression
        # and str function convert the result
        # into string
        total = str(eval(expression))
 
        equation.set(total)
 
        # initialze the expression variable
        # by empty string
        expression = ""
 
    # if error is generate then handle
    # by the except block
    except:
 
        equation.set(" error ")
        expression = ""
 
 
# Function to clear the contents
# of text entry box
def clear():
    global expression
    expression = ""
    equation.set("")
 
 
# Driver code
if __name__ == "__main__":
    # create a GUI window
    root = Tk()
    
 
    # set the background colour of GUI window
    root.configure(background="light blue")
 
    # set the title of GUI window
    root.title("Calculator")
    # StringVar() is the variable class
    # we create an instance of this class
    equation = StringVar()
 
    # create the text entry box for
    # showing the expression .
    expression_field = Entry(textvariable=equation)
 
    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure .
    expression_field.grid(columnspan=4,ipady=10,ipadx=70)
 
    equation.set('0')
 
    # create a Buttons and place at a particular
    # location inside the root window .
    # when user press the button, the command or
    # function affiliated to that button is executed .
    button1 = Button(text=' 1 ', fg='black', bg='SlateGray3',
                     command=lambda: press(1), height=1, width=8)
    button1.grid(row=2, column=0)
 
    button2 = Button(text=' 2 ', fg='black', bg='SlateGray3',
                     command=lambda: press(2), height=1, width=8)
    button2.grid(row=2, column=1)
 
    button3 = Button(text=' 3 ', fg='black', bg='SlateGray3',
                     command=lambda: press(3), height=1, width=8)
    button3.grid(row=2, column=2)
 
    button4 = Button(text=' 4 ', fg='black', bg='SlateGray3',
                     command=lambda: press(4), height=1, width=8)
    button4.grid(row=3, column=0)
 
    button5 = Button(text=' 5 ', fg='black', bg='SlateGray3',
                     command=lambda: press(5), height=1, width=8)
    button5.grid(row=3, column=1)
 
    button6 = Button(text=' 6 ', fg='black', bg='SlateGray3',
                     command=lambda: press(6), height=1, width=8)
    button6.grid(row=3, column=2)
 
    button7 = Button(text=' 7 ', fg='black', bg='SlateGray3',
                     command=lambda: press(7), height=1, width=8)
    button7.grid(row=4, column=0)
 
    button8 = Button(text=' 8 ', fg='black', bg='SlateGray3',
                     command=lambda: press(8), height=1, width=8)
    button8.grid(row=4, column=1)
 
    button9 = Button(text=' 9 ', fg='black', bg='SlateGray3',
                     command=lambda: press(9), height=1, width=8)
    button9.grid(row=4, column=2)
 
    button0 = Button(text=' 0 ', fg='black', bg='SlateGray3',
                     command=lambda: press(0), height=1, width=8)
    button0.grid(row=5, column=0)
 
    plus = Button(text=' + ', fg='black', bg='SlateGray2',
                  command=lambda: press("+"), height=1, width=8)
    plus.grid(row=2, column=3)
 
    minus = Button(text=' - ', fg='black', bg='SlateGray2',
                   command=lambda: press("-"), height=1, width=8)
    minus.grid(row=3, column=3)
 
    multiply = Button(text=' * ', fg='black', bg='SlateGray2',
                      command=lambda: press("*"), height=1, width=8)
    multiply.grid(row=4, column=3)
 
    divide = Button(text=' / ', fg='black', bg='SlateGray2',
                    command=lambda: press("/"), height=1, width=8)
    divide.grid(row=5, column=3)
 
    equal = Button(text=' = ', fg='black', bg='SlateGray3',
                   command=equalpress,height=1, width=8)
    equal.grid(row=5, column='2')
 
    clear = Button(text='C', fg='black', bg='SlateGray1',
                   command=clear, height=1, width=8)
    clear.grid(row=5, column='1')
 
    

