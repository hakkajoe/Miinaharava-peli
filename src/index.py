from tkinter import Tk
from ui.ui import UI


def main():
    """sets up tkinter window
    """
    window = Tk()
    window.title("Minesweeper")
    window.geometry("+550+250")

    ui_index = UI(window)
    ui_index.start()

    window.mainloop()


if __name__ == "__main__":
    main()
