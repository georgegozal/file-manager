from app import App


if __name__ == "__main__":
    app = App()
    app.title("File Manager")

    window_width = 600
    window_height = 500

    # Get the screen width and height
    screen_width = app.winfo_screenwidth()
    screen_height = app.winfo_screenheight()

    # Calculate the x and y position to center the window
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)

    # Set the geometry dynamically
    app.geometry(f"{window_width}x{window_height}+{x}+{y}")
    
    app.mainloop()