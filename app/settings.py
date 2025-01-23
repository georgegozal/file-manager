import tkinter as tk
from pathlib import Path


class SettingsPage(tk.Frame):
    def __init__(self, controller):
        super().__init__(controller)
        self.controller = controller

        self.label = tk.Label(self, text="This is the Settings Page", font=("Helvetica", 16))
        self.label.pack(pady=20)

        # self.go_back_button = tk.Button(self, text="Go Back to Home", 
        #                                 command=lambda: controller.show_frame("HomePage"))
        # self.go_back_button.pack()
        self.current_directory = str(Path.home())
