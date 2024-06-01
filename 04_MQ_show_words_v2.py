import customtkinter as ctk
import csv

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Maori word quiz")
        self.geometry("700x450")
        self._set_appearance_mode("System")
        self.resizable(False, False)
        self.word_ui = WordScreen(self)

        self.word_ui.grid(row=0, column=1)
        self.chooseCategory = ChoosableUI(self, self.word_ui)
        
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

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
        elif category == "Places":
            questions = place_questions

        for i, question in enumerate(questions, start=2):
            maori_word_label = ctk.CTkLabel(self.word_table, text=question.maori_word.title())
            maori_word_label.grid(row=i, column=0, padx=10, pady=2)
            english_word_label = ctk.CTkLabel(self.word_table, text=question.english_word.title())
            english_word_label.grid(row=i, column=1, padx=10, pady=2)


class ChoosableUI(ctk.CTkSegmentedButton):
    def __init__(self, master, word_screen):
        super().__init__(master)
        self.choices = ["Colour", "Days", "Places"]
        self.word_choice = ctk.CTkSegmentedButton(master, values=self.choices)
        self.word_choice.place(relx=0.625, rely=0.04, anchor="n")
        self.word_choice.set("Colour")
        self.word_screen = word_screen
        self.word_choice.configure(command=self.update_screens)
        self.update_screens("Colour")

    def update_screens(self, value):
        self.word_screen.update_words(value)


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
