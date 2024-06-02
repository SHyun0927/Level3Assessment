"""
00_MQ_base_v2.py
creating basic side panel of the program
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
        # Sets the program's default theme to Dark mode
        self._set_appearance_mode("Dark")
        # calls the class Frame1()
        self.frame = Frame1(self)
        # sets the grid for the class Frame1()
        self.frame.grid(row=0, column=0, sticky="nsew")
        

# This class forming the left-hand-side of the UI allowing the user
# To have appropriate number of information in single screen.
class Frame1(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        # Creates a button 'home' written inside.
        self.home_button = ctk.CTkButton(self, text="Home", command=self.home_button_event)
        # Places the button on first row of the grid setted up in App() class.
        self.home_button.grid(row=0, column=0, padx=20, pady=20, sticky="ew")

        # Creates a button 'Quiz' written inside.
        self.quiz_button = ctk.CTkButton(self, text="Quiz", command=self.quiz_button_event)

        # Places the button on second row of the grid.
        self.quiz_button.grid(row=1, column=0, padx=20, pady=20, sticky="ew")

        # Creates a button 'Results' written inside.
        self.result_button = ctk.CTkButton(self, text="Results", command=self.result_button_event)

        # Places the button on third row of the grid.
        self.result_button.grid(row=2, column=0, padx=20, pady=20, sticky="ew")

        # Creates a OptionMenu button which allows the user to change theme
        # of the program.
        self.appearance_mode_menu = ctk.CTkOptionMenu(self, values=["Dark", "Light"],
                                                    command=self.change_appearance_mode_event)
        
        # Places the button on fourth row of the grid.
        self.appearance_mode_menu.grid(row=3, column=0, padx=20, pady=20, sticky="s")

    # These definitions below will be updated later!

    # updates the data on screen as 'home' 
    def home_button_event(self):
        print("Home button clicked")

    # updates the screen to quiz selection
    def quiz_button_event(self):
        print("Quiz button clicked")

    # updates the screen to results screen
    def result_button_event(self):
        print("Result button clicked")

    # updates the colour theme of the program. (working!)
    def change_appearance_mode_event(self, new_appearance_mode):
        # This allows the program to change between light and dark mode
        ctk.set_appearance_mode(new_appearance_mode)

# This  allows the program to run and loop+
if __name__ == "__main__":
    # defines variable 'app' as a class 'App()'
    app = App()
    # runs the app
    app.mainloop()



