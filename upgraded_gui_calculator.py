
# Import required modules
from customtkinter import *
import math
from tkinter import simpledialog  # For getting user input

# Configuration for the standard buttons
button_config = {
    'fg_color': 'transparent',
    'width': 60,
    'height': 60,
    'border_color': '#ef6319',
    'border_width': 2,
    'corner_radius': 15,
    'hover_color': '#ef6319',
    'font': ('arial', 18)
}

# Create the main window and configure it
root = CTk()
root.title('Calculator')
root.geometry('310x430+700+60')
root.minsize(300, 500)

main_frame = CTkFrame(root, fg_color='black', corner_radius=15)
main_frame.pack(fill='both', expand=True, padx=5, pady=5)

# Global variable to store the current expression
expression = ''

# ---------------------------
# Basic Calculator Functions
# ---------------------------
def update_expression(val):
    global expression
    expression += str(val)
    entry_var.set(expression)

def evaluate_expression():
    global expression
    try:
        # Evaluate the expression in a restricted environment with math functions.
        result = str(eval(expression, {"__builtins__": None}, math.__dict__))
        entry_var.set(result)
        expression = result
    except Exception:
        entry_var.set('Error')
        expression = ''

def clear_expression():
    global expression
    expression = ''
    entry_var.set(expression)

# ---------------------------
# New Scientific Functions
# ---------------------------
def apply_scientific_function(func):
    """
    Apply a scientific function to the current value.
    Assumes the current expression is a valid number.
    """
    global expression
    try:
        value = float(expression)
        result = func(value)
        expression = str(result)
        entry_var.set(expression)
    except Exception:
        entry_var.set("Error")
        expression = ''

def nth_root():
    """
    Ask the user for the degree of the root (n) and compute the nth root.
    """
    global expression
    try:
        base = float(expression)
        n = simpledialog.askfloat("Nth Root", "Enter the degree of root (n):", parent=root)
        if n is None or n == 0:
            return
        result = base ** (1 / n)
        expression = str(result)
        entry_var.set(expression)
    except Exception:
        entry_var.set("Error")
        expression = ''

def power():
    """
    Ask the user for an exponent and compute the value raised to that power.
    """
    global expression
    try:
        base = float(expression)
        exp = simpledialog.askfloat("Power", "Enter the exponent:", parent=root)
        if exp is None:
            return
        result = base ** exp
        expression = str(result)
        entry_var.set(expression)
    except Exception:
        entry_var.set("Error")
        expression = ''

def insert_pi():
    """
    Inserts the value of PI into the current expression.
    """
    global expression
    expression += str(math.pi)
    entry_var.set(expression)

def factorial_value():
    """
    Compute the factorial of the current number.
    Note: math.factorial requires a non-negative integer.
    """
    global expression
    try:
        value = float(expression)
        if not value.is_integer() or value < 0:
            raise ValueError("Factorial requires a non-negative integer")
        value = int(value)
        result = math.factorial(value)
        expression = str(result)
        entry_var.set(expression)
    except Exception:
        entry_var.set("Error")
        expression = ''

# Helper functions to convert degrees to radians for trig calculations
def sin_deg(x):
    return math.sin(math.radians(x))

def cos_deg(x):
    return math.cos(math.radians(x))

def tan_deg(x):
    return math.tan(math.radians(x))

# ---------------------------
# Create the Display Entry
# ---------------------------
entry_frame = CTkFrame(main_frame, fg_color='black')
entry_frame.grid(row=0, column=0, pady=7, padx=7, columnspan=4)

entry_var = StringVar()
main_entry = CTkEntry(entry_frame, corner_radius=15, height=45, width=80000,
                      font=('arial', 20), textvariable=entry_var, justify='right')
main_entry.pack(fill='x')

# ---------------------------
# Standard Calculator Buttons
# ---------------------------
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3)
]

for (text, row, column) in buttons:
    if text == '=':
        button = CTkButton(main_frame, text=text,
                           fg_color='transparent',
                           border_color='blue',
                           border_width=2,
                           corner_radius=15,
                           width=60,
                           height=60,
                           hover_color='blue',
                           font=('arial', 18),
                           command=evaluate_expression)
    else:
        button = CTkButton(main_frame, text=text, **button_config,
                           command=lambda t=text: update_expression(t))
    button.grid(row=row, column=column, padx=5, pady=5)

# ---------------------------
# Bottom Frame for Clear and Scientific Toggle
# ---------------------------
bottom_frame = CTkFrame(main_frame, fg_color='black')
bottom_frame.grid(row=5, column=0, columnspan=4, pady=5, padx=5)

clear_button = CTkButton(bottom_frame, text='C',
                         fg_color='transparent',
                         border_color='red',
                         border_width=2,
                         corner_radius=15,
                         width=60,
                         height=60,
                         hover_color='red',
                         font=('arial', 18),
                         command=clear_expression)
clear_button.grid(row=0, column=0, padx=5, pady=5)

# ---------------------------
# Scientific Mode Toggle
# ---------------------------
scientific_mode = False

def toggle_scientific_mode():
    global scientific_mode
    if not scientific_mode:
        scientific_frame.grid(row=6, column=0, columnspan=4, pady=5, padx=5)
        # Adjust the window height to accommodate additional rows
        root.geometry("310x750")
        scientific_mode = True
    else:
        scientific_frame.grid_forget()
        root.geometry("310x430")
        scientific_mode = False

sci_toggle_button = CTkButton(bottom_frame, text='Sci',
                              fg_color='transparent',
                              border_color='green',
                              border_width=2,
                              corner_radius=15,
                              width=60,
                              height=60,
                              hover_color='green',
                              font=('arial', 18),
                              command=toggle_scientific_mode)
sci_toggle_button.grid(row=0, column=1, padx=5, pady=5)

# ---------------------------
# Scientific Functions Panel
# ---------------------------
scientific_frame = CTkFrame(main_frame, fg_color='black', corner_radius=15)

# Arrange scientific buttons in a grid.
# Row 0
sci_buttons = [
    ("√",   0, 0, lambda: apply_scientific_function(math.sqrt)),
    ("sin", 0, 1, lambda: apply_scientific_function(sin_deg)),
    ("cos", 0, 2, lambda: apply_scientific_function(cos_deg)),
    ("tan", 0, 3, lambda: apply_scientific_function(tan_deg)),
    # Row 1
    ("log", 1, 0, lambda: apply_scientific_function(math.log10)),
    ("ln",  1, 1, lambda: apply_scientific_function(math.log)),
    ("x²",  1, 2, lambda: apply_scientific_function(lambda x: x**2)),
    ("x³",  1, 3, lambda: apply_scientific_function(lambda x: x**3)),
    # Row 2
    ("n√",  2, 0, nth_root),
    ("pow", 2, 1, power),
    ("PI",  2, 2, insert_pi),
    ("fact",2, 3, factorial_value)
]

for (text, row, column, cmd) in sci_buttons:
    sci_button = CTkButton(scientific_frame, text=text, **button_config, command=cmd)
    sci_button.grid(row=row, column=column, padx=5, pady=5)

# ---------------------------
# Grid Configuration
# ---------------------------
for i in range(7):  # rows 0 through 6 in main_frame
    main_frame.rowconfigure(i, weight=1)
for j in range(4):
    main_frame.columnconfigure(j, weight=1)

# ---------------------------
# Run the Application
# ---------------------------
root.mainloop()
