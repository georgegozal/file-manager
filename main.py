from app import App
import os


if __name__ == "__main__":
    app = App()
    app.title(f"{os.environ.get('USER')} - File Manager")

    window_width = 850
    window_height = 650

    # Get the screen width and height
    screen_width = app.winfo_screenwidth()
    screen_height = app.winfo_screenheight()

    # Calculate the x and y position to center the window
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)

    # Set the geometry dynamically
    app.geometry(f"{window_width}x{window_height}+{x}+{y}")
    
    app.mainloop()