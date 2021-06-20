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
        self.output = StringVar(value="  ")
        lab = Label(self.window, textvariable=self.output, font=text_style)
        lab.grid(row=0, column=0, columnspan=3, sticky=N + S + E + W)


        # Set the numbers from 0 to 9 buttons
        button = Button(self.window, text="1", font=text_style, width=5, height=3, command=lambda: self.add_number(1))
        button.grid(row=1, column=0, sticky=N + S + E + W)

        button = Button(self.window, text="2", font=text_style, width=5, height=3, command=lambda: self.add_number(2))
        button.grid(row=1, column=1, sticky=N + S + E + W)

        button = Button(self.window, text="3", font=text_style, width=5, height=3, command=lambda: self.add_number(3))
        button.grid(row=1, column=2, sticky=N + S + E + W)

        button = Button(self.window, text="4", font=text_style, width=5, height=3, command=lambda: self.add_number(4))
        button.grid(row=2, column=0, sticky=N + S + E + W)

        button = Button(self.window, text="5", font=text_style, width=5, height=3, command=lambda: self.add_number(5))
        button.grid(row=2, column=1, sticky=N + S + E + W)

        button = Button(self.window, text="6", font=text_style, width=5, height=3, command=lambda: self.add_number(6))
        button.grid(row=2, column=2, sticky=N + S + E + W)

        button = Button(self.window, text="7", font=text_style, width=5, height=3, command=lambda: self.add_number(7))
        button.grid(row=3, column=0, sticky=N + S + E + W)

        button = Button(self.window, text="8", font=text_style, width=5, height=3, command=lambda: self.add_number(8))
        button.grid(row=3, column=1, sticky=N + S + E + W)

        button = Button(self.window, text="9", font=text_style, height=3, width=5, command=lambda: self.add_number(9))
        button.grid(row=3, column=2, sticky=N + S + E + W)

        button = Button(self.window, text="0", font=text_style, height=3, width=5, command=lambda: self.add_number(0))
        button.grid(row=4, column=1, sticky=N + S + E + W)

        # Set the point button
        button = Button(self.window, text=".", font=text_style, height=3, width=5, command=lambda: self.point())
        button.grid(row=4, column=0, sticky=N + S + E + W)

        # Set the CANC button
        button = Button(self.window, text="C", font=text_style, height=3, width=5, command=lambda: self.canc())
        button.grid(row=0, column=3, sticky=N + S + E + W)

        # Set the operators + - * / buttons
        button = Button(self.window, text="+", font=text_style, height=3, width=5, command=lambda: self.add_operator('+'))
        button.grid(row=1, column=3, sticky=N + S + E + W)

        button = Button(self.window, text="x", font=text_style, height=3, width=5, command=lambda: self.add_operator('x'))
        button.grid(row=2, column=3, sticky=N + S + E + W)

        button = Button(self.window, text="/", font=text_style, height=3, width=5, command=lambda: self.add_operator('/'))
        button.grid(row=3, column=3, sticky=N + S + E + W)

        button = Button(self.window, text="-", font=text_style, height=3, width=5, command=lambda: self.add_operator('-'))
        button.grid(row=4, column=3, sticky=N + S + E + W)

        # Set the result button 
        button = Button(self.window, text="=", font=text_style, height=3, width=5, command=lambda: self.result())
        button.grid(row=4, column=2, sticky=N + S + E + W)


    def add_number(self, value):
        # This function is called when I press a number or operator button
        
        # Control the place to store the value and save it there 
        # Then print the value
        if self.tmp_number == None:
            self.tmp_number = value
            self.print_output(self.tmp_number)
        
        elif self.tmp_operator == 'x' or self.tmp_operator == '/':

            if self.tmp_number2 == None:
                self.tmp_number2 = value
            
            else:
                if self.after_point == False:
                    self.tmp_number2 = self.tmp_number2 * 10 + value
            
                else:
                    self.tmp_number2 += float(value / (10.0 ** self.after_point))
                    self.after_point += 1

            self.print_output(self.tmp_number2)

        else:
            if self.after_point == False:
                self.tmp_number = self.tmp_number * 10 + value
            
            else:
                self.tmp_number += float(value / (10.0 ** self.after_point))
                self.after_point += 1

            self.print_output(self.tmp_number)

        self.just_result = False


    def add_operator(self, value):
        # This function get called when the user press an operator button

        # Check if the next operation is a multiplication or not
        is_mult = (value == 'x' or value == '/')

        self.after_point = False

        # Calculate the last operation
        if self.calculate(is_multiplication=is_mult) == 1:
            return

        self.tmp_operator = value

    
    def point(self):
        # Check the syntax
        if self.after_point != False:
            self.error("Point pressed yet!")
            return

        if self.tmp_number == None:
            self.error("no number before the point!")
            return

        if (self.tmp_operator == 'x' or self.tmp_operator == '/') and self.tmp_number2 == None:
            self.error("no number before the point!")
            return

        # Start counting how many numbers are there after the point
        self.after_point = 1

    
    def calculate(self, is_multiplication=False):

        if self.just_result:
            self.tmp_number = self.result_number
            self.just_result = False
            self.result_number = 0

        # Check if this is there are syntax errors
        # in case print a warning in the output
        if self.tmp_number == None:
            self.error("no numbers in the operation!")  
            return 1

        if self.tmp_operator != None and self.tmp_number == None:
            self.error("no number after the + or - operators!")
            return 1

        if (self.tmp_operator == 'x' or self.tmp_operator == '/') and self.tmp_number2 == None:
            self.error("no number after the x or / operators!")
            return 1

        if self.tmp_operator == '/' and self.tmp_number2 == 0:
            self.error("impossible division for 0")
            return 1

        # Calculate the result, doing at first multiplications and divisions,
        # than additions and subtractions
        if self.tmp_operator == '-':
            self.tmp_number *= -1

        elif self.tmp_operator == 'x':
            self.tmp_number *= self.tmp_number2 
            self.tmp_number2 = None

        elif self.tmp_operator == '/':
            self.tmp_number *= (1 / self.tmp_number2)
            self.tmp_number2 = None

        # If the next operation is not an operation or a division 
        # add the result of this operation to the final one
        if not is_multiplication:
            self.result_number += self.tmp_number
            self.tmp_number = None

        return 0


    def canc(self, print=True, keep_result=False):
        # This function is called to delete (or initalize) the variables of the calculator

        # Set the variable to None 
        self.tmp_number = None
        self.tmp_number2 = None         # This variable is used only for moltiplications and divisions
        self.tmp_operator = None  
        self.after_point = False

        if not keep_result:
            self.just_result = False 
            self.result_number = 0

        # After calculating the result whe delete the variables,
        # but we keep the old output setting the variable 'print' to False 
        if print:
            self.print_output(" ")


    def result(self):
        # This function is called for calculate the result and print it in the output widget

        # Calculate the last operations 
        if self.calculate() == 1:
            return
        
        # Print the output in the output widget
        if self.result_number == None:
            self.print_output(" ")

        else:
            self.print_output(f"{self.result_number:g}")

        # Delete the variables but keep showing them
        self.canc(print=False, keep_result=True)

        self.just_result = True

    
    def print_output(self, val):
        # This function prints the output in the output widget

        # Print the argument passed in this function
        # It's always the result_variable or the tmp_number variable
        self.output.set(f"\n{val}\n")


    def error(self, type=None):
        # This function is called to print 'Syntax Error' in the output widget

        # Delete the variables and print a warning
        self.canc(print=False)

        self.print_output("Syntax Error!")

        if type != None:
            print(f"Syntax Error: {type}")


if __name__ == '__main__':
    tk = GUI()