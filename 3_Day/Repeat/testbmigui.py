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

        # Create radio buttons for selecting gender
        self.gender_label = tk.Label(master, text="Select your gender:")
        self.gender_label.pack()
        self.gender_var = tk.StringVar(value="male")
        self.gender_male = tk.Radiobutton(master, text="Male", variable=self.gender_var, value="male")
        self.gender_female = tk.Radiobutton(master, text="Female", variable=self.gender_var, value="female")
        self.gender_male.pack()
        self.gender_female.pack()

        # Create a slider for selecting age
        self.age_label = tk.Label(master, text="Select your age:")
        self.age_label.pack()
        self.age_var = tk.IntVar(value=30)
        self.age_slider = tk.Scale(master, from_=1, to=100, orient=tk.HORIZONTAL, variable=self.age_var)
        self.age_slider.pack()

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

        # Calculate BMR (Basal Metabolic Rate) based on gender, age, and weight
        gender = self.gender_var.get()
        age = self.age_var.get()
        if gender == "male":
            bmr = 88.36 + (13.4 * weight) + (4.8 * height * 100) - (5.7 * age)
        else:
            bmr = 447.6 + (9.2 * weight) + (3.1 * height * 100) - (4.3 * age)

        # Calculate TDEE (Total Daily Energy Expenditure) based on BMR and activity level
        activity_level = 1.2  # Sedentary (little or no exercise)
        if bmi <= 18.5:
            activity_level = 1.375  # Lightly active (light exercise or sports 1-3 days a week)
        elif bmi <= 24.9:
            activity_level = 1.55  # Moderately active (moderate exercise or sports 3-5 days a week)
        elif bmi <= 29.9:
            activity_level = 1.725  # Very active (hard exercise or sports 6-7 days a week)
        else:
            activity_level = 1.9  # Extra active (very hard exercise or sports, physical job or training twice a day)

        tdee = bmr * activity_level

        # Set result label text and color based on BMI value
        if bmi <= 18.5:
            self.result_label.config(text=f"Your BMI is {bmi}, you are underweight.", fg="yellow")
        elif bmi <= 24.9:
            self.result_label.config(text=f"Your BMI is {bmi}, you have a normal weight.", fg="green")
        elif bmi <= 29.9:
            self.result_label.config(text=f"Your BMI is {bmi}, you are overweight.", fg="orange")
        else:
            self.result_label.config(text=f"Your BMI is {bmi}, you are obese.", fg="red")

        # Add BMR and TDEE information to the result label
        self.result_label.config(text=self.result_label.cget("text") +
                                      f"\nYour BMR is {round(bmr, 2)} kcal/day and your TDEE is {round(tdee, 2)} kcal/day.")


# Create a window
root = tk.Tk()

# Create an instance of BMI_Calculator class
bmi_calculator = BMI_Calculator(root)

# Run the window
root.mainloop()
