import customtkinter as ctk

root = ctk.CTk()

root.title("test")
root.geometry('800x800')

def clicker():
    pass

choices = ["Colour", "Days", "Places"]
word_choice = ctk.CTkSegmentedButton(root, values=choices, command=clicker)
word_choice.pack(pady=40)
word_choice.set("Colour")


root.mainloop()