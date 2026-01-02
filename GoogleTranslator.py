from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

def change(text = "type", src = "English", dest = "Hindi"):
    text1 = text
    src1 = src
    dest1 = dest
    trans = Translator()
    trans1 = trans.translate(text, src=src1, dest=dest1)
    return trans1.text

def data():
    s = comb_sor.get()
    d = comb_dest.get()
    msg = Sor_txt.get(1.0, END)
    textget = change(text=msg, src=s, dest=d)
    dest_txt.delete(1.0, END)
    dest_txt.insert(END, textget)


root = Tk()
root.title("Translator")
root.geometry("500x800")
root.config(bg='Darkblue')

lab_txt = Label(root, text="Translator", font=("Time New Roman", 40, "bold"))
lab_txt.place(x=100, y=40, width=300, height=50)

lab_txt = Label(root, text="Source Text", font=("Time New Roman", 20, "bold"), fg = "White", bg ="Darkblue")
lab_txt.place(x=100, y=100, width=300, height=20)

frame = Frame(root).pack(side = BOTTOM)

Sor_txt = Text(frame, font=("Time New Roman", 20, "bold"), wrap=WORD, padx=5, pady=5)
Sor_txt.place(x=10, y=130, width=480, height=150)

list_text = list(LANGUAGES.values())

comb_sor = ttk.Combobox(frame, values=list_text, font=("Time New Roman", 14, "bold"))
comb_sor.place(x=10, y=300, width=150, height=40)
comb_sor.set("english")

button_change = Button(frame, text="Translate", relief=RAISED, command = data)
button_change.place(x=170, y=300, width=150, height=40)

comb_dest = ttk.Combobox(frame, values=list_text, font=("Time New Roman", 14, "bold"))
comb_dest.place(x=330, y=300, width=150, height=40)
comb_dest.set("english")

lab_txt = Label(root, text="Dest Text", font=("Time New Roman", 20, "bold"), fg = "White", bg ="Darkblue")
lab_txt.place(x=100, y=360, width=300, height=20)

dest_txt = Text(frame, font=("Time New Roman", 20, "bold"), wrap=WORD, padx=5, pady=5)
dest_txt.place(x=10, y=400, width=480, height=150)

root.mainloop()