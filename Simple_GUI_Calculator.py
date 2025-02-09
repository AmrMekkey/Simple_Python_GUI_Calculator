# import the module
from customtkinter import *
# make the button configration
button_config = {
    'fg_color':'transparent',
    'width':60,
    'height':60,
    'border_color':'#ef6319',
    'border_width':2,
    'corner_radius':15,
    'hover_color':'#ef6319',
    'font':('arial',18)
}
# make the main window and main frame and the global variable
root = CTk()
root.title('Calculator')
root.geometry('310x430+700+160')
root.minsize(300,500)

main_frame = CTkFrame(root,fg_color='black',corner_radius=15)
main_frame.pack(fill='both',expand=True,padx=5,pady=5)

expression = ''
# create the functions:
# first one to renew the exprission
# add the number to the expression and set the entry to the expression
def update_expression(val):
    global expression
    expression += str(val)
    entry_var.set(expression)

# second one to calculate the result:
def evaluate_expression():
    global expression
# try get the value of the expresstion using eval method 
    try:
        result = str(eval(expression))
# then, set the entry to the expression
        entry_var.set(result)
# then, update the expression to the result
        expression = result

# else show error#
    except:
        entry_var.set('Error')
        expression = '' 

# third one to clear every thing#
def clear_expression():
    global expression
    expression = ''
    entry_var.set(expression)
# 
# creater the entry
entry_frame = CTkFrame(main_frame,fg_color='black')
entry_frame.grid(row=0,column=0,pady=7,padx=7,columnspan=4)

entry_var = StringVar()
main_entry = CTkEntry(entry_frame,corner_radius=15,height=45,width=80000,font=('arial',20),textvariable=entry_var,justify='right')
main_entry.pack(fill='x')

# create the buttons
buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
    ('0',4,0), ('.',4,1), ('+',4,2), ('=',4,3)
]



for (text, row, column) in buttons:
    if text == '=':
        button = CTkButton(main_frame,text=text,fg_color='transparent',border_color='blue',
                           border_width=2,corner_radius=15,width=60, height=60,hover_color='blue',
                           font=('arial',18),command=evaluate_expression)
    else:
        button = CTkButton(main_frame,text=text, **button_config, command=lambda t=text: update_expression(t))
    button.grid(row=row,column=column,padx=5,pady=5)


clear_button = CTkButton(main_frame,text='C',fg_color='transparent',border_color='red',
                           border_width=2,corner_radius=15,width=60, height=60,hover_color='red',
                           font=('arial',18),command=clear_expression)
clear_button.grid(row=5,column=0,pady=5,columnspan=4)

main_frame.rowconfigure(0, weight=1)
main_frame.rowconfigure(1, weight=1)
main_frame.rowconfigure(2, weight=1)
main_frame.rowconfigure(3, weight=1)
main_frame.rowconfigure(4, weight=1)

main_frame.columnconfigure(0, weight=1)
main_frame.columnconfigure(1, weight=1)
main_frame.columnconfigure(2, weight=1)
main_frame.columnconfigure(3, weight=1)

# run the app#
root.mainloop()
