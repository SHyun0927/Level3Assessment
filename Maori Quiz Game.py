"""
Maori Quiz Game.py
Final version of the program.
This code follows PEP8 standard.
"""
import csv
import random
import customtkinter as ctk


# Quiz Class, functionality for quiz
class Quiz:
    def __init__(self, questions, label1, quizlabel, scorelabel,
                 submission_textbox, submit_button, start_quiz_button,
                 chooseCategory):
        self.questions = questions
        self.current_question_index = 0
        self.label1 = label1
        self.quizlabel = quizlabel
        self.scorelabel = scorelabel
        self.submission_textbox = submission_textbox
        self.submit_button = submit_button
        self.start_quiz_button = start_quiz_button
        self.chooseCategory = chooseCategory
        self.score = 0
        self.quiz_finished = False

    # Initially sends to next qustion as first index is 0 (first question=1)
    def start(self):
        self.next_question()

    # displays next question until question runs out
    def next_question(self):
        self.current_question_index += 1
        if self.current_question_index < len(self.questions):
            self.current_question = self.questions[self.current_question_index]
            self.show_question()

        else:
            # if question finishes, calls the program the quiz is finished
            self.quiz_finished = True
            
            # Calls save_score function to save statistics
            self.save_score(self.score)
            self.current_question = None

            # DIsplay 'Quiz finished!' text on program.
            self.label1.configure(text="Quiz finished!", font=("Arial", 15))

            # submission textbox is disappeared
            self.submission_textbox.grid_forget()
            self.submit_button.grid_forget()

            # start quiz button appear again
            self.start_quiz_button.grid(row=2, column=1, padx=20, pady=20)
            self.chooseCategory.word_choice.configure(state='normal')

    # reads and show questions in english word.
    def show_question(self):
        question = self.current_question
        self.quizlabel.configure(text="Question: "
                              f"{question.english_word.title()}",
                              font=("Arial", 15, "bold"))

    # Tells the program if the user's answer is right
    def correct_answer(self, submission):
        # If user gets correct answer, display "correct" and add score by 1
        if self.current_question:
            if submission == self.current_question.maori_word:
                self.label1.configure(text="Correct!")
                self.score += 1

            # if not, show correct answer
            else:
                self.label1.configure(
                    text="Incorrect. The correct answer for "
                    f"{self.current_question.english_word} is "
                    f"{self.current_question.maori_word}."
                )
            self.scorelabel.configure(text=f"Score: {self.score}")

        # submission box is deleted at the end of each question
        self.submission_textbox.delete(0, 'end')
        # move to next questions
        self.next_question()

    # save score functionality.
    def save_score(self, score):
        # define which category he current question is.
        category = (self.current_question.category 
                    if self.current_question else self.questions[
            0].category)
        
        # with found category, find correct score file
        scores_file = f"MQ_{category}_score.txt"

        # open file, and read how many lines in the file.
        try:
            with open(scores_file, "r") as file:
                scores_data = file.readlines()

        except FileNotFoundError:
            scores_data = []

        # saves the score, the maximum line for this document is 10 lines.
        scores_data.append(str(score) + "\n")
        scores_data = scores_data[-10:]

        # write the new data to the file
        with open(scores_file, "w") as file:
            file.writelines(scores_data)


# Class to import questions to program
class QuizData:
    # defines the dictionary for questions
    def __init__(self):
        self.questions = []

    # allowing the program to read and import the questions from csv file
    def load_questions_from_csv(self, filename, category):
        # if correct filename and category has given, append questions
        # in given category.
        with open(filename, 'r') as file:
            reader = csv.reader(file)

            for row in reader:
                english_word, maori_word = row
                self.questions.append(
                    Question(english_word.strip(),
                             maori_word.strip(), category)
                )

    # finds the lists of words available from given category
    def get_questions_by_category(self, category):
        return [question for question in self.questions 
        if question.category == category]


# class defines the maori word, english word, and category.
class Question:
    def __init__(self, english_word, maori_word, category):
        self.english_word = english_word
        self.maori_word = maori_word
        self.category = category


# main base background application
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        # setting the title of the program to 'maori word quiz'
        self.title("Maori word quiz")

        # sets the size of the program to 700x450
        self.geometry("700x450")

        # sets the default theme to adapt the user's PC colour theme
        self._set_appearance_mode("System")

        # blocks the user to resize the window to prevent unexpected error
        self.resizable(False, False)

        # calls QuizScreen class initially
        self.quiz_ui = QuizScreen(self)
        self.quiz_ui.grid(row=0, column=1)

        # calls WordScreen, and ResultsScreen, but not showing.
        self.word_ui = WordScreen(self)
        self.result_ui = ResultsScreen(self)

        # calls Sidepanel class initially
        self.sidepanel = Sidepanel(self)
        self.sidepanel.grid(row=0, column=0, sticky="nsew")

        # calls ChoosableUI class initially
        self.chooseCategory = ChoosableUI(self, self.word_ui, self.result_ui)

        # configure grids for sidepanel and quiz/word/result screen.
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

    # allowing the program to close each window (quiz/word/result).
    def close_current_ui(self):
        for child in self.winfo_children():
            if isinstance(child, (QuizScreen, WordScreen, ResultsScreen)):
                child.grid_forget()

        # if quiz is not ongoing, category selection is available
        if not self.quiz_ui.quiz or self.quiz_ui.quiz.quiz_finished:
            self.chooseCategory.word_choice.configure(state='normal')

    # allows the program to decide when to disable category selection
    def check_and_disable_choosable_ui(self):
        # While quiz is ongoing, it is disbled
        if self.quiz_ui.quiz and not self.quiz_ui.quiz.quiz_finished:
            self.chooseCategory.word_choice.configure(state='disabled')
        # if not, selection is enabled
        else:
            self.chooseCategory.word_choice.configure(state='normal')


# functionality for panel in Left Hand Side.
class Sidepanel(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        # displays the main title on the top of the side panel.
        self.label = ctk.CTkLabel(
            self, text="Maori quiz", font=('Arial', 20, "bold"))
        self.label.grid(row=0, column=0, padx=15, pady=30, sticky="ew")

        # displays 'Quiz' button which redirects to quiz screen.
        self.quiz_button = ctk.CTkButton(
            self,
            text="Quiz",
            command=self.quiz_button_event,
            fg_color='transparent',
            corner_radius=0,
            hover_color=("gray70", "gray20"),
            text_color=("gray10", "gray90"),
            font=("Arial", 15, "bold"),
            border_spacing=10,
            height=50,
        )
        self.quiz_button.grid(row=1, column=0, sticky="ew")

        # displays 'Learn Word' button which redirects to word screen.
        self.word_button = ctk.CTkButton(
            self,
            text="Learn words",
            command=self.word_button_event,
            fg_color='transparent',
            corner_radius=0,
            hover_color=("gray70", "gray20"),
            text_color=("gray10", "gray90"),
            font=("Arial", 15, "bold"),
            border_spacing=10,
            height=50,
        )
        self.word_button.grid(row=2, column=0, sticky="ew")

        # displays 'Results' button which redirects to word screen.
        self.result_button = ctk.CTkButton(
            self,
            text="Results",
            command=self.result_button_event,
            fg_color='transparent',
            corner_radius=0,
            hover_color=("gray70", "gray20"),
            text_color=("gray10", "gray90"),
            font=("Arial", 15, "bold"),
            border_spacing=10,
            height=50,
        )
        self.result_button.grid(row=3, column=0, sticky="ew")

        # creates an empty frame to fit the whoe sidepanel within the height
        self.empty_frame = ctk.CTkLabel(self, text="")
        self.empty_frame.grid(row=4, column=0, padx=15, pady=57, sticky="ew")

        # Creates a dropbox for theme selection. 
        self.appearance_mode_menu = ctk.CTkOptionMenu(
            self, values=["System", "Light", "Dark"],
            command=self.change_appearance_mode_event,
            font=("Arial", 14)
        )
        self.appearance_mode_menu.grid(
            row=5, column=0, padx=15, pady=20, sticky="s")

    # functions when quiz button presed.
    def quiz_button_event(self):
        # calls close_current_ui function to close whatever tab is opened.
        self.master.close_current_ui()

        # opens quiz ui
        self.master.quiz_ui.grid(row=0, column=1)

        # let program to decide whether to disable/enable selection.
        self.master.check_and_disable_choosable_ui()

    # functions when word button presed.
    def word_button_event(self):
        # remove current ui
        self.master.close_current_ui()

        # load word ui
        self.master.word_ui.grid(row=0, column=1)

        # update the words to the current category selection
        self.master.word_ui.update_words(
            self.master.chooseCategory.word_choice.get())
        
        # if category selection was locked(quiz playing), enables the selection
        self.master.chooseCategory.word_choice.configure(state='normal')

    # functions when result button pressed.
    def result_button_event(self):\
        # remove current ui
        self.master.close_current_ui()

        # load up result ui
        self.master.result_ui.grid(row=0, column=1)

        # update the scores according to current category selection
        self.master.result_ui.update_scores(
            self.master.chooseCategory.word_choice.get())
        
        # unlock category selection
        self.master.chooseCategory.word_choice.configure(state='normal')

    # function to appearance mode change  button.
    def change_appearance_mode_event(self, new_appearance_mode):
        ctk.set_appearance_mode(new_appearance_mode)


# this class works for ui setting for quiz game.
class QuizScreen(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color='transparent')

        # sets label for welcome and correct/incorrect message
        self.label1 = ctk.CTkLabel(
            self, text="Welcome to Maori Quiz Game!", font=("Arial", 15))
        self.label1.grid(row=1, column=1, padx=20, pady=20)

        # sets a new label for display quiz
        self.quizlabel = ctk.CTkLabel(self, text="")
        self.quizlabel.grid(row=2, column=1)

        # sets a new label for displaying quiz
        self.scorelabel = ctk.CTkLabel(
            self, text="Score: 0", font=("Arial", 15, "bold"))
        self.scorelabel.grid(row=5, column=1)

        # adds a 'Start Quiz' button in quiz screen.
        self.start_quiz_button = ctk.CTkButton(
            self, text="Start Quiz", command=self.start_quiz,
            font=("Arial", 15, "bold"))
        self.start_quiz_button.grid(row=2, column=1, padx=20, pady=20)

        # sets enterbox to allow user to make an entry(answer) to the question.
        self.submission_textbox = ctk.CTkEntry(self)
        self.submission_textbox.grid(row=3, column=1, padx=20, pady=20)

        # sets a submit box to user confirms they are submitting the answer.
        self.submit_button = ctk.CTkButton(self, text="Submit",
                                           command=self.submit,
                                           font=("Arial", 15, "bold"))
        self.submit_button.grid(row=4, column=1, padx=20, pady=20)

        # initially forget enterbox and button
        # as the quiz starts when user presses 'Start Quiz' button.
        self.submission_textbox.grid_forget()
        self.submit_button.grid_forget()
        self.quiz = None

    # functions for prepare the question and start the quiz
    def start_quiz(self):
        # finds the current category when user pressed 'start quiz' button.
        category = self.master.chooseCategory.word_choice.get()

        # initially sets quizlabel to empty to ensure question does not appear
        # before the quiz starts
        self.quizlabel.configure(text="")

        # remove welcome message, finish message
        self.label1.configure(text="")

        # prepares questions for each category selection
        if category == "Colour":
            questions = colour_questions
        elif category == "Days":
            questions = days_questions
        else:
            questions = place_questions

        # shuffles the question so the user cannot predict
        random.shuffle(questions)

        # sends information to the quiz function.
        self.quiz = Quiz(
            questions,
            self.label1,
            self.quizlabel,
            self.scorelabel,
            self.submission_textbox,
            self.submit_button,
            self.start_quiz_button,
            self.master.chooseCategory
        )
        # calls 'start' function in quiz class.
        self.quiz.start()

        # grids enterbox, submit button 
        self.submission_textbox.grid(row=3, column=1, padx=20, pady=20)
        self.submit_button.grid(row=4, column=1, padx=20, pady=20)

        # make start quiz  button disppear after starting quiz.
        self.start_quiz_button.grid_forget()

        # set the category selection to be disabled.
        self.master.chooseCategory.word_choice.configure(
            state='disabled') 
        
        # at the start of the quiz, score display resets to 0.
        self.scorelabel.configure(text="Score: 0")

    # function to send enterbox's information
    # to correct_answer function in quiz class.
    def submit(self):
        submission = self.submission_textbox.get().lower()
        self.quiz.correct_answer(submission)


# class for learn words tab.
class WordScreen(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color='transparent')

        # initially sets a frame.
        self.word_table = ctk.CTkFrame(self)
        self.word_table.grid(row=1, column=0, padx=20, pady=20)

    # forget the previous words list they were displaying.
    def update_words(self, category):
        for widget in self.word_table.winfo_children():
            widget.destroy()

        # sets up top label.
        words_label = ctk.CTkLabel(
            self.word_table, text=f"Words in {category}:", font=("Arial", 16)
        )
        words_label.grid(row=0, column=0, columnspan=2, pady=(0, 10))

        # sets up left-hand-side column
        maori_label = ctk.CTkLabel(
            self.word_table, text="Maori words", font=("Arial", 15, "bold")
        )
        maori_label.grid(row=1, column=0, padx=10)

        # sets up right-hand-side column
        english_label = ctk.CTkLabel(
            self.word_table, text="English words", font=("Arial", 15, "bold")
        )
        english_label.grid(row=1, column=1, padx=10)

        # prepares questions for each category selection
        questions = []
        if category == "Colour":
            questions = colour_questions
        elif category == "Days":
            questions = days_questions
        else:
            questions = place_questions

        # adds words to the table
        for i, question in enumerate(questions, start=2):
            maori_word_label = ctk.CTkLabel(self.word_table,
                                            text=question.maori_word.title(),
                                            font=("Arial", 14))
            maori_word_label.grid(row=i, column=0, padx=10, pady=2)

            english_word_label = ctk.CTkLabel(self.word_table,
                                              text=(question.
                                                    english_word.title()),
                                                    font=("Arial", 14))
            english_word_label.grid(row=i, column=1, padx=10, pady=2)


# class for displaying result.
class ResultsScreen(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color='transparent')
        
        # initially sets up frame on grid.
        self.result_table = ctk.CTkFrame(self)
        self.result_table.grid(row=1, column=0, padx=20, pady=20)

    # forget the previous selection the user was watching.
    def update_scores(self, category):
        for widget in self.result_table.winfo_children():
            widget.destroy()

        # sets up top label
        scores_label = ctk.CTkLabel(
            self.result_table, text=f"Latest 10 Scores for {category}:",
            font=("Arial", 15)
        )
        scores_label.grid(row=0, column=0, columnspan=2, pady=0)

        # sets up left hand side column
        rank_label = ctk.CTkLabel(
            self.result_table, text="Trial", font=("Arial", 14, "bold")
        )
        rank_label.grid(row=1, column=0, padx=10)

        # sets up right hand side column
        score_label = ctk.CTkLabel(
            self.result_table, text="Score", font=("Arial", 14, "bold")
        )
        score_label.grid(row=1, column=1, padx=5)

        # finds correct score file for user's category selection.
        scores_file = f"MQ_{category}_score.txt"

        # opens scorefile, and read
        try:
            with open(scores_file, "r") as file:
                scores_data = file.readlines()
            
            # if there are no data, send message.
            if not scores_data:
                scores_data = ["No scores recorded yet!\n"]
        
        # if there are no file, send message.
        except FileNotFoundError:
            scores_data = ["No scores file available.\n"]

        # grabs information from first 10 lines of the data.
        scores_data = scores_data[-10:]
        # reverse the data so user can view from latest score.
        scores_data.reverse()

        # adds scores to the table
        for i, score in enumerate(scores_data, start=2):
            count = ctk.CTkLabel(self.result_table, text=f"{i - 1}",
                                font=("Arial", 13))
            count.grid(row=i, column=0, padx=10, pady=1)

            score_text = ctk.CTkLabel(self.result_table, text=score.strip(),
                                      font=("Arial", 13))
            score_text.grid(row=i, column=1, padx=10, pady=1)


# class for category selectoin.
class ChoosableUI(ctk.CTkSegmentedButton):
    def __init__(self, master, word_screen, results_screen):
        super().__init__(master)

        # choices for category selection
        self.choices = ["Colour", "Days", "Place"]

        # makes a segmented button with choices
        self.word_choice = ctk.CTkSegmentedButton(master, values=self.choices,
                                                  font=("Arial", 14))
        self.word_choice.place(relx=0.625, rely=0.04, anchor="n")

        # sets up default selection
        self.word_choice.set("Colour")

        # sets up callbacks
        self.word_screen = word_screen
        self.results_screen = results_screen

        # calls word_choice with current selection to display words.
        self.word_choice.configure(command=self.update_screens)

    # function for updating scores/words depends on category selection.
    def update_screens(self, value):
        self.word_screen.update_words(value)
        self.results_screen.update_scores(value)


# main routine
if __name__ == "__main__":
    # calls a quizdata class as quiz_data.
    quiz_data = QuizData()

    # loads questions from csv file, add category.
    quiz_data.load_questions_from_csv("MaoriDaysQuiz.csv", "Days")
    quiz_data.load_questions_from_csv("MaoriColourQuiz.csv", "Colour")
    quiz_data.load_questions_from_csv("MaoriPlacesQuiz.csv", "Place")

    # make a dictionary from the category.
    days_questions = quiz_data.get_questions_by_category("Days")
    colour_questions = quiz_data.get_questions_by_category("Colour")
    place_questions = quiz_data.get_questions_by_category("Place")

    # calls a base app as app variable
    app = App()
    # loops the functions in main class App()
    app.mainloop()
