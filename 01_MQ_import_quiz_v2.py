import csv

class Question:
    def __init__(self, english_word, maori_word):
        self.english_word = english_word
        self.maori_word = maori_word

def load_questions_from_csv(filename):
    questions = []
    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            english_word, maori_word = row
            questions.append(Question(english_word.strip(), maori_word.strip()))
    return questions

def main():
    days_questions = load_questions_from_csv('MaoriDaysQuiz.csv')
    places_questions = load_questions_from_csv('MaoriNZPlaceQuiz.csv')
    colours_questions = load_questions_from_csv('MaoriColourQuiz.csv')

    print("Maori Days Questions:")
    for question in days_questions:
        print(f"{question.english_word}: {question.maori_word}")

    print("\nMaori Places Questions:")
    for question in places_questions:
        print(f"{question.english_word}: {question.maori_word})")

    print("\nMaori Colours Questions:")
    for question in colours_questions:
        print(f"{question.english_word}: {question.maori_word}")

if __name__ == "__main__":
    main()
