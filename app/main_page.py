# import tkinter as tk
from tkinter import *
from pathlib import Path
import os
from pprint import pprint
import subprocess
from functools import partial


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
        self.top_frame.pack()
        self.top_frame.grid_columnconfigure(2, weight=1)

        self.back_btn = Button(self.top_frame, text="⇦", command=self.go_back)
        self.back_btn.grid(row=0, column=0, padx=(0, 5))

        self.home_btn = Button(self.top_frame, text="⌂", command=self.home)
        self.home_btn.grid(row=0, column=1, padx=(0, 5))

        self.entry_path = Entry(self.top_frame, width=90, textvariable=self.dirVar)
        self.entry_path.grid(row=0, column=2, sticky='ew')
        self.entry_path.bind('<Return>', self.path_changed)

        places_row = Label(self.top_frame, text="Places", bg='grey', anchor='w', padx=10, fg="white", font=("Arial", 12))
        places_row.grid(row=1, column=0, columnspan=3, sticky='ew', padx=2)

        self.left_frame = Frame(self)
        self.left_frame.pack(side=LEFT, padx=15, fill='y')

        DIRECTORIES = (
            'Desktop',
            'Trash',
            'Documents',
            'Music',
            'Pictures',
            'Videos',
            'Downloads',
        )

        for address in DIRECTORIES:
            btn = Button(
                self.left_frame,
                text=address,
                anchor='nw',
                relief='flat',
                bg='#f0f0f0',
                activebackground='#e0e0e0',
                pady=5,
                width=10,
                command=lambda p=address: self.path_changed(var=None, path=p)
            )
            btn.pack(fill='x', padx=(5), pady=(0, 0))
        
        # Create Window for listing files
        self.right_frame = Frame(self, bg='white', width=680, height=570)
        self.right_frame.pack(side=LEFT)

    def path_changed(self, var, path=None):
        if path:
            print(path)
            if path == 'Trash':
                self.dirVar.set('~/.local/share/Trash/files')
            else:
                self.dirVar.set(str(Path.home() / path))
        if path == 'Trash' or os.path.exists(self.dirVar.get()):
            self.current_dir = self.dirVar.get()
        else:
            self.entry_path.delete(0, END)
            self.dirVar.set(self.current_dir)

        return self.list_directory()

    def list_directory(self):
        # Create and arrange file names in a grid (horizontal + vertical)
        row, column = 0, 0
        max_columns = 3

        files = os.scandir(self.dirVar.get())
        for file in files:
            file = File(file)
        
            file_frame = Frame(self.right_frame, bd=2, relief="groove", padx=10, pady=5, bg="lightgray")
            file_frame.grid(row=row, column=column, padx=5, pady=5, sticky="nsew")
            file_frame.bind("<Button-1>", lambda event, current_file=file: self.left_click(env=event, file=current_file))
            # file_frame.bind("<Button-1>", partial(self.left_click, file))


            label = Label(file_frame, text=file.name, bg="lightgray")
            label.pack()
            label.bind("<Button-1>", lambda event, current_file=file: self.left_click(event, current_file))

            
            # Update row and column for next item
            column += 1
            if column >= max_columns:
                column = 0
                row += 1
        
        # Make sure columns stretch to fill the frame
        for i in range(max_columns):
            self.right_frame.grid_columnconfigure(i, weight=1, uniform="equal")

    def left_click(self, env, file):
        print("left_click", file)
        
        # Use xdg-open to open the file with the default application
        try:
            # subprocess.run(['xdg-open', file.path], check=True)
            subprocess.run(['vlc', file.path])
        except subprocess.CalledProcessError as e:
            print(f"Error opening file {file.path}: {e}")



    def go_back(self):
        pass

    def home(self):
        self.dirVar.set(str(Path.home()))


class File:
    def __init__(self, file):
        self.file = file
        self.name = file.name
        self.path = file.path
        self.size = self.set_file_size()
        self.is_file = self.file.is_file()
        self.is_dir = self.file.is_dir()
        self.is_symlink = self.file.is_symlink()

    def set_file_size(self):
        kilobytes = self.file.stat().st_size / 1024
        if kilobytes > 1000:
            megabytes = kilobytes / 1024
            if megabytes > 1000:
                gigabytes = megabytes / 1024
                return {'size': round(gigabytes, 2), 'unit': 'gig'}
            return {'size': round(megabytes, 2), 'unit': 'mb'}
        return {'size': round(kilobytes, 2), 'unit': 'kb'}
