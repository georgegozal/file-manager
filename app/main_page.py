# import tkinter as tk
from tkinter import *
from pathlib import Path
import os


class MainPage(Frame):
    def __init__(self, controller):
        super().__init__(controller)
        self.controller = controller

        self.current_dir = str(Path.home())
        self.dirVar = StringVar()
        self.dirVar.set(self.current_dir)

        self.build_page()

    def build_page(self):
        self.top_frame = Frame(self)
        self.top_frame.grid(row=0, column=0, sticky='ew', padx=5, pady=5)
        self.top_frame.grid_columnconfigure(2, weight=1)

        self.back_btn = Button(self.top_frame, text="⇦", command=self.go_back)
        self.back_btn.grid(row=0, column=0, padx=(0, 5))

        self.home_btn = Button(self.top_frame, text="⌂", command=self.home)
        self.home_btn.grid(row=0, column=1, padx=(0, 5))

        self.entry_path = Entry(self.top_frame, width=90, textvariable=self.dirVar)
        self.entry_path.grid(row=0, column=2, sticky='ew')
        self.entry_path.bind('<Return>', self.path_changed)

    def path_changed(self, var):
        if os.path.exists(self.dirVar.get()):
            self.current_dir = self.dirVar.get()
        else:
            self.entry_path.delete(0, END)
            self.dirVar.set(self.current_dir)
    

    def go_back(self):
        pass

    def home(self):
        self.dirVar.set(str(Path.home()))
