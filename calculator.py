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
        button1 = Button(self.window, text="1", font=text_style, width=5, height=3, command=lambda: self.add_number(1))
        button1.grid(row=2, column=0, sticky=N + S + E + W)

        button2 = Button(self.window, text="2", font=text_style, width=5, height=3, command=lambda: self.add_number(2))
        button2.grid(row=2, column=1, sticky=N + S + E + W)

        button3 = Button(self.window, text="3", font=text_style, width=5, height=3, command=lambda: self.add_number(3))
        button3.grid(row=2, column=2, sticky=N + S + E + W)

        button4 = Button(self.window, text="4", font=text_style, width=5, height=3, command=lambda: self.add_number(4))
        button4.grid(row=3, column=0, sticky=N + S + E + W)

        button5 = Button(self.window, text="5", font=text_style, width=5, height=3, command=lambda: self.add_number(5))
        button5.grid(row=3, column=1, sticky=N + S + E + W)

        button6 = Button(self.window, text="6", font=text_style, width=5, height=3, command=lambda: self.add_number(6))
        button6.grid(row=3, column=2, sticky=N + S + E + W)

        button7 = Button(self.window, text="7", font=text_style, width=5, height=3, command=lambda: self.add_number(7))
        button7.grid(row=4, column=0, sticky=N + S + E + W)

        button8 = Button(self.window, text="8", font=text_style, width=5, height=3, command=lambda: self.add_number(8))
        button8.grid(row=4, column=1, sticky=N + S + E + W)

        button9 = Button(self.window, text="9", font=text_style, height=3, width=5, command=lambda: self.add_number(9))
        button9.grid(row=4, column=2, sticky=N + S + E + W)

        button10 = Button(self.window, text="0", font=text_style, height=3, width=5, command=lambda: self.add_number(0))
        button10.grid(row=5, column=0, sticky=N + S + E + W)

        # Set the CANC button
        button11 = Button(self.window, text="C", font=text_style, height=3, width=5, command=lambda: self.canc())
        button11.grid(row=2, column=3, sticky=N + S + E + W)

        # Set the operators + - * / buttons
        button12 = Button(self.window, text="+", font=text_style, height=3, width=5, command=lambda: self.add_operator('+'))
        button12.grid(row=3, column=3, sticky=N + S + E + W)

        button13 = Button(self.window, text="x", font=text_style, height=3, width=5, command=lambda: self.add_operator('x'))
        button13.grid(row=4, column=3, sticky=N + S + E + W)

        button14 = Button(self.window, text="/", font=text_style, height=3, width=5, command=lambda: self.add_operator('/'))
        button14.grid(row=5, column=3, sticky=N + S + E + W)

        button15 = Button(self.window, text="-", font=text_style, height=3, width=5, command=lambda: self.add_operator('-'))
        button15.grid(row=5, column=2, sticky=N + S + E + W)

        # Set the result button 
        button16 = Button(self.window, text="=", font=text_style, height=3, width=5, command=lambda: self.result())
        button16.grid(row=5, column=1, sticky=N + S + E + W)


    def add_number(self, value):
        # This function is called when I press a number or operator button
        
        # Control the place to store the value and save it there 
        # Then print the value
        if self.tmp_number == None:
            self.tmp_number = value
            self.print_output(self.tmp_number)
        
        elif self.tmp_operator != 'x' and self.tmp_operator != '/':
            self.tmp_number = self.tmp_number * 10 + value
            self.print_output(self.tmp_number)

        elif self.tmp_number2 == None:
            self.tmp_number2 = value
            self.print_output(self.tmp_number2)

        else:
            self.tmp_number2 = self.tmp_number2 * 10 + value
            self.print_output(self.tmp_number2)


    def add_operator(self, value):
        # This function get called when the user press an operator button

        # Check if the next operation is a multiplication or not
        is_mult = (value == 'x' or value == '/')

        # Calculate the last operation
        self.calculate(is_multiplication=is_mult)


        self.tmp_operator = value

    
    def calculate(self, is_multiplication=False):
        # Check if this is there are syntax errors
        # in case print a warning in the output
        if self.tmp_number == None:
            self.error()  
            return

        if self.tmp_operator != None and self.tmp_number == None:
            self.error()
            return

        if (self.tmp_operator == 'x' or self.tmp_operator == '/') and self.tmp_number2 == None:
            self.error()
            return

        if self.tmp_operator == '/' and self.tmp_number2 == 0:
            self.error()
            return

        # Calculate the result, doing at first multiplications and divisions,
        # than additions and subtractions
        if self.tmp_operator == '-':
            self.tmp_number *= -1

        elif self.tmp_operator == 'x':
            self.tmp_number *= self.tmp_number2 
            self.tmp_numer2 = None

        elif self.tmp_operator == '/':
            self.tmp_number *= (self.tmp_number2) ** -1
            self.tmp_numer2 = None

        
        # If the next operation is not an operation or a division 
        # add the result of this operation to the final one
        if not is_multiplication:
            self.result_number += self.tmp_number
            self.tmp_number = None


    def canc(self, print=True):
        # This function is called to delete (or initalize) the variables of the calculator

        # Set the variable to None 
        self.result_number = 0
        self.tmp_number = None
        self.tmp_number2 = None         # This variable is used only for moltiplications and divisions
        self.tmp_operator = None         

        # After calculating the result whe delete the variables,
        # but we keep the old output setting the variable 'print' to False 
        if print:
            self.print_output(" ")


    def result(self):
        # This function is called for calculate the result and print it in the output widget

        # Calculate the last operations 
        self.calculate()
        
        # Print the output in the output widget
        if self.result_number == None:
            self.print_output(0)

        else:
            self.print_output(self.result_number)

        # Delete the variables but keep showing them
        self.canc(print=False)

    
    def print_output(self, val):
        # This function prints the output in the output widget

        # Print the argument passed in this function
        # It's always the result_variable or the tmp_number variable
        self.output.set(f"\n{val}\n")


    def error(self):
        # This function is called to print 'Syntax Error' in the output widget

        # Delete the variables and print string 'Error!'
        self.canc(print=False)
        self.print_output("Syntax Error!")


if __name__ == '__main__':
    tk = GUI()