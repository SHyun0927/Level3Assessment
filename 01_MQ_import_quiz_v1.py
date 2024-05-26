class daysQuiz:
    def __init__(self, english_word, maori_word):
        self.english_word = english_word
        self.maori_word = maori_word
        days_list.append(self)
    
    def display_days(self):
        print("")
        print(f"Days word: {self.english_word}")
        print(f"Maori word: {self.maori_word}")

class coloursQuiz:
    def __init__(self, english_word, maori_word):
        self.english_word = english_word
        self.maori_word = maori_word
        colour_list.append(self)
    
    def display_colour(self):
        print("")
        print(f"Colour word: {self.english_word}")
        print(f"Maori word: {self.maori_word}")

class placeQuiz:
    def __init__(self, english_word, maori_word):
        self.english_word = english_word
        self.maori_word = maori_word
        place_list.append(self)
    
    def display_place(self):
        print("")
        print(f"Place word: {self.english_word}")
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
                else:
                    placeQuiz(line[0], line[1])

                

filenames = ["MaoriColourQuiz.csv", "MaoriDaysQuiz.csv", "MaoriNZPlaceQuiz.csv"]

days_list = []
colour_list = []
place_list = []

def print_daysQuestion():
    for words in days_list:
        words.display_days()

def print_colourQuestion():
    for words in colour_list:
        words.display_colour()

def print_placeQuestion():
    for words in place_list:
        words.display_place()
def mainroutine():
    generate_questions()
    print_daysQuestion()
    print_colourQuestion()
    print_placeQuestion()

mainroutine()