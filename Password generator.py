import tkinter as tk
from tkinter import messagebox

def generate_password_gui():
    length = int(length_entry.get())
    use_upper = upper_var.get()
    use_digits = digits_var.get()
    use_symbols = symbols_var.get()
    
    password = generate_password(length, use_upper, use_digits, use_symbols)
    result_label.config(text=f"Generated Password: {password}")

# Create GUI
root = tk.Tk()
root.title("Password Generator")

tk.Label(root, text="Password Length:").pack()
length_entry = tk.Entry(root)
length_entry.pack()

upper_var = tk.BooleanVar(value=True)
digits_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)

tk.Checkbutton(root, text="Include Uppercase", variable=upper_var).pack()
tk.Checkbutton(root, text="Include Digits", variable=digits_var).pack()
tk.Checkbutton(root, text="Include Symbols", variable=symbols_var).pack()

generate_button = tk.Button(root, text="Generate Password", command=generate_password_gui)
generate_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
