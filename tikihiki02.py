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

def kuva_pilt(aken,failinimi,laius,korgus):
    pilt=image.open(failinimi)
    pilt=pilt.resize((laius,korgus))
    foto=imageTK.photoimage(pilt)
    label=tkl.label(aken,image=foto)
    label.image=foto
    label.pack()

def main():
    aken=tk.tk()
    aken.title("Mario ülesanded")
    aken.geometry("400x300")

    #kuva_pilt(aken,"img/python_512x512.png",200,200)

    aken.mainloop()

if __name__== "__main__":
    main()