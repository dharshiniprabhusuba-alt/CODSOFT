import customtkinter as ctk

class Calculator(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Calculator")
        self.geometry("250x350")
        self.resizable(False, False)

        # Set up a variable to hold the expression
        self.expression = ""

        # Entry field for display
        self.display_entry = ctk.CTkEntry(self, font=ctk.CTkFont(size=24), justify="right")
        self.display_entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="ew")

        # --- Button Layout ---
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            if button == '=':
                btn = ctk.CTkButton(self, text=button, command=self.calculate)
            else:
                btn = ctk.CTkButton(self, text=button, command=lambda b=button: self.add_to_expression(b))
            
            btn.grid(row=row_val, column=col_val, sticky="nsew", padx=5, pady=5)
            
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1
        
        # Clear button
        clear_btn = ctk.CTkButton(self, text="C", command=self.clear_expression)
        clear_btn.grid(row=row_val, column=0, columnspan=2, sticky="nsew", padx=5, pady=5)

        # Configure grid for buttons to expand evenly
        for i in range(5):
            self.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.grid_columnconfigure(i, weight=1)
        
    # --- Methods ---
    def add_to_expression(self, value):
        self.expression += str(value)
        self.display_entry.delete(0, ctk.END)
        self.display_entry.insert(ctk.END, self.expression)

    def calculate(self):
        try:
            # Use Python's built-in `eval()` to evaluate the expression
            result = eval(self.expression)
            self.display_entry.delete(0, ctk.END)
            self.display_entry.insert(ctk.END, str(result))
            self.expression = str(result)
        except (ValueError, SyntaxError, ZeroDivisionError) as e:
            self.display_entry.delete(0, ctk.END)
            self.display_entry.insert(ctk.END, "Error")
            self.expression = ""

    def clear_expression(self):
        self.expression = ""
        self.display_entry.delete(0, ctk.END)

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()