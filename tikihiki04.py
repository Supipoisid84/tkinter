#Alex Kreimann
#06.02.2025
#tk04

import tkinter as tk

def main():
    aken = tk.Tk()
    aken.geometry("300x400")
   
    nupp1 = tk.Button(aken, text="Vajuta mind", bg="blue", fg="white", font=("Arial", 16))
    nupp2 = tk.Button(aken, text="Vajuta mind", bg="black", fg="white", font=("Arial", 16))
    nupp3 = tk.Button(aken, text="Vajuta mind", bg="white", fg="black", font=("Arial", 16))
    nupp4 = tk.Button(aken, text="Vajuta mind", bg="green", fg="white", font=("Arial", 16))
    nupp1.pack(padx=20, pady=10)
    nupp2.pack(padx=20, pady=10)
    nupp3.pack(padx=20, pady=10)
    nupp4.pack(padx=20, pady=10)

    aken.mainloop()

if __name__ == "__main__":
    main()
