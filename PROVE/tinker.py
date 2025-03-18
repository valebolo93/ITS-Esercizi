from tkinter import *

#get preleva il testo e lo va a sostituire
def change(evento):
    testo.configure(text=casella_testo.get())
    testo.configure(background="black")

def erase():
    casella_testo.delete(0, END)

def controll():
    print(valore.get())

f= Tk()

valore= IntVar()

#come impostare titolo
f.title("Roma Capitale")
#impostare larghezza finestra
f.geometry("500x500")
#configurazione colore background
f.configure(background="dark red")

casella_testo= Entry(f,show="*")
casella_testo.pack()
#andrà a mettere il cursone sull'etichetta
casella_testo.focus_set()
#per far capire dove inserire testo con una sorta di esempio
casella_testo.insert(0, "Cerca qui")
#per giustificare il testo:
casella_testo.configure(justify=CENTER)
casella_testo.bind("<Return>", change)

b1 = Button(f, text="Elimina",command=erase)
b1.pack()



#come impostare testo,font,colore e posizionamento, lasciando il colore backgrond del sito altrimenti diventa bianco.
testo= Label(f,text="Comune di Roma", background="dark red", font="Times 50 bold")
testo.pack(side=TOP)
#impostare colore testo
testo.configure(foreground="Yellow")

testo1= Label(f,text="Municipi",background="dark red", font="Times 22 bold")
testo1.pack(side=TOP)
testo1.configure(cursor="hand2")


testo1.configure(foreground="Yellow")
#comando per far si che la finestra rimanga aperta

#bottoni
b = Button(f, text="Servizi",command=change)
b.pack(side=TOP)

casella =Checkbutton(f,text="Residente a Roma",variable=valore, command=controll)
casella.pack()

f.mainloop()