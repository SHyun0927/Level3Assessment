"""
01_MQ_import_quiz_v2.py
first version of the program. 
simplified three classes into one class.
"""
import csv

class QuizData:
    def __init__(self):
        self.questions = []

    def load_questions_from_csv(self, filename, category):
        with open(filename, 'r') as file:
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


def main():
    quiz_data = QuizData()
    quiz_data.load_questions_from_csv("MaoriDaysQuiz.csv", "Days")
    quiz_data.load_questions_from_csv("MaoriColourQuiz.csv", "Colour")
    quiz_data.load_questions_from_csv("MaoriPlacesQuiz.csv", "Place")

    days_questions = quiz_data.get_questions_by_category("Days")
    colour_questions = quiz_data.get_questions_by_category("Colour")
    place_questions = quiz_data.get_questions_by_category("Place")

    print("\nMaori Days Questions:")
    for question in days_questions:
        print(f"{question.english_word}: {question.maori_word}, ({question.category})")

    print("\nMaori Places Questions:")
    for question in place_questions:
        print(f"{question.english_word}: {question.maori_word}, ({question.category})")

    print("\nMaori Colours Questions:")
    for question in colour_questions:
        print(f"{question.english_word}: {question.maori_word}, ({question.category})")

if __name__ == "__main__":
    main()
