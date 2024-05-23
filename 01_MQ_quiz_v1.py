class daysQuiz:
    def __init__(self, english_word, maori_word):
        self.english_word = english_word
        self.maori_word = maori_word
        days_list.append(self)
    
    def display_words(self):
        print("")
        print(f"English word: {self.english_word}")
        print(f"Maori word: {self.maori_word}")

class coloursQuiz:
    def __init__(self, english_word, maori_word):
        self.english_word = english_word
        self.maori_word = maori_word
        days_list.append(self)
    
    def display_words(self):
        print("")
        print(f"English word: {self.english_word}")
        print(f"Maori word: {self.maori_word}")

def generate_questions():
    import csv
    for filename in filenames:
        with open(filename, newline='') as csvfile:
            filereader = csv.reader(csvfile, delimiter=',')
            for line in filereader:
                if line == "MaoriColourQuiz.csv":
                    coloursQuiz(line[0], line[1])
                elif line == "MaoriDaysQuiz.csv":
                    daysQuiz(line[0], line[1])
                # else:
                

filenames = ["MaoriColourQuiz.csv", "MaoriDaysQuiz.csv"]

days_list = []
colour_list = []

def print_daysQuestion():
    for words in colour_list:
        words.display_words()
def mainroutine():
    generate_questions()
    print_daysQuestion()

mainroutine()