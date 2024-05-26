"""
00_MQ_base_v4.py
Improving the UI aesthetics. 
Changing the Frame1's button as transparent, adding hover colours to look more simpler
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
        # does not allow program window to be resized by user
        self.resizable(False, False)
        # calls the class Frame1()
        self.frame = Frame1(self)
        # sets the grid for the class Frame1()
        self.frame.grid(row=0, column=0, sticky="nsew")
        

# This class forming the left-hand-side of the UI allowing the user
# To have appropriate number of information in single screen.
class Frame1(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        # Creates a label "Maori quiz"
        self.label = ctk.CTkLabel(self, text="Maori quiz", font=('Arial', 17))

        # Places the label on first row of the grid setted up in App() class.
        self.label.grid(row=0, column=0, padx=15, pady=30, sticky="ew")

        # Creates a button 'Quiz' written inside.
        self.quiz_button = ctk.CTkButton(self, text="Quiz", command=self.quiz_button_event, fg_color = 'transparent', corner_radius=0, hover_color = 'grey20', border_spacing = 10, height = 50)

        # Places the button on second row of the grid setted up in App() class.
        self.quiz_button.grid(row=1, column=0, sticky="ew")

        # Creates a button 'Quiz' written inside.
        self.word_button = ctk.CTkButton(self, text="Learn words", command=self.word_button_event, fg_color = 'transparent', corner_radius=0, hover_color = 'grey20', border_spacing = 10, height = 50)

        # Places the button on third row of the grid.
        self.word_button.grid(row=2, column=0, sticky="ew")

        # Creates a button 'Results' written inside.
        self.result_button = ctk.CTkButton(self, text="Results", command=self.result_button_event, fg_color = 'transparent', corner_radius=0, hover_color = 'grey20', border_spacing = 10, height = 50)

        # Places the button on fourth row of the grid.
        self.result_button.grid(row=3, column=0,sticky="ew")

        # Creates empty label
        self.empty_frame = ctk.CTkLabel(self, text = "")
        
        # Places empty grid between results anad appearance mode
        # to make the left-hand-side panel fill the screen fully
        self.empty_frame.grid(row=4, column=0, padx=15, pady=57, sticky="ew")

        # Creates a OptionMenu button which allows the user to change theme
        # of the program.
        self.appearance_mode_menu = ctk.CTkOptionMenu(self, values=["Dark", "Light"], command=self.change_appearance_mode_event)
        
        # Places the button on sixth row of the grid.
        self.appearance_mode_menu.grid(row=5, column=0, padx=15, pady=20, sticky="s")

    # These definitions below will be updated later!

    # updates the data to quiz selection' 
    def quiz_button_event(self):
        print("Quiz button clicked")

    # updates the screen list of words
    def word_button_event(self):
        print("Word button clicked")

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



