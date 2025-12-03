import tkinter as tk
from tkinter import  messagebox
result= None
def calculate_bmi(h_v_entry, h_u_entry, w_v_entry, w_u_entry):
    global result

    try:
        h = float(h_v_entry.get())
        w = float(w_v_entry.get())
        uh = h_u_entry.get().lower()
        uw = w_u_entry.get().lower()

    except ValueError:
        messagebox.showerror("Input Error", "Height and Weight must be numbers.")
        return

    if uh == "f":
        h = h * 0.3048
    elif uh != "m":
        messagebox.showerror("Input Error", "Invalid height unit. Use 'f' or 'm'.")
        return

    if uw == "p":
        w = w * 0.45359
    elif uw != "k":
        messagebox.showerror("Input Error", "Invalid weight unit. Use 'p' or 'k'.")
        return

    if h > 0:
        bmi_score = round(w / (h * h), 2)
    else:
        messagebox.showerror("Error", "Height must be greater than zero.")
        return

    if bmi_score < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi_score <= 24.9:
        category = "Healthy weight"
    elif 25 <= bmi_score <= 29.9:
        category = "Overweight"
    elif 30 <= bmi_score <= 39.9:
        category = "Obesity"
    else:
        category = "Severe Obesity"

    output_text = f"Your BMI: {bmi_score}\nCategory: {category}"
    result.config(text=output_text)

def setupgui():
    root=tk.Tk()
    root.title("BMI CALCULATOR")
    BG_COLOR = "#ADD8E6"
    LABEL_COLOR = "#4682B4"
    root.configure(bg=BG_COLOR)

    root.grid_columnconfigure(1, weight=1)
    root.grid_columnconfigure(2, weight=1)
    root.grid_columnconfigure(3, weight=1)
    root.grid_rowconfigure(1, weight=1)
    root.grid_rowconfigure(4, weight=1)

    tk.Label(root, text="Height Unit (f/m):",bg=BG_COLOR,font=('Arial', 16, 'bold')).grid(row=0, column=0, padx=10, pady=5, sticky='w')
    h_u_entry=tk.Entry(root,width=5)
    h_u_entry.grid(row=0,column=1,padx=10,pady=5)

    tk.Label(root, text="Weight Unit (p/k):",bg=BG_COLOR,font=('Arial', 16, 'bold')).grid(row=1, column=0, padx=10, pady=5, sticky='w')
    w_u_entry=tk.Entry(root,width=5)
    w_u_entry.grid(row=1,column=1,padx=10,pady=5)

    tk.Label(root,text="Enter height:",bg=BG_COLOR,font=('Arial', 16, 'bold')).grid(row=0,column=2,padx=10,pady=5,sticky="ew")
    h_v_entry=tk.Entry(root,width=5)
    h_v_entry.grid(row=0,column=3,padx=10,pady=5)

    tk.Label(root,text="Enter weight:",bg=BG_COLOR,font=('Arial', 16, 'bold')).grid(row=1,column=2,padx=10,pady=5,sticky="ew")
    w_v_entry=tk.Entry(root,width=5)
    w_v_entry.grid(row=1,column=3,padx=10,pady=5)

    calculate_button = tk.Button(root, text="Calculate BMI",bg=LABEL_COLOR,fg="white",
                                 command=lambda: calculate_bmi(h_v_entry, h_u_entry, w_v_entry, w_u_entry))
    calculate_button.grid(row=2, column=0, columnspan=4, pady=10)
    global result
    result = tk.Label(root, text="Enter values and click Calculate.", font=('Arial', 22, 'bold'))
    result.grid(row=3, column=0, columnspan=4, pady=5,sticky='nsew')

    root.mainloop()
if __name__=='__main__':
    setupgui()
