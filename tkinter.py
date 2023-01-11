import tkinter as tk
window = tk.Tk()
window.title("Calculator")


# global variables 
expression = ""
ifOperatorPressed = False
lastExpression = ""
lastNumberInputted = ""
lastOperatorPressed = ""
ifEqualPressedAlready = False

# init Frames
numberFrame = tk.Frame()
operatorFrame = tk.Frame()
EntryFrame = tk.Frame()

# putting frames within frames so that they can be clean
# still need to make the gui cleaner as there's empty space between numbers and operator buttons

entry = tk.Entry(master=EntryFrame)

row1 = tk.Frame(master=numberFrame)
row2 = tk.Frame(master=numberFrame)
row3 = tk.Frame(master=numberFrame)
row4 = tk.Frame(master=numberFrame)
rowOperator = tk.Frame()

def insert(x):
    global ifOperatorPressed
    global expression
    global lastNumberInputted
    global ifEqualPressedAlready
    if ifOperatorPressed == True: # if an Operator was last pressed, clear the entry field for next number
        entry.delete(0,tk.END)
        ifOperatorPressed = False
        lastNumberInputted = ""
    elif ifEqualPressedAlready == True: # if equals was last pressed, clear the entry field for next number
        entry.delete(0,tk.END)
        ifOperatorPressed = False
        lastNumberInputted = ""
        expression = ""
    if entry.get() == "0": # no repeating zeroes
        entry.delete(0,1)
        expression = expression[:-1]
        lastNumberInputted = lastNumberInputted[:-1]
    entry.insert(tk.END,x)
    lastNumberInputted = lastNumberInputted + str(x)
    expression = expression + str(x)
    ifEqualPressedAlready = False
    return

def clear():
    global expression
    global ifOperatorPressed
    global ifEqualPressedAlready
    global lastNumberInputted
    lastNumberInputted = ""
    ifEqualPressedAlready = False
    if ifOperatorPressed == False:
        entryLength = len(entry.get())
        expression = expression[:-entryLength] 
    if entry.get() == "":
        expression = ""
    entry.delete(0,tk.END)
    ifOperatorPressed = False
    return

def insertDot():
    global expression
    global ifOperatorPressed
    global lastNumberInputted
    global ifEqualPressedAlready
    ifEqualPressedAlready = False
    if ifOperatorPressed == True:
        entry.delete(0,tk.END)
        ifOperatorPressed = False
        lastNumberInputted = ""
    if "." not in entry.get():
        entry.insert(tk.END,".")
        expression = expression + "."
        lastNumberInputted = lastNumberInputted + "."
    return  

def operatorPressed(operator):
    global expression
    global ifOperatorPressed
    global lastNumberInputted
    global ifEqualPressedAlready
    global lastOperatorPressed
    lastOperatorPressed = operator
    ifEqualPressedAlready = False
    if ifOperatorPressed == True:
        expression = expression[:-1]
    expression = str(eval(expression))
    entry.delete(0,tk.END)
    entry.insert(tk.END,expression)
    if operator == "+":
        expression = expression + "+"
    elif operator == "-":
        expression = expression + "-"
    elif operator == "*":
        expression = expression + "*"
    elif operator == "/":
        expression = expression + "/"
    ifOperatorPressed = True
    return

def equals():
    global expression
    global ifOperatorPressed
    global lastExpression
    global ifEqualPressedAlready
    global lastOperatorPressed
    global lastNumberInputted
    lastEntry = entry.get()
    lastExpression = expression[-len(entry.get())-1:]
    if ifOperatorPressed == False:
        if ifEqualPressedAlready == True:
            expression = expression + lastOperatorPressed + str(lastNumberInputted)
        expression = str(eval(expression))
        entry.delete(0,tk.END)
        entry.insert(tk.END,expression)
    else:#if last button pressed was an operator
        if expression[-1] == '+' or expression[-1] == '-' or expression[-1] == '*' or expression[-1] == '/': # if last button pressed was an operator
            expression = expression + expression[-1] + lastEntry
            entry.delete(0,tk.END)
            entry.insert(tk.END,eval(expression))
        else:
            entry.delete(0,tk.END)
            entry.insert(tk.END,eval(expression))
    ifOperatorPressed = False
    ifEqualPressedAlready = True
    return

button1 = tk.Button(
    master=row1,
    text="1",
    command=lambda:insert(1),
    height=2 ,width=2
)
button2 = tk.Button(
    master=row1,
    text="2",
    command=lambda:insert(2),
    height=2 ,width=2
)
button3 = tk.Button(
    master=row1,
    text="3",
    command=lambda:insert(3),
    height=2 ,width=2
)
button4 = tk.Button(
    master=row2,
    text="4",
    command=lambda:insert(4),
    height=2 ,width=2
)
button5 = tk.Button(
    master=row2,
    text="5",
    command=lambda:insert(5),
    height=2 ,width=2
)
button6 = tk.Button(
    master=row2,
    text="6",
    command=lambda:insert(6),
    height=2 ,width=2
)
button7 = tk.Button(
    master=row3,
    text="7",
    command=lambda:insert(7),
    height=2 ,width=2
)
button8 = tk.Button(
    master=row3,
    text="8",
    command=lambda:insert(8),
    height=2 ,width=2
)
button9 = tk.Button(
    master=row3,
    text="9",
    command=lambda:insert(9),
    height=2 ,width=2
)
button0 = tk.Button(
    master=row4,
    text="0",
    command=lambda:insert(0),
    height=2 ,width=2
)
buttonDot = tk.Button(
    master=row4,
    text=".",
    command=lambda:insertDot(),
    height=2 ,width=2
)
buttonClear = tk.Button(
    master=row4,
    text="C",
    command=lambda:clear(),
    height=2 ,width=2
)
buttonPlus = tk.Button(
    master=rowOperator,
    text="+",
    command=lambda:operatorPressed("+"),
    height=2 ,width=2
)
buttonMinus = tk.Button(
    master=rowOperator,
    text="-",
    command=lambda:operatorPressed("-"),
    height=2 ,width=2
)
buttonMultiply = tk.Button(
    master=rowOperator,
    text="x",
    command=lambda:operatorPressed("*"),
    height=2 ,width=2
)
buttonDivide = tk.Button(
    master=rowOperator,
    text="/",
    command=lambda:operatorPressed("/"),
    height=2 ,width=2
)
buttonEquals = tk.Button(
    master=rowOperator,
    text="=",
    command=lambda:equals(),
    height=2 ,width=2
)

entry.pack()
EntryFrame.pack()

button1.pack(side=tk.LEFT)
button2.pack(side=tk.LEFT)
button3.pack(side=tk.LEFT)
button4.pack(side=tk.LEFT)
button5.pack(side=tk.LEFT)
button6.pack(side=tk.LEFT)
button7.pack(side=tk.LEFT)
button8.pack(side=tk.LEFT)
button9.pack(side=tk.LEFT)
button0.pack(side=tk.LEFT)
buttonDot.pack(side=tk.LEFT)
buttonClear.pack(side=tk.LEFT)
buttonDivide.pack()
buttonMultiply.pack()
buttonMinus.pack()
buttonPlus.pack()
buttonEquals.pack()

row3.pack()
row2.pack()
row1.pack()
row4.pack()
rowOperator.pack(side=tk.RIGHT)

numberFrame.pack(side=tk.LEFT)
operatorFrame.pack(side=tk.RIGHT)

window.mainloop()
