from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Blank & Live Counter")
content = ttk.Frame(root,padding="0 0 300 0")
content.grid(column=0,row=0,sticky=(N,W,E,S))
content.columnconfigure(0,weight=3)
content.rowconfigure(0,weight=3)


#[BlankShells, LiveShells]
ShellCounts = [0,0]
blank = StringVar()
live = StringVar()
blank.set("0")
live.set("0")

def ResetCounter():
    blank.set("0")
    live.set("0")
    ShellCounts[0] = 0
    ShellCounts[1] = 0

#Increment/decrement either global variable  
def UpdateCounter(ShellVar,operation,):
    global ShellCounts
    if ShellVar == "Blank":
        if operation == "add":
            ShellCounts[0] += 1
            blank.set(str(ShellCounts[0]))
        elif operation == "subtract":
            ShellCounts[0] -= 1
            blank.set(str(ShellCounts[0]))
    elif ShellVar == "Live":
        if operation == "add":
            ShellCounts[1] += 1
            live.set(str(ShellCounts[1]))
        elif operation == "subtract":
            ShellCounts[1] -= 1
            live.set(str(ShellCounts[1]))

def get():
    print(str(ShellCounts[0]) + " " + str(ShellCounts[1]))

def ResetChkBtns():
    for child in checkBoxContent.winfo_children():
        if isinstance(child,Checkbutton):
            child.deselect()


ttk.Button(content, text="+", command=lambda:UpdateCounter("Live","add")).grid(column=3,row=2,sticky=(W))
#Above button adds a button that uses Update Counter function to increment the Live counter by 1

ttk.Button(content, text="-", command=lambda:UpdateCounter("Live","subtract")).grid(column=4,row=2,sticky=(E))
#Above button adds a button that uses Update Counter function to decrement the Live counter by 1



#include a label of "Blank" and the value in BlankShells (and the same for LiveShells)
blankLabel = ttk.Label(content,text="Blanks").grid(column=1,row=1,sticky=(W))
blankCounter = ttk.Label(content,textvariable=blank).grid(column=2,row=1,padx=20)
liveLabel = ttk.Label(content,text="Live Rounds").grid(column=1,row=2,sticky=(W))
liveCounter = ttk.Label(content,textvariable=live).grid(column=2,row=2,padx=20)


ttk.Button(content, text="+", command=lambda:UpdateCounter("Blank","add")).grid(column=3,row=1,sticky=(W))
#Above button adds a button that uses Update Counter function to increment the Blank counter by 1

ttk.Button(content, text="-", command=lambda:UpdateCounter("Blank","subtract")).grid(column=4,row=1,sticky=(E))
#Above button adds a button that uses Update Counter function to decrement the Blank counter by 1

ttk.Button(content, text="Reset", command=lambda:ResetCounter()).grid(column=5,row=2,padx=20)



#new frame for the checkboxes because it looks weird otherwise
checkBoxContent = ttk.Frame(root,padding="10")
checkBoxContent.grid(column=0,row=4,sticky=(N,W,E,S))


ttk.Label(checkBoxContent,text="Blanks").grid(column=1,row=3,padx=10)
ttk.Label(checkBoxContent,text="Live").grid(column=1,row=5,padx=10)
for i in range(8):
    var = IntVar()  # Variable to store the state of the checkbox
    cb = Checkbutton(checkBoxContent, text=str(i+1), variable=var)
    cb.grid(row=3, column=i+2,sticky=(W),padx=7)  # Place the checkbox in the frame

for i in range(8):
    var = IntVar()  # Variable to store the state of the checkbox
    cb = Checkbutton(checkBoxContent, text=str(i+1), variable=var)
    cb.grid(row=5, column=i+2)  # Place the checkbox in the frame

ttk.Button(checkBoxContent,text="Reset",command=lambda:ResetChkBtns()).grid(column=0,row=3)
    

root.mainloop()