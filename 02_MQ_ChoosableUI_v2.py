"""
Second version of the ChoosableUI,
imported into class to make the easier.
"""
import customtkinter as ctk

class ChoosableUI:
    def __init__(self, master):
        self.master = master
        master.title("test")
        master.geometry('800x800')

        self.choices = ["Colour", "Days", "Places"]
        self.word_choice = ctk.CTkSegmentedButton(master, values=self.choices, command=self.clicker)
        self.word_choice.pack(pady=40)
        self.word_choice.set("Colour")
        print(self.word_choice.get())

    def clicker(self, value):
        print(value)

if __name__ == "__main__":
    root = ctk.CTk()
    app = ChoosableUI(root)
    root.mainloop()
