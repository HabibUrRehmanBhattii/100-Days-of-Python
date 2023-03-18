import tkinter as tk


def check_leap_year(event=None):
    year = int(year_entry.get())
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                result_label.config(text='Leap year')
            else:
                result_label.config(text='Not Leap year')
        else:
            result_label.config(text='Leap year')
    else:
        result_label.config(text='Not Leap year')


# Create the main window
root = tk.Tk()
root.title('Leap Year Checker')

# Create label and an entry widget for the year input
year_label = tk.Label(root, text='Enter a year')
year_label.pack()
year_entry = tk.Entry(root)
year_entry.pack()

# Create a button to check the leap year
check_button = tk.Button(root, text='Check', command=check_leap_year)
check_button.pack()

# Create a label to display the result
result_label = tk.Label(root, text='')
result_label.pack()

# Bind the Enter key to the year entry widget
year_entry.bind('<Return>', check_leap_year)

# Start the main event loop
root.mainloop()
