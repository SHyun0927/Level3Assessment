"""
05_MQ_sidepanel_v1.py
This script is used to generate the side panel for the program's dashboard.
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
        self.sidepanel = Sidepanel(self)
        self.sidepanel.grid(row=0, column=0, sticky="nsew")

        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)


class Sidepanel(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.label = ctk.CTkLabel(self, text="Maori quiz", font=("Arial", 16))
        self.label.grid(row=0, column=0, padx=15, pady=30, sticky="ew")

        self.quiz_button = ctk.CTkButton(
            self,
            text="Quiz",
            command=self.quiz_button_event,
            fg_color='transparent',
            corner_radius=0,
            hover_color=("gray70", "gray20"),
            text_color=("gray10", "gray90"),
            height=50,
        )
        self.quiz_button.grid(row=1, column=0, sticky="ew")
        self.word_button = ctk.CTkButton(
            self,
            text="Learn words",
            command=self.word_button_event,
            fg_color='transparent',
            corner_radius=0,
            hover_color=("gray70", "gray20"),
            text_color=("gray10", "gray90"),
            height=50,
        )
        self.word_button.grid(row=2, column=0, sticky="ew")

        self.result_button = ctk.CTkButton(
            self,
            text="Results",
            command=self.result_button_event,
            fg_color='transparent',
            corner_radius=0,
            hover_color=("gray70", "gray20"),
            text_color=("gray10", "gray90"),
            border_spacing=10,
            height=50,
        )
        self.result_button.grid(row=3, column=0, sticky="ew")

        self.empty_frame = ctk.CTkLabel(self, text="")
        self.empty_frame.grid(row=4, column=0, padx=15, pady=57, sticky="ew")

        self.appearance_mode_menu = ctk.CTkOptionMenu(
            self, values=["System", "Light", "Dark"], 
            command=self.change_appearance_mode_event,
        )
        self.appearance_mode_menu.grid(row=5, column=0, padx=15, pady=20, sticky="s")

    def quiz_button_event(self):
        print("Quiz button pressed.")
    def word_button_event(self):
        print("Word button pressed.")

    def result_button_event(self):
        print("Result button pressed.")

    def change_appearance_mode_event(self, new_appearance_mode):
        ctk.set_appearance_mode(new_appearance_mode)

if __name__ == "__main__":
    app = App()
    app.mainloop()
