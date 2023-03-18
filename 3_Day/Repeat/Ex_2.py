import tkinter as tk

class BMI_Calculator:
    def __init__(self, master):
        self.master = master
        master.title("BMI Calculator")

        # Create labels and entries for height and weight
        self.height_label = tk.Label(master, text="Enter your height in meters:")
        self.height_label.pack()
        self.height_entry = tk.Entry(master)
        self.height_entry.pack()

        self.weight_label = tk.Label(master, text="Enter your weight in kilograms:")
        self.weight_label.pack()
        self.weight_entry = tk.Entry(master)
        self.weight_entry.pack()

        # Create a button to calculate BMI
        self.calculate_button = tk.Button(master, text="Calculate BMI", command=self.calculate_bmi)
        self.calculate_button.pack()

        # Create a label to display the result
        self.result_label = tk.Label(master, font=("Helvetica", 16))
        self.result_label.pack()

    def calculate_bmi(self):
        height = float(self.height_entry.get())
        weight = float(self.weight_entry.get())
        bmi = round(weight / height ** 2, 2)

        # Set result label text and color based on BMI value
        if bmi <= 18.5:
            self.result_label.config(text=f"Your BMI is {bmi}, you are underweight.", fg="blue")
        elif bmi <= 24.9:
            self.result_label.config(text=f"Your BMI is {bmi}, you have a normal weight.", fg="green")
        elif bmi <= 29.9:
            self.result_label.config(text=f"Your BMI is {bmi}, you are overweight.", fg="orange")
        else:
            self.result_label.config(text=f"Your BMI is {bmi}, you are obese.", fg="red")

# Create a window
root = tk.Tk()

# Create an instance of BMI_Calculator class
bmi_calculator = BMI_Calculator(root)

# Run the window
root.mainloop()




import tkinter as tk

# class BMI_Calculator:
#     def __init__(self, master):
#         self.master = master
#         master.title("BMI Calculator")
#
#         # Create labels and entries for height and weight
#         self.height_label = tk.Label(master, text="Enter your height in meters:")
#         self.height_label.pack()
#         self.height_entry = tk.Entry(master)
#         self.height_entry.pack()
#
#         self.weight_label = tk.Label(master, text="Enter your weight in kilograms:")
#         self.weight_label.pack()
#         self.weight_entry = tk.Entry(master)
#         self.weight_entry.pack()
#
#         # Create a button to calculate BMI
#         self.calculate_button = tk.Button(master, text="Calculate BMI", command=self.calculate_bmi)
#         self.calculate_button.pack()
#
#         # Create a label to display the result
#         self.result_label = tk.Label(master, font=("Helvetica", 16))
#         self.result_label.pack()
#
#     def calculate_bmi(self):
#         height = float(self.height_entry.get())
#         weight = float(self.weight_entry.get())
#         bmi = round(weight / height ** 2, 2)
#
#         # Set result label text and color based on BMI value
#         if bmi <= 18.5:
#             self.result_label.config(text=f"Your BMI is {bmi}, you are underweight.", fg="blue")
#         elif bmi <= 24.9:
#             self.result_label.config(text=f"Your BMI is {bmi}, you have a normal weight.", fg="green")
#         elif bmi <= 29.9:
#             self.result_label.config(text=f"Your BMI is {bmi}, you are overweight.", fg="orange")
#         else:
#             self.result_label.config(text=f"Your BMI is {bmi}, you are obese.", fg="red")
#
# # Create a window
# root = tk.Tk()
#
# # Create an instance of BMI_Calculator class
# bmi_calculator = BMI_Calculator(root)
#
# # Run the window
# root.mainloop()
