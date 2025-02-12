#Alex Kreimann
#04.02.2025
#tk02

import tkinter as tk
from PIL import Image, ImageTK

    #Loo peamine aken ning kasutame if __name__ == "__main__": main() meetodit
    #Loo silt oma nimega ja vorminda see:
    #    Kirjatüüp: Arial
    #    Suurus: 16
    #    Paks kiri (bold)
    #    Värv: tumesinine
    #Lisa pilt mõõtudega: 200x200px, kärbi image.crop((0, 0, 200, 200))
    #Lisa tekstikast, mis võtab info failist ja võimaldab kerida. Tekstifail tee ise ja piisava pikkusega
    #    Laius: 40
    #    Kõrgus: 20
    #    Teksti mähkimine: sõna kaupa
    #    Kirjatüüp: Arial
    #    Suurus: 12
    #Lisa tekstikastile kerimisriba
    #Keela akna suuruse muutmine

def loe_fail(failinimi):
    with open(failinimi,'r',encoding='utf-8') as file:
        return file.read()

def main():
    aken=tk.Tk()
    aken.title("tkinter ülesanded")
    aken.geometry("400x400")
    # Akna suuruse muutmise keelamine
    aken.resizable(False,False)

    # Pildi avamine ja Tkinteri jaoks ettevalmistamine
    pilt=Image.open("Kuck Porris.webp")
    p=0
    pilt=pilt.crop((0+p,0+p,200+p,200+p))
    # pilt = pilt.resize((200,200))
    foto=ImageTk.PhotoImage(pilt)

    # Sildi kuvamine
    label=tk.Label(aken,text="Jäck Nurris",font=("Arial",16,"bold"),fg="blue").pack()

    # Pildi kuvamine Label abil
    label=tk.Label(aken,image=foto)
    label.image=foto
    label.pack()

    # Tekstkast
    tekst=tk.Text(aken,wrap=tk.WORD,font=("Arial",12))
    scrollbar=tk.Scrollbar(aken,command=tekst.yview)
    tekst.config(yscrollcommand=scrollbar.set)
    scrollbar.pack(side=tk.RIGHT,fill=tk.Y)
    tekst.pack(expand=True,fill=tk.BOTH)

    failisisu=loe_fail("tekst.txt")
    tekst.insert(tk.INSERT,failisisu)
   
    aken.mainloop()

if __name__ == "__main__":
    main()
