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
        self.word_ui = WordScreen(self)
        self.word_ui.grid(row=0, column=1)
        self.chooseCategory = ChoosableUI(self, self.word_ui)
        
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

class WordScreen(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color='transparent')
        self.label1 = ctk.CTkLabel(self, text="Words")
        self.label1.grid(row=1, column=1, padx=20, pady=20)
        self.word_list_label = ctk.CTkLabel(self, text="", justify="left")
        self.word_list_label.grid(row=2, column=1, padx=20, pady=20)

    def update_words(self, category):
        if category == "Colour":
            questions = colour_questions
        elif category == "Days":
            questions = days_questions
        elif category == "Places":
            questions = place_questions
        else:
            questions = []

        word_list = f"Words in {category}:\n"
        for question in questions:
            word_list += f"Maori word: {question.maori_word},   English word: {question.english_word}\n"
        
        self.word_list_label.configure(text=word_list)


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
