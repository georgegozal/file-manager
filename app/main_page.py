from tkinter import *
from pathlib import Path
import os


class MainPage(Frame):
    def __init__(self, controller):
        super().__init__(controller)
        self.controller = controller

        self.current_dir = StringVar()
        self.current_dir.set(str(Path.home()))

        self.build_page()
        self.show_sidebar()
        # self.list_current_directory()

    def build_page(self):
        self.top_frame = Frame(self)
        self.top_frame.grid(row=0, column=0, sticky='ew', padx=5, pady=5)
        self.top_frame.grid_columnconfigure(2, weight=1)

        self.back_btn = Button(self.top_frame, text="⇦", command=self.go_back)
        self.back_btn.grid(row=0, column=0, padx=(0, 5))

        self.home_btn = Button(self.top_frame, text="⌂")
        self.home_btn.grid(row=0, column=1, padx=(0, 5))

        self.current_path = Entry(self.top_frame, width=90, textvariable=self.current_dir)
        self.current_path.grid(row=0, column=2, sticky='ew')
        self.current_path.bind('<Return>', self.path_changed)  


    def show_sidebar(self):
        # Left sidebar container
        self.sidebar_container = Frame(self)
        self.sidebar_container.grid(row=1, column=0, sticky='nsew')
        self.sidebar_container.grid_propagate(False)  # Prevent frame from shrinking
        
        # Configure the container to expand vertically
        self.sidebar_container.grid_rowconfigure(0, weight=1)
        self.sidebar_container.grid_columnconfigure(0, weight=1)
        
        # Set fixed width for sidebar
        self.sidebar_container.configure(width=200)
        
        # Create the actual sidebar with a canvas for scrolling if needed
        self.sidebar_canvas = Canvas(self.sidebar_container, bg='#f0f0f0', highlightthickness=0)
        self.sidebar_canvas.grid(row=0, column=0, sticky='nsew')
        
        # Add a scrollbar
        self.sidebar_scrollbar = Scrollbar(self.sidebar_container, orient="vertical", 
                                        command=self.sidebar_canvas.yview)
        self.sidebar_scrollbar.grid(row=0, column=1, sticky='ns')
        
        # Configure the canvas
        self.sidebar_canvas.configure(yscrollcommand=self.sidebar_scrollbar.set)
        
        # Create the frame for content
        self.sidebar = Frame(self.sidebar_canvas, bg='#f0f0f0')
        
        # Add the frame to the canvas
        self.sidebar_canvas.create_window((0, 0), window=self.sidebar, anchor='nw', width=200)
        
        # Quick access header
        Label(self.sidebar, text="Quick Access", bg='#f0f0f0', 
            font=('Arial', 10, 'bold')).pack(pady=(10,5), anchor='w', padx=10)
    
        # Common directories
        common_dirs = {
            "Downloads": str(Path.home() / "Downloads"),
            "Documents": str(Path.home() / "Documents"),
            "Pictures": str(Path.home() / "Pictures"),
            "Videos": str(Path.home() / "Videos"),
            "Music": str(Path.home() / "Music")
        }
        
        for name, path in common_dirs.items():
            btn = Button(self.sidebar, 
                        text=f"📁 {name}", 
                        command=lambda p=path: self.navigate_to(p),
                        anchor='w',
                        relief='flat',
                        bg='#f0f0f0',
                        activebackground='#e0e0e0',
                        pady=5,
                        width=25)  # Fixed width for buttons
            btn.pack(fill='x', padx=5, pady=1)
    
        # Configure scrolling
        self.sidebar.bind('<Configure>', self._configure_sidebar_scroll)
        
        # Add a separator
        Frame(self.sidebar, height=1, bg='#d0d0d0').pack(fill='x', pady=10)
        
        # You can add more sections here
        Label(self.sidebar, text="Favorites", bg='#f0f0f0', 
            font=('Arial', 10, 'bold')).pack(pady=(10,5), anchor='w', padx=10)
        
        # Fill remaining space
        Frame(self.sidebar, bg='#f0f0f0').pack(expand=True, fill='both')

    def _configure_sidebar_scroll(self, event):
        # Update the scroll region when the sidebar contents change
        self.sidebar_canvas.configure(scrollregion=self.sidebar_canvas.bbox("all"))


    def list_current_directory(self):
        path = os.chdir(self.current_dir.get())
        _list = os.listdir()
        for item in _list:
            file = File(path, item)


    def go_back(self):
        pass

    def path_changed(self, event=None):
        path = self.current_dir.get()
        if os.path.exists(path):
            self.list_current_directory()
        else:
            self.current_dir.set(str(Path.home()))
            self.list_current_directory()

class File:
    def __init__(self, path, file):
        self.path = path
        self.file = file
        full_path = os.path.join(os.getcwd(), self.file)
        
        if os.path.isfile(full_path):
            print(f"{self.file} is a file.")
        elif os.path.isdir(full_path):
            print(f"{self.file} is a directory.")
        elif os.path.islink(full_path):
            print(f"{self.file} is a symbolic link.")
        else:
            print(f"{self.file} is of an unknown type.")
