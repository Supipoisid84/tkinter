#Alex Kreimann
#04.02.2025
#tk01

    #Veendu, et arvutis on Python paigaldatud
    #Vali oma programm ja loo uus projekt tkinter ülesannete jaoks (ära miksi kataloogi eelmiste ülesannetega)
    #Seadista Github või Github Desktop
    #Loo rakenduse põhistruktuur, mis käivitab akna 400×400
    #    akna nimeks pane oma nimi, näiteks “Mario ülesanded”
    #    keela akna suurendamine y-suunas, x-suunas on lubatud
    #Käivita aken

import tkinter as tk
import ctypes

def main():
    aken=tk.Tk()
    aken.title("tkinter ülesanded")
    aken.geometry("400x400")
    # Akna suuruse muutmise keelamine
    aken.resizable(False,True)
   
    label=tk.Label(aken,text="Tere,maailm!").pack()
    button=tk.Button(aken,text="Sulge",command=aken.destroy).pack()
   
    aken.mainloop()

if __name__ == "__main__":
    main()
