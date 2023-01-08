from tkinter import *    nsioacao
import math

def click(value):
    ex = entryField.get()  
    answer = ''

    try:

        if value == 'C':
            ex = ex[0:len(ex) - 1]  
            entryField.delete(0, END)
            entryField.insert(0, ex)
            return

        elif value == 'CE':
            entryField.delete(0, END)

        elif value == '√':
            answer = math.sqrt(eval(ex))

        elif value == 'π':
            answer = math.pi

        elif value == '2π':
            answer = 2*(math.pi)

        elif value == 'cosθ':
            answer = math.cos(math.radians(eval(ex)))

        elif value == 'tanθ':
            answer = math.tan(math.radians(eval(ex)))

        elif value == 'sinθ':
            answer = math.sin(math.radians(eval(ex)))

        elif value == chr(8731):
            answer = eval(ex) ** (1 / 3)

        elif value == 'x\u02b8':  
            entryField.insert(END, '**')
            return

        elif value == 'x\u00B2':
            answer = eval(ex) ** 2

        elif value == 'ln':
            answer = math.log2(eval(ex))

        elif value == 'deg':
            answer = math.degrees(eval(ex))

        elif value == "rad":
            answer = math.radians(eval(ex))

        elif value == 'e':
            answer = math.e

        elif value == 'log₁₀':
            answer = math.log10(eval(ex))

        elif value == 'x!':
            answer = math.factorial(eval(ex))

        elif value == 'bin':
            if ex.isdigit():
                answer = bin(int(ex))

            else:
                if ex[1] == "x":
                    ex = int(ex, 16)
                    answer = bin(ex)

                elif ex[1] == "o":
                    ex = int(ex, 8)
                    answer = bin(ex)


        elif value == 'hex':
            if ex.isdigit():
                answer = hex(int(ex))

            else:
                if ex[1] == "b":
                    ex = int(ex, 2)
                    answer = hex(ex)

                elif ex[1] == "o":
                    ex = int(ex, 8)
                    answer = hex(ex)

        elif value == 'oct':
            if ex.isdigit():
                answer = oct(int(ex))

            else:
                if ex[1] == "b":
                    ex = int(ex, 2)
                    answer = oct(ex)

                elif ex[1] == "x":
                    ex = int(ex, 16)
                    answer = oct(ex)

        elif value == chr(247):  
            entryField.insert(END, "/")
            return

        elif value == '=':
            answer = eval(ex)

        elif value == 'END':
            root.destroy()

        else:
            entryField.insert(END, value)
            return

        entryField.delete(0, END)
        entryField.insert(0, answer)

    except SyntaxError:
        pass


def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

def mod(a ,b ):
    return a % b


root = Tk()
root.title('Calculator')
root.config(bg='#8EC3B0')
root.geometry('680x486+100+100')


entryField = Entry(root, font=('Arial', 20, 'bold'), bg='#BCEAD5', fg='black', bd=10, relief=SUNKEN, width=30)
entryField.grid(row=0, column=0, columnspan=8)

button_text_list = ["C", "CE", "√", "+", "π", "cosθ", "tanθ", "sinθ",
                    "1", "2", "3", "-", "2π", "bin","hex","oct" ,
                    "4", "5", "6", "*", chr(8731), "x\u02b8", "x\u00B2","log₁₀",
                    "7", "8", "9", chr(247), "ln", "deg", "rad", "e",
                    "0", ".", "%", "=", "(", ")", "x!","END"]
rowvalue = 1
columnvalue = 0
for i in button_text_list:

    button = Button(root, width=5, height=2, bd=2, relief=SUNKEN, text=i, bg='#9ED5C5', fg='black',
                    font=('Arial', 18, 'bold'), activebackground='#9ED5C5', command=lambda button=i: click(button))
    button.grid(row=rowvalue, column=columnvalue, pady=1)
    columnvalue += 1
    if columnvalue > 7:
        rowvalue += 1
        columnvalue = 0

root.mainloop()
