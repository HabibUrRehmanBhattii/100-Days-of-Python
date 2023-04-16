import tkinter as tk
from typing import Tuple


class Calculator(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master

        # Add widgets to interface
        self.create_widgets()

    def create_widgets(self):
        """Add all the necessary widgets for the calculator."""
        # Number Label
        number_label = tk.Label(text='0', font=('Arial', 50))
        number_label.grid(row=1, column=2)

        # Operators Buttons
        operators = ('*', '+', '-', '/')
        operator_frame = tk.Frame(self, bd=3)
        operator_button_frame = tk.Frame(operator_frame)

        operator_buttons = []
        for oper in operators:
            button = tk.Button(operator_button_frame, text=oper)
            button.grid(column=0, row=operator_button_frame.winfo_height())
            operator_buttons.append(button)

        operator_frame.grid(row=4, column=0, rowspan=3)

        # Equal Button
        equal_button = tk.Button(self, text="=", command=lambda: None)
        equal_button.grid(column=4, row=4)

        # Clear Button
        clear_button = tk.Button(self, text="Clear", command=lambda: None)
        clear_button.grid(column=3, row=7)


if __name__ == "__main__":
    app = tk.Tk()
    app.title("Calculator")
    app.geometry("800x600")
    calculator = Calculator(app)
    calculator.grid(row=2, column=0, rowspan=9)
    app.mainloop()
