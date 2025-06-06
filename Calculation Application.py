'''
Num1 = float(input("Enter First Number:"))
Num2 = float(input("Enter Second Number:"))

a = input("1. Addition\n2. Substraction\n3. Multiplication\n4. Division\nEnter your choice:")
if a == '1':
    print(Num1 + Num2)
elif a == '2':
    print(Num1 - Num2)
elif a == '3':
    print(Num1 * Num2)
elif a == '4':
    print(Num1/Num2)
else:
    print("Invalid option")
    
'''
'''
def calculator():
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    
    # Take input from the user
    choice = input("Enter the number corresponding to your choice (1/2/3/4): ")

    if choice in ['1', '2', '3', '4']:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input. Please enter numerical values.")
            return
        
        if choice == '1':
            print(f"The result of addition is: {num1 + num2}")
        elif choice == '2':
            print(f"The result of subtraction is: {num1 - num2}")
        elif choice == '3':
            print(f"The result of multiplication is: {num1 * num2}")
        elif choice == '4':
            if num2 != 0:
                print(f"The result of division is: {num1 / num2}")
            else:
                print("Error! Division by zero is not allowed.")
    else:
        print("Invalid choice. Please select a valid option.")

# Run the calculator
calculator()
'''


import tkinter as tk

# Function to update the expression in the input field
def press(key):
    current = input_text.get()
    input_text.set(current + str(key))

# Function to evaluate the expression
def evaluate():
    try:
        result = eval(input_text.get())
        input_text.set(result)
    except Exception as e:
        input_text.set("Error")

# Function to clear the input field
def clear():
    input_text.set("")

# Create the main window
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")
root.resizable(False, False)

# Input field
input_text = tk.StringVar()
input_field = tk.Entry(root, textvariable=input_text, font=('Arial', 20), bd=10, insertwidth=2, width=14, justify='right')
input_field.grid(row=0, column=0, columnspan=4)

# Button layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

# Add buttons to the window
for (text, row, col) in buttons:
    if text == "=":
        tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 14), bg="lightgreen", command=evaluate).grid(row=row, column=col, sticky='nsew')
    elif text == "C":
        tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 14), bg="lightcoral", command=clear).grid(row=row, column=col, sticky='nsew')
    else:
        tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 14), command=lambda t=text: press(t)).grid(row=row, column=col, sticky='nsew')

# Adjust row and column weights
for i in range(5):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

# Run the application
root.mainloop()
