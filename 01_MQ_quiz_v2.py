import csv

class Question:
    def __init__(self, english_word, maori_word, category):
        self.english_word = english_word
        self.maori_word = maori_word
        self.category = category

def load_questions_from_csv(filename, category):
    questions = []
    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            english_word, maori_word = row
            questions.append(Question(english_word.strip(), maori_word.strip(), category))
    return questions

def main():
    days_questions = load_questions_from_csv('MaoriDaysQuiz.csv', 'Days')
    places_questions = load_questions_from_csv('MaoriNZPlaceQuiz.csv', 'Places')
    colours_questions = load_questions_from_csv('MaoriColourQuiz.csv', 'Colours')

    print("Maori Days Questions:")
    for question in days_questions:
        print(f"{question.english_word}: {question.maori_word} ({question.category})")

    print("\nMaori Places Questions:")
    for question in places_questions:
        print(f"{question.english_word}: {question.maori_word} ({question.category})")

    print("\nMaori Colours Questions:")
    for question in colours_questions:
        print(f"{question.english_word}: {question.maori_word} ({question.category})")

if __name__ == "__main__":
    main()
