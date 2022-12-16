from tkinter import *
from tkinter import ttk

window = Tk()
window.title("Lista Despegable")
window.geometry('200x190')

label = ttk.Label(window,text="Lista Despegable")
label.place(x=45,y=20)

combo = ttk.Combobox(window,width=17)
combo.place(x=30,y=77)

opciones = ["Opcion1","Opcion2","Opcion3"]

combo['values'] = opciones

window.mainloop()
