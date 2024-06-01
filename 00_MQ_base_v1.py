"""
00_MQ_base_v1.py
creating base window of the program
"""
import customtkinter as ctk

# This is base class for application using CustomTKinter
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        # Makes the title to certain text within " ""
        self.title("Maori word quiz")
        # Adjusts the size of window. ("(width)x(height)")
        self.geometry("700x450")

# This  allows the program to run and loop
if __name__ == "__main__":
    # defines variable 'app' as a class 'App()'
    app = App()
    # runs the program
    app.mainloop()



