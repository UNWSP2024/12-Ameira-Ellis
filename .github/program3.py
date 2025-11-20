import tkinter as tk
from tkinter import messagebox

#Rate Defintions

Rates = {
    "Daytime (6AM-5:59PM)": 0.02,
    "Evening (6PM-11:59PM)": 0.12,
    "Off-Peak (12AM-5:59AM)": 0.05
}

def calculate_charge():
    try:
        minutes = int(minutes_entry.get())
        if minutes < 0:
            raise ValueError("Minutes must be a non-negative integer.")
        rate = Rates[rate_var.get()]
        total_charge = minutes * rate
        result_label.config(text=f"Total Charge: ${total_charge:.2f}")
    except ValueError as e:
        messagebox.showerror("Input Error", str(e))

#Main window

root = tk.Tk()
root.title("Long-Distance Call Calculator")

#Minutes input

tk.Label(root, text="Call Duration (mintues): ").grid(row=0, column=0, padx=10, pady=5, sticky='e')
minutes_entry = tk.Entry(root)
minutes_entry.grid(row=0, column=1, padx=10, pady=5)

#Rate selection

rate_var = tk.StringVar(value="Daytime (6AM-5:59PM)")
tk.Label(root, text="Select Rate: ").grid(row=1, column=0, padx=10, pady=5, sticky='e')

rate_frame = tk.Frame(root)
rate_frame.grid(row=1, column=1, padx=10, pady=5)

for rate in Rates.keys():
    tk.Radiobutton(rate_frame, text=rate, variable=rate_var, value=rate).pack(anchor='w')
    
#Calculate button

tk.Button(root, text="Calculate Charge", command=calculate_charge).grid(row=2, columnspan=2, pady=10)   

#Result label

result_label = tk.Label(root, text="Total Charge: $0.00")
result_label.grid(row=3, columnspan=2, pady=5)      

root.mainloop()

