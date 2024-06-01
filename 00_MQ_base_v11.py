"""
00_MQ_base_v11.py
Updated its functionality of the ChoosableUI while playing Quiz.
Now ChoosalbeUI's selection is disabled while user is playing quiz, ensuring the program proceeds correctly.
Bug fix: fixed bug where ResultScreen class loads the textfile, it opens wrong textfile and does not load scores.
How: changed selection in ChoosalbeUI "Places" was not the same as the category when words being loaded in program ("Place")
"""
import customtkinter as ctk
import csv
import random

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Maori word quiz")
        self.geometry("700x450")
        self._set_appearance_mode("System")
        self.resizable(False, False)
        
        self.quiz_ui = QuizScreen(self)
        self.quiz_ui.grid(row=0, column=1)

        self.word_ui = WordScreen(self)
        self.result_ui = ResultsScreen(self)
        self.sidepanel = Sidepanel(self)
        self.sidepanel.grid(row=0, column=0, sticky="nsew")
        self.chooseCategory = ChoosableUI(self, self.word_ui, self.result_ui)
        
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

    def close_current_ui(self):
        for child in self.winfo_children():
            if isinstance(child, (QuizScreen, WordScreen, ResultsScreen)):
                child.grid_forget()

class Sidepanel(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.label = ctk.CTkLabel(self, text="Maori quiz", font=('Arial', 17))
        self.label.grid(row=0, column=0, padx=15, pady=30, sticky="ew")
        self.quiz_button = ctk.CTkButton(self, text="Quiz", command=self.quiz_button_event, fg_color='transparent', corner_radius=0, hover_color=("gray70", "gray20"), text_color=("gray10", "gray90"), border_spacing=10, height=50)
        self.quiz_button.grid(row=1, column=0, sticky="ew")
        self.word_button = ctk.CTkButton(self, text="Learn words", command=self.word_button_event, fg_color='transparent', corner_radius=0, hover_color=("gray70", "gray20"), text_color=("gray10", "gray90"), border_spacing=10, height=50)
        self.word_button.grid(row=2, column=0, sticky="ew")
        self.result_button = ctk.CTkButton(self, text="Results", command=self.result_button_event, fg_color='transparent', corner_radius=0, hover_color=("gray70", "gray20"), text_color=("gray10", "gray90"), border_spacing=10, height=50)
        self.result_button.grid(row=3, column=0, sticky="ew")
        self.empty_frame = ctk.CTkLabel(self, text="")
        self.empty_frame.grid(row=4, column=0, padx=15, pady=57, sticky="ew")
        self.appearance_mode_menu = ctk.CTkOptionMenu(self, values=["System","Light", "Dark"], command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=5, column=0, padx=15, pady=20, sticky="s")

    def quiz_button_event(self):
        self.master.close_current_ui()
        self.master.quiz_ui.grid(row=0, column=1)

    def word_button_event(self):
        self.master.close_current_ui()
        self.master.word_ui.grid(row=0, column=1)
        self.master.word_ui.update_words(self.master.chooseCategory.word_choice.get())

    def result_button_event(self):
        self.master.close_current_ui()
        self.master.result_ui.grid(row=0, column=1)
        self.master.result_ui.update_scores(self.master.chooseCategory.word_choice.get())

    def change_appearance_mode_event(self, new_appearance_mode):
        ctk.set_appearance_mode(new_appearance_mode)

class QuizScreen(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color='transparent')
        self.label1 = ctk.CTkLabel(self, text="")
        self.label1.grid(row=1, column=1, padx=20, pady=20)
        self.label2 = ctk.CTkLabel(self, text="")
        self.label2.grid(row=2, column=1)
        self.scorelabel = ctk.CTkLabel(self, text="Score: 0")
        self.scorelabel.grid(row=5, column=1)
        self.start_quiz_button = ctk.CTkButton(self, text="Start Quiz", command=self.start_quiz)
        self.start_quiz_button.grid(row=2, column=1, padx=20, pady=20)
        self.submission_textbox = ctk.CTkEntry(self)
        self.submission_textbox.grid(row=3, column=1, padx=20, pady=20)
        self.submit_button = ctk.CTkButton(self, text="Submit", command=self.submit)
        self.submit_button.grid(row=4, column=1, padx=20, pady=20)
        self.submission_textbox.grid_forget()
        self.submit_button.grid_forget()

    def start_quiz(self):
        category = self.master.chooseCategory.word_choice.get()
        if category == "Colour":
            questions = colour_questions
        elif category == "Days":
            questions = days_questions
        elif category == "Place":
            questions = place_questions
        else:
            raise ValueError(f"Invalid category: {category}")
        
        random.shuffle(questions)
        self.quiz = Quiz(questions, self.label1, self.label2, self.scorelabel, self.submission_textbox, self.submit_button, self.start_quiz_button, self.master.chooseCategory)
        self.quiz.start()
        self.submission_textbox.grid(row=3, column=1, padx=20, pady=20)
        self.submit_button.grid(row=4, column=1, padx=20, pady=20)
        self.start_quiz_button.grid_forget()
        self.master.chooseCategory.word_choice.configure(state='disabled')  # Disable the segmented button
        self.scorelabel.configure(text="Score: 0")

    def submit(self):
        submission = self.submission_textbox.get().lower()
        self.quiz.correct_answer(submission)

class WordScreen(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color='transparent')
        self.word_table = ctk.CTkFrame(self)
        self.word_table.grid(row=1, column=0, padx=20, pady=20)

    def update_words(self, category):
        for widget in self.word_table.winfo_children():
            widget.destroy()

        words_label = ctk.CTkLabel(self.word_table, text=f"Words in {category}:", font=("Arial", 16))
        words_label.grid(row=0, column=0, columnspan=2, pady=(0, 10))

        maori_label = ctk.CTkLabel(self.word_table, text="Maori words", font=("Arial", 14, "bold"))
        maori_label.grid(row=1, column=0, padx=10)
        english_label = ctk.CTkLabel(self.word_table, text="English words", font=("Arial", 14, "bold"))
        english_label.grid(row=1, column=1, padx=10)

        questions = []
        if category == "Colour":
            questions = colour_questions
        elif category == "Days":
            questions = days_questions
        elif category == "Place":
            questions = place_questions

        for i, question in enumerate(questions, start=2):
            maori_word_label = ctk.CTkLabel(self.word_table, text=question.maori_word.title())
            maori_word_label.grid(row=i, column=0, padx=10, pady=2)
            english_word_label = ctk.CTkLabel(self.word_table, text=question.english_word.title())
            english_word_label.grid(row=i, column=1, padx=10, pady=2)

class ResultsScreen(ctk.CTkFrame):
  def __init__(self, master):
    super().__init__(master, fg_color='transparent')
    self.score_label = ctk.CTkLabel(self, text="Top Scores")
    self.score_label.grid(row=0, column=0, padx=20, pady=20)

  def update_scores(self, category):
    scores_file = f"MQ_{category}_score.txt"
    try:
      with open(scores_file, "r") as file:
        scores_data = file.readlines()
      if not scores_data:
          scores_data = ["No scores recorded yet!\n"]
    except FileNotFoundError:
      scores_data = ["No scores file available.\n"]

    scores_data = scores_data[-10:]  # Keep only the 10 latest scores
    scores_data.reverse()  # Reverse the order to display from 10th to 1st

    # Create formatted score text with numbering
    score_text = ""
    for i, score in enumerate(scores_data, start=1):
      score_text += f"Score {i}: {score}"

    self.score_label.configure(text=f"Top Scores for {category}:\n{score_text}")

class ChoosableUI(ctk.CTkSegmentedButton):
    def __init__(self, master, word_screen, results_screen):
        super().__init__(master)
        self.choices = ["Colour", "Days", "Place"]
        self.word_choice = ctk.CTkSegmentedButton(master, values=self.choices)
        self.word_choice.place(relx=0.625, rely=0.04, anchor="n")
        self.word_choice.set("Colour")
        self.word_screen = word_screen
        self.results_screen = results_screen
        self.word_choice.configure(command=self.update_screens)

    def update_screens(self, value):
        self.word_screen.update_words(value)
        self.results_screen.update_scores(value)

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
        self.score = 0
        self.quiz_finished = False

    def start(self):
        self.next_question()

    def next_question(self):
        self.current_question_index += 1
        if self.current_question_index < len(self.questions):
            self.current_question = self.questions[self.current_question_index]
            self.show_question()
        else:
            self.quiz_finished = True
            self.save_score(self.score)
            self.current_question = None
            self.label1.configure(text="Quiz finished!")
            self.submission_textbox.grid_forget()
            self.submit_button.grid_forget()
            self.start_quiz_button.grid(row=2, column=1, padx=20, pady=20)
            self.chooseCategory.word_choice.configure(state='normal')  # Enable the segmented button

    def show_question(self):
        question = self.current_question
        self.label2.configure(text=f"Question: {question.english_word.title()}")

    def correct_answer(self, submission):
        if self.current_question:
            if submission == self.current_question.maori_word:
                self.label1.configure(text="Correct!")
                self.score += 1
            else:
                self.label1.configure(text=f"Incorrect. The correct answer for {self.current_question.english_word} is {self.current_question.maori_word}.")
            self.scorelabel.configure(text=f"Score: {self.score}")
        self.submission_textbox.delete(0, 'end')
        self.next_question()

    def save_score(self, score):
        category = self.current_question.category if self.current_question else self.questions[0].category
        scores_file = f"MQ_{category}_score.txt"
        try:
            with open(scores_file, "r") as file:
                scores_data = file.readlines()
        except FileNotFoundError:
            scores_data = []

        scores_data.append(str(score) + "\n")
        scores_data = scores_data[-10:]

        with open(scores_file, "w") as file:
            file.writelines(scores_data)

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

if __name__ == "__main__":
    quiz_data = QuizData()
    quiz_data.load_questions_from_csv("MaoriDaysQuiz.csv", "Days")
    quiz_data.load_questions_from_csv("MaoriColourQuiz.csv", "Colour")
    quiz_data.load_questions_from_csv("MaoriPlacesQuiz.csv", "Place")
    days_questions = quiz_data.get_questions_by_category("Days")
    colour_questions = quiz_data.get_questions_by_category("Colour")
    place_questions = quiz_data.get_questions_by_category("Place")

    app = App()
    app.mainloop()
