"""
03_MQ_show_results_v1.py
display results.
"""
import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Maori word quiz")
        self.geometry("700x450")
        self._set_appearance_mode("System")
        self.resizable(False, False)
        self.result_ui = ResultsScreen(self)
        
        self.result_ui.grid(row=0, column=1)
        self.chooseCategory = ChoosableUI(self, self.result_ui)
        
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

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

    self.score_label.configure(text=f"Latest 10 Scores for {category}:\n{score_text}")


class ChoosableUI(ctk.CTkSegmentedButton):
    def __init__(self, master, results_screen):
        super().__init__(master)
        self.choices = ["Colour", "Days", "Places"]
        self.word_choice = ctk.CTkSegmentedButton(master, values=self.choices)
        self.word_choice.place(relx=0.625, rely=0.04, anchor="n")
        self.word_choice.set("Colour")
        self.results_screen = results_screen
        self.word_choice.configure(command=self.update_results_screen)
        self.update_results_screen("Colour")

    def update_results_screen(self, value):
        self.results_screen.update_scores(value)

if __name__ == "__main__":
    app = App()
    app.mainloop()
