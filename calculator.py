from tkinter import *

class GUI:
    def __init__(self):

        self.window = Tk()
        self.window.title("Calcolatrice GUI")

        # Print the widgets in the window
        self.make_window()

        # Set the variables to "", so they don't appear in the window
        self.canc()

        # Print the window
        self.window.mainloop()


    def make_window(self):
        text_style = ('Helvetica', 14)

        # Set the output widget
        self.output = StringVar(value=" \n ")
        lab = Label(self.window, textvariable=self.output, font=text_style)
        lab.grid(row=0, column=0, rowspan=2, columnspan=4, sticky=N + S + E + W)


        # Set the numbers from 0 to 9 buttons
        button1 = Button(self.window, text="1", font=text_style, width=5, height=3, command=lambda: self.add(1))
        button1.grid(row=2, column=0, sticky=N + S + E + W)

        button2 = Button(self.window, text="2", font=text_style, width=5, height=3, command=lambda: self.add(2))
        button2.grid(row=2, column=1, sticky=N + S + E + W)

        button3 = Button(self.window, text="3", font=text_style, width=5, height=3, command=lambda: self.add(3))
        button3.grid(row=2, column=2, sticky=N + S + E + W)

        button4 = Button(self.window, text="4", font=text_style, width=5, height=3, command=lambda: self.add(4))
        button4.grid(row=3, column=0, sticky=N + S + E + W)

        button5 = Button(self.window, text="5", font=text_style, width=5, height=3, command=lambda: self.add(5))
        button5.grid(row=3, column=1, sticky=N + S + E + W)

        button6 = Button(self.window, text="6", font=text_style, width=5, height=3, command=lambda: self.add(6))
        button6.grid(row=3, column=2, sticky=N + S + E + W)

        button7 = Button(self.window, text="7", font=text_style, width=5, height=3, command=lambda: self.add(7))
        button7.grid(row=4, column=0, sticky=N + S + E + W)

        button8 = Button(self.window, text="8", font=text_style, width=5, height=3, command=lambda: self.add(8))
        button8.grid(row=4, column=1, sticky=N + S + E + W)

        button9 = Button(self.window, text="9", font=text_style, height=3, width=5, command=lambda: self.add(9))
        button9.grid(row=4, column=2, sticky=N + S + E + W)

        button10 = Button(self.window, text="0", font=text_style, height=3, width=5, command=lambda: self.add(0))
        button10.grid(row=5, column=0, sticky=N + S + E + W)

        # Set the CANC button
        button11 = Button(self.window, text="C", font=text_style, height=3, width=5, command=lambda: self.canc())
        button11.grid(row=2, column=3, sticky=N + S + E + W)

        # Set the operators + - * / buttons
        button12 = Button(self.window, text="+", font=text_style, height=3, width=5, command=lambda: self.add('+'))
        button12.grid(row=3, column=3, sticky=N + S + E + W)

        button13 = Button(self.window, text="x", font=text_style, height=3, width=5, command=lambda: self.add('x'))
        button13.grid(row=4, column=3, sticky=N + S + E + W)

        button14 = Button(self.window, text="/", font=text_style, height=3, width=5, command=lambda: self.add('/'))
        button14.grid(row=5, column=3, sticky=N + S + E + W)

        button15 = Button(self.window, text="-", font=text_style, height=3, width=5, command=lambda: self.add('-'))
        button15.grid(row=5, column=2, sticky=N + S + E + W)

        # Set the result button 
        button16 = Button(self.window, text="=", font=text_style, height=3, width=5, command=lambda: self.result())
        button16.grid(row=5, column=1, sticky=N + S + E + W)


    def add(self, value):

        # This function is called when I press a number or operator button
        
        # Control the value of the variables and the value of the button pressed
        # In case of syntax error call the self.error() function 
        if self.first == "":

            if type(value) == int:
                self.first = value
            
            else:
                self.error()

        elif self.operator == "":

            if type(value) == int:
                self.first = self.first * 10 + value

            else:
                self.operator = value

        elif self.second == "":

            if type(value) == int:
                self.second = value

            else:
                self.error()

        else: 

            if type(value) == int:
                self.second = self.second * 10 + value

            else:
                self.first = self.calculate()
                self.operator = value
                self.second = ""

        self.print_output()


    def canc(self, print=True):
        # This function is called to delete (or initalize) the variables of the calculator

        # Set the variable to "" for don't show them
        self.first = ""
        self.operator = ""
        self.second = ""
        self.third = ""

        # After calculating the result whe delete the variables,
        # but we keep the old output setting the variable 'print' to False 
        if print:
            self.print_output()


    def result(self):
        # This function is called for calculate the result and print it in the output widget

        # Assign at the result variable the result
        self.third = self.calculate()

        # if there is a syntax error print 'Syntax Error' in the output widget
        if self.third == None:
            self.error()

        # Print the output in the output widget
        self.print_output()

        # Delete the variables but keep showing them
        self.canc(False)
        

    def calculate(self):
        # This function is called to return the operation result value

        # If there are no values in the operaton it returns 0
        if self.first == "":
            return 0

        # If the operation is composed only by a number the function returns it
        elif self.operator == "":
            return self.first
        
        # If the operation is composed only by a number and an operator 
        # return None, so in the result function call the self.error() function
        elif self.second == "":
            return None

        # Else if there are 2 numbers and an operator
        # it controls the operator and return the right result
        else:

            if self.operator == '+':
                return self.first + self.second

            elif self.operator == '-':
                return self.first - self.second

            elif self.operator == 'x':
                return self.first * self.second

            elif self.operator == '/':
                return self.first / float(self.second)

    
    def print_output(self):
        # This function prints the output in the output widget

        # It prints the 2 numbers and the operator in the first line and the result in the second one
        self.output.set(f"{self.first} {self.operator} {self.second}\n{self.third}")


    def error(self):
        # This function is called to print 'Syntax Error' in the output widget

        # It deletes the variables and set the first to the string 'Error!', so it's shown in the output
        self.first = "Syntax Error"
        self.operator = ''
        self.second = ''
        self.third = ''


if __name__ == '__main__':
    tk = GUI()