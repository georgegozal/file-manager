import tkinter as tk
import os
from .settings import SettingsPage
from .main_page import MainPage


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.settings = None

        self.setup_gui()
        
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

    def setup_gui(self):
        # Create menu bar
        self.create_menu()

        # Create frames for different pages
        self.frames = {}
        for F in (MainPage, SettingsPage):
            page_name = F.__name__
            frame = F(controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

            # if page_name == "SettingsPage":
            #     self.settings = frame

        self.show_frame("MainPage")

    def create_menu(self):
        """Create a dropdown menu for navigation."""
        self.menu = tk.Menu(self)
        self.config(menu=self.menu)
        self.menu.add_command(label="Home", command=lambda: self.show_frame("MainPage"))
        self.menu.add_command(label="Settings", command=lambda: self.show_frame("SettingsPage"))


    def show_frame(self, name):
        self.frames[name].tkraise()





app = App()
app.title(f"{os.environ.get('USER')} - File Manager")

window_width = 850
window_height = 650
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

# Set the geometry dynamically
app.geometry(f"{window_width}x{window_height}+{x}+{y}")
app.mainloop()
