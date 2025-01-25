from tkinter import *
from .main_page import MainPage
from .settings import SettingsPage


class App(Tk):
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

        self.show_frame("MainPage")

    def create_menu(self):
        """Create a dropdown menu for navigation."""
        self.menu = Menu(self)
        self.config(menu=self.menu)
        self.menu.add_command(label="Home", command=lambda: self.show_frame("MainPage"))
        self.menu.add_command(label="Settings", command=lambda: self.show_frame("SettingsPage"))


    def show_frame(self, name):
        self.frames[name].tkraise()
