import tkinter as tk
from tkinter import messagebox

def calculate_mpg():
    try:
        miles = float(miles_entry.get())
        gallons = float(gallons_entry.get())
        if gallons <= 0:
            raise ValueError("Gallons must be greater than zero.")
        mpg = miles / gallons
        result_label.config(text=f"Miles per Gallon: {mpg:.2f}")
    except ValueError as e:
        messagebox.showerror("Input Error", str(e)) 

#Main window

root = tk.Tk()
root.title("MPG Calculator")

#Gallon input

tk.Label(root, text="Gallons of gas: ").grid(row=0, column=0, padx=10, pady=5, sticky='e')
gallons_entry = tk.Entry(root)
gallons_entry.grid(row=0, column=1, padx=10, pady=5)

#Miles input

tk.Label(root, text="Miles driven: ").grid(row=1, column=0, padx=10, pady=5, sticky='e')
miles_entry = tk.Entry(root)
miles_entry.grid(row=1, column=1, padx=10, pady=5)

#Calculate button

calculate_button = tk.Button(root, text="Calculate MPG", command=calculate_mpg)
calculate_button.grid(row=2, columnspan=2, pady=10)

#Result label

result_label = tk.Label(root, text="Miles per Gallon: ")
result_label.grid(row=3, columnspan=2, pady=5)  

root.mainloop()