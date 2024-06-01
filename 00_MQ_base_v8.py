"""
00_MQ_base_v8.py
Added quiz function.
"""
import customtkinter as ctk
import csv
import random

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

        self.chooseCategory = ChoosableUI(self, self.result_ui)


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
        self.label1 = ctk.CTkLabel(self, text="")

        # Place the label in the center of the frame using grid
        self.label1.grid(row=1, column=1, padx=20, pady=20)

        self.label2 = ctk.CTkLabel(self, text="")

        self.label2.grid(row=2, column=1)

        self.scorelabel = ctk.CTkLabel(self, text="Score: 0")

        self.scorelabel.grid(row=5, column=1)

        # Create the start quiz button
        self.start_quiz_button = ctk.CTkButton(self, text="Start Quiz", command=self.start_quiz)

        # Place the start quiz button in the center of the frame using grid
        self.start_quiz_button.grid(row=2, column=1, padx=20, pady=20)

        # Create the submission textbox
        self.submission_textbox = ctk.CTkEntry(self)

        # Place the submission textbox below the start quiz button using grid
        self.submission_textbox.grid(row=3, column=1, padx=20, pady=20)

        # Create the submit button
        self.submit_button = ctk.CTkButton(self, text="Submit", command=self.submit)

        # Place the submit button below the submission textbox using grid
        self.submit_button.grid(row=4, column=1, padx=20, pady=20)

        # Hide the submission textbox and submit button initially
        self.submission_textbox.grid_forget()
        self.submit_button.grid_forget()

    def start_quiz(self):
        # Get the selected category from the ChoosableUI
        category = self.master.chooseCategory.word_choice.get()

        # Get the questions for the selected category
        if category == "Colour":
            questions = colour_questions
        elif category == "Days":
            questions = days_questions
        elif category == "Places":
            questions = place_questions
        else:
            raise ValueError(f"Invalid category: {category}")
        
        random.shuffle(questions)

        # Create a new Quiz class instance with the selected questions
        self.quiz = Quiz(questions, self.label1, self.label2, self.scorelabel, self.submission_textbox, self.submit_button, self.start_quiz_button, self.master.chooseCategory)

        # Start the quiz
        self.quiz.start()

        # Show the submission textbox and submit button
        self.submission_textbox.grid(row=3, column=1, padx=20, pady=20)
        self.submit_button.grid(row=4, column=1, padx=20, pady=20)

        # Hide the start quiz button
        self.start_quiz_button.grid_forget()

        # Disable the chooseCategory widget while the quiz is in progress
        self.master.chooseCategory.configure(state='disabled')

        self.scorelabel.configure(text="Score: 0 ")

    def submit(self):
        # Get the user's submission from the submission textbox
        submission = self.submission_textbox.get()

        # Check if the submission is correct
        self.quiz.correct_answer(submission)

    def submit(self):
        # Get the user's submission from the submission textbox
        submission = self.submission_textbox.get()

        # Check if the submission is correct
        self.quiz.correct_answer(submission)
        
# ... (similar code for WordScreen and ResultsScreen)
# This class forming the UI when the user has chosen 'Word'
class WordScreen(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color='transparent')

        # Create the label
        self.label1 = ctk.CTkLabel(self, text="WordFrame")

        # Place the label in the center of the frame using grid
        self.label1.grid(row=1, column=1, padx=20, pady=20)

# This class forming the UI when the user has chosen 'Results'
class ResultsScreen(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color='transparent')

        self.days_score_label = ctk.CTkLabel(self, text="TestLabel")
        self.days_score_label.grid(row=0, column=0, padx=20, pady=20)
# This class forming the Choosable UI for the user.
class ChoosableUI(ctk.CTkSegmentedButton):
    def __init__(self, master, results_screen):
        super().__init__(master)
        self.choices = ["Colour", "Days", "Places"]
        self.word_choice = ctk.CTkSegmentedButton(master, values=self.choices)
        self.word_choice.place(relx=0.625, rely=0.04, anchor="n")
        self.word_choice.set("Colour")
        self.results_screen = results_screen
        self.word_choice.configure(command=self.update_results_screen)

    def update_results_screen(self, value):
        self.results_screen.update_scores()
class Quiz:
    def __init__(self, questions, label1, label2, scorelabel, submission_textbox, submit_button, start_quiz_button, chooseCategory):
        self.questions = questions
        self.current_question_index = 0
        self.label1 = label1
        self.label2 = label2
        self.scorelabel = scorelabel
        self.submission_textbox = submission_textbox
        self.submit_button = submit_button
        self.start_quiz_button = start_quiz_button
        self.chooseCategory = chooseCategory
        self.score = 0  # Initialize the score variable

    def start(self):
        # Show the first question
        self.next_question()

    def next_question(self):
        # Move to the next question
        self.current_question_index += 1
        if self.current_question_index < len(self.questions):
            self.current_question = self.questions[self.current_question_index]
            self.show_question()
        else:
            self.current_question = None
            self.label1.configure(text="Quiz finished!")
            self.submission_textbox.grid_forget()
            self.submit_button.grid_forget()
            self.start_quiz_button.grid(row=2, column=1, padx=20, pady=20)
            self.chooseCategory.configure(state='normal')

    def show_question(self):
        # Show the current question in the QuizScreen
        question = self.current_question
        self.label2.configure(text=f"Question: {question.english_word}")

    def correct_answer(self, submission):
        # Check if the submission is correct
        if submission == self.current_question.maori_word:
            # Show a message indicating that the answer is correct
            self.label1.configure(text="Correct!")
            # Increment the score
            self.score += 1  # Corrected syntax
            self.save_score(self.score)
            # Show the score
            self.scorelabel.configure(text=f"Score: {self.score}")
        else:
            # Show a message indicating that the answer is incorrect
            self.label1.configure(text=f"Incorrect. The correct answer for {self.current_question.english_word} is {self.current_question.maori_word}.")
        # Clear the submission textbox
        self.submission_textbox.delete(0, 'end')
        # Move to the next question
        self.next_question()

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
    quiz_data.load_questions_from_csv("MaoriPlacesQuiz.csv", "Place")
    days_questions = quiz_data.get_questions_by_category("Days")
    colour_questions = quiz_data.get_questions_by_category("Colour")
    place_questions = quiz_data.get_questions_by_category("Place")

    app = App()
    app.mainloop()