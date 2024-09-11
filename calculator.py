import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.expression = ""
        self.input_text = tk.StringVar(value="0")

        root.title("Calculator")
        root.geometry("360x500")
        root.configure(bg="#202020")
        root.resizable(0, 0)

        input_frame = tk.Frame(root, bg="#202020")
        input_frame.pack(expand=True, fill="both")

        input_field = tk.Entry(input_frame, textvariable=self.input_text, font=('Arial', 22, 'bold'),
                               bd=10, insertwidth=2, justify='right', bg="#282828", fg="white", relief="flat")
        input_field.grid(row=0, column=0, columnspan=4, ipady=15, sticky="nsew")

        btns_frame = tk.Frame(root, bg="#202020")
        btns_frame.pack(expand=True, fill="both")

        buttons = [
            ('C', 1, 0), ('%', 1, 1), ('⌫', 1, 2), ('/', 1, 3),
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('*', 2, 3),
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3),
            ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('+', 4, 3),
            ('+/-', 5, 0), ('0', 5, 1), ('.', 5, 2), ('=', 5, 3)
        ]

        for (label, row, col) in buttons:
            self.create_button(btns_frame, label, row, col)

        for i in range(6):
            btns_frame.grid_rowconfigure(i, weight=1)
            btns_frame.grid_columnconfigure(i, weight=1)

    def create_button(self, parent, label, row, col):
        button = tk.Button(parent, text=label, font=('Arial', 18, 'bold'), fg="white", bg="#333333",
                           bd=1, command=lambda: self.on_button_click(label), height=3, width=7,
                           relief="flat", activebackground="#505050", activeforeground="white",
                           highlightthickness=0)
        button.grid(row=row, column=col, sticky="nsew", padx=1, pady=1)

        button.bind("<Enter>", lambda e: button.configure(bg="#505050"))
        button.bind("<Leave>", lambda e: button.configure(bg="#333333"))

    def on_button_click(self, label):
        if label == 'C':
            self.clear()
        elif label == '⌫':
            self.backspace()
        elif label == '=':
            self.calculate()
        elif label == '+/-':
            self.toggle_sign()
        elif label == '%':
            self.percent()
        elif label == '.':
            self.add_decimal()
        else:
            self.add_to_expression(label)

    def clear(self):
        self.expression = ""
        self.input_text.set("0")

    def backspace(self):
        self.expression = self.expression[:-1]
        self.input_text.set(self.expression if self.expression else "0")

    def calculate(self):
        try:
            result = str(eval(self.expression))
            self.input_text.set(result)
            self.expression = result
        except:
            self.input_text.set("Error")
            self.expression = ""

    def toggle_sign(self):
        if self.expression:
            if self.expression[0] == '-':
                self.expression = self.expression[1:]
            else:
                self.expression = '-' + self.expression
            self.input_text.set(self.expression)

    def percent(self):
        try:
            self.expression = str(float(self.expression) / 100)
            self.input_text.set(self.expression)
        except:
            self.input_text.set("Error")
            self.expression = ""

    def add_decimal(self):
        if '.' not in self.expression.split()[-1]:
            self.expression += '.'
            self.input_text.set(self.expression)

    def add_to_expression(self, label):
        if self.expression == "0" and label not in "+-*/%":
            self.expression = label
        else:
            self.expression += str(label)
        self.input_text.set(self.expression)

root = tk.Tk()
calc = Calculator(root)
root.mainloop()