"""
00_MQ_base_v7.py
updating functions for getting questions from multiple csv files
Updated appearance_mode issue when initial launch of the program, theme is not applied properly
Fixed issue when the program is set as a light mode, text on the sidepanel cannot be visible
"""
import customtkinter as ctk
import csv

# This is base class for application using CustomTKinter
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        # Makes the title to certain text within " "
        self.title("Maori word quiz")
        # Adjusts the size of window. ("(width)x(height)")
        self.geometry("700x450")
        # Sets the program's default theme to Dark mode
        self._set_appearance_mode("System")
        # does not allow program window to be resized by user
        self.resizable(False, False)
        # calls the class Frame1()
        self.quiz_ui = QuizScreen(self)
        
        self.quiz_ui.grid(row=0, column=1)

        self.word_ui = WordScreen(self)

        self.result_ui = ResultsScreen(self)

        self.sidepanel = Sidepanel(self)

        self.sidepanel.grid(row=0, column=0, sticky="nsew")

        self.chooseCategory = ChoosableUI(self)

        self.grid_columnconfigure(0, weight=0)

        self.grid_columnconfigure(1, weight=1)

        self.grid_rowconfigure(0, weight=1)

    def close_current_ui(self):
        for child in self.winfo_children():
            if isinstance(child, (QuizScreen, WordScreen, ResultsScreen)):
                child.grid_forget()

# This class forming the left-hand-side of the UI allowing the user
# To have appropriate number of information in single screen.
class Sidepanel(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        # Creates a label "Maori quiz"
        self.label = ctk.CTkLabel(self, text="Maori quiz", font=('Arial', 17))

        # Places the label on first row of the grid setted up in App() class.
        self.label.grid(row=0, column=0, padx=15, pady=30, sticky="ew")

        # Creates a button 'Quiz' written inside.
        self.quiz_button = ctk.CTkButton(self, text="Quiz", command=self.quiz_button_event, fg_color='transparent', corner_radius=0, hover_color=("gray70", "gray20"), text_color=("gray10", "gray90"), border_spacing=10, height=50)

        # Places the button on second row of the grid setted up in App() class.
        self.quiz_button.grid(row=1, column=0, sticky="ew")

        # Creates a button 'Learn words' written inside.
        self.word_button = ctk.CTkButton(self, text="Learn words", command=self.word_button_event, fg_color='transparent', corner_radius=0, hover_color=("gray70", "gray20"), text_color=("gray10", "gray90"), border_spacing=10, height=50)

        # Places the button on third row of the grid.
        self.word_button.grid(row=2, column=0, sticky="ew")

        # Creates a button 'Results' written inside.
        self.result_button = ctk.CTkButton(self, text="Results", command=self.result_button_event, fg_color='transparent', corner_radius=0, hover_color=("gray70", "gray20"), text_color=("gray10", "gray90"), border_spacing=10, height=50)

        # Places the button on fourth row of the grid.
        self.result_button.grid(row=3, column=0, sticky="ew")

        # Creates empty label
        self.empty_frame = ctk.CTkLabel(self, text="")

        # Places empty grid between results and appearance mode
        # to make the left-hand-side panel fill the screen fully
        self.empty_frame.grid(row=4, column=0, padx=15, pady=57, sticky="ew")

        # Creates a OptionMenu button which allows the user to change theme
        # of the program.
        self.appearance_mode_menu = ctk.CTkOptionMenu(self, values=["System","Light", "Dark"], command=self.change_appearance_mode_event)

        # Places the button on sixth row of the grid.
        self.appearance_mode_menu.grid(row=5, column=0, padx=15, pady=20, sticky="s")



    # These definitions below will be updated later!
    # updates the data to quiz selection'
    def quiz_button_event(self):
        print("Quiz button clicked")
        self.master.close_current_ui()
        self.master.quiz_ui.grid(row=0, column=1)  # show QuizScreen


    def word_button_event(self):
        print("Word button clicked")
        self.master.close_current_ui()
        self.master.word_ui.grid(row=0, column=1)  # show WordScreen
    def result_button_event(self):
        print("Result button clicked")
        self.master.close_current_ui()
        self.master.result_ui.grid(row=0, column=1)  # show ResultsScreen
    # updates the colour theme of the program. (working!)
    def change_appearance_mode_event(self, new_appearance_mode):
        # This allows the program to change between light and dark mode
        ctk.set_appearance_mode(new_appearance_mode)

# This class forming the right-panel of the UI allowing the user
# To have appropriate number of information in single screen.

# This class forming the UI when the user has chosen 'Quiz'

class QuizScreen(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color='transparent')

        # Create the label
        self.testlabel = ctk.CTkLabel(self, text="QuizFrame")

        # Place the label in the center of the frame using grid
        self.testlabel.grid(row=1, column=1, padx=20, pady=20)

# ... (similar code for WordScreen and ResultsScreen)
# This class forming the UI when the user has chosen 'Word'
class WordScreen(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color='transparent')

        # Create the label
        self.testlabel = ctk.CTkLabel(self, text="WordFrame")

        # Place the label in the center of the frame using grid
        self.testlabel.grid(row=1, column=1, padx=20, pady=20)

# This class forming the UI when the user has chosen 'Results'
class ResultsScreen(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color='transparent')

        # Create the label
        self.testlabel = ctk.CTkLabel(self, text="ResultFrame")

        # Place the label in the center of the frame using grid
        self.testlabel.grid(row=1, column=1, padx=20, pady=20)

# This class forming the Choosable UI for the user.
class ChoosableUI(ctk.CTkSegmentedButton):
    def __init__(self, master):
        super().__init__(master)
        self.choices = ["Colour", "Days", "Places"]
        self.word_choice = ctk.CTkSegmentedButton(master, values=self.choices, command=self.clicker)
        self.word_choice.place(relx=0.65, rely=0.04, anchor="n")
        self.word_choice.set("Colour")

        print(self.word_choice.get())

    def clicker(self, value):
        print(value)

class QuizData:
    def __init__(self):
        self.questions = []

    def load_questions_from_csv(self, filename, category):
        with open(filename, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                english_word, maori_word = row
                self.questions.append(Question(english_word.strip(), maori_word.strip(), category))

    def get_questions_by_category(self, category):
        return [question for question in self.questions if question.category == category]

class Question:
    def __init__(self, english_word, maori_word, category):
        self.english_word = english_word
        self.maori_word = maori_word
        self.category = category

# creates an instance of App class
if __name__ == "__main__":
    quiz_data = QuizData()
    quiz_data.load_questions_from_csv("MaoriDaysQuiz.csv", "Days")
    quiz_data.load_questions_from_csv("MaoriColourQUiz.csv", "Colour")
    quiz_data.load_questions_from_csv("MaoriNZPlaceQuiz.csv", "Place")
    days_questions = quiz_data.get_questions_by_category("Days")
    colour_questions = quiz_data.get_questions_by_category("Colour")
    place_questions = quiz_data.get_questions_by_category("Place")

    app = App()
    app.mainloop()