import tkinter as tk
from tkinter import messagebox
import random
import string

class PasswordGeneratorApp:
    def __init__(self, master):
        self.master = master
        master.title("Password Generator")
        master.geometry("350x200")
        master.config(bg="#f0f0f0")

        # --- Widgets ---
        self.label_length = tk.Label(master, text="Enter password length:", bg="#f0f0f0")
        self.label_length.pack(pady=10)

        self.entry_length = tk.Entry(master, width=10, bd=2, relief="groove")
        self.entry_length.pack()

        self.generate_button = tk.Button(master, text="Generate Password", command=self.generate_and_display, bg="#4CAF50", fg="white", font=("Helvetica", 10, "bold"))
        self.generate_button.pack(pady=10)

        self.result_label = tk.Label(master, text="Generated Password: ", font=("Courier", 12, "bold"), bg="#f0f0f0", wraplength=300)
        self.result_label.pack(pady=10)
        
    def generate_and_display(self):
        """
        Generates a password based on user input and displays it.
        """
        try:
            length = int(self.entry_length.get())
            if length <= 0:
                messagebox.showerror("Error", "Password length must be a positive number.")
                return

            characters = string.ascii_letters + string.digits + string.punctuation
            password = ''.join(random.choice(characters) for _ in range(length))
            
            self.result_label.config(text=f"Generated Password: {password}")
            
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter a valid number.")

# --- Main application loop ---
if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()

