import tkinter as tk
from tkinter import messagebox

#dictionary of services and each cost

services = {
    "Oil Change": 30.00,
    "Lube Job": 20.00,
    "Radiator Flush": 40.00,
    "Transmission Flush": 100.00,
    "Inspection": 35.00,
    "Muffer Replacement": 200.00,
    "Tire Rotation": 20.00,
}

def calculate_total():
    total = 0.0
    for service, var in service_vars.items():
        if var.get():
            total += services[service]
        label_total.config(text=f"Total Cost: ${total:.2f}")
    
#Main window

root = tk.Tk()
root.title("Joe's Automotive Services")

#Checkbuttons

service_vars = {}
for i, (service, cost) in enumerate(services.items()):
    var = tk.BooleanVar()
    chk = tk.Checkbutton(root, text=f"{service} (${cost:.2f})", variable=var)
    chk.grid(row=i, column=0, sticky='w', padx=10, pady=2)
    service_vars[service] = var

#Calculate button

calculate_button = tk.Button(root, text="Calculate Total", command=calculate_total)
calculate_button.grid(row=len(services), column=0, pady=10)

#Total label

label_total = tk.Label(root, text="Total Cost: $0.00")
label_total.grid(row=len(services)+1, column=0, pady=5)

root.mainloop()