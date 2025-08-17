import tkinter as tk
from tkinter import messagebox
import os

class ToDoApp:
    def __init__(self, master):
        self.master = master
        master.title("Advanced To-Do List App")
        master.geometry("500x550")
        master.config(bg="#e8f4f8")

        self.tasks = []
        self.file_path = "tasks.txt"
        self.load_tasks()

        # --- Widgets ---
        self.label = tk.Label(master, text="My To-Do List", font=("Arial", 20, "bold"), bg="#e8f4f8", fg="#333")
        self.label.pack(pady=10)

        self.entry_frame = tk.Frame(master, bg="#e8f4f8")
        self.entry_frame.pack(pady=5)

        self.task_entry = tk.Entry(self.entry_frame, width=35, font=("Arial", 12), bd=2, relief="groove")
        self.task_entry.pack(side=tk.LEFT, padx=5)
        self.task_entry.bind("<Return>", self.add_task)

        self.add_button = tk.Button(self.entry_frame, text="Add Task", command=self.add_task, font=("Arial", 10, "bold"), bg="#4CAF50", fg="white", relief="raised")
        self.add_button.pack(side=tk.LEFT, padx=5)

        self.list_frame = tk.Frame(master, bg="#e8f4f8")
        self.list_frame.pack(pady=10)

        self.task_listbox = tk.Listbox(self.list_frame, width=50, height=15, selectmode=tk.SINGLE, font=("Arial", 12), bd=2, relief="sunken")
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.scrollbar = tk.Scrollbar(self.list_frame, orient=tk.VERTICAL, command=self.task_listbox.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.task_listbox.config(yscrollcommand=self.scrollbar.set)

        self.button_frame = tk.Frame(master, bg="#e8f4f8")
        self.button_frame.pack(pady=10)

        self.complete_button = tk.Button(self.button_frame, text="Mark Complete", command=self.complete_task, font=("Arial", 10, "bold"), bg="#2196F3", fg="white", relief="raised")
        self.complete_button.pack(side=tk.LEFT, padx=5)

        self.edit_button = tk.Button(self.button_frame, text="Edit Task", command=self.edit_task, font=("Arial", 10, "bold"), bg="#FFC107", fg="black", relief="raised")
        self.edit_button.pack(side=tk.LEFT, padx=5)

        self.delete_button = tk.Button(self.button_frame, text="Delete Task", command=self.delete_task, font=("Arial", 10, "bold"), bg="#f44336", fg="white", relief="raised")
        self.delete_button.pack(side=tk.LEFT, padx=5)

        # Update the listbox display
        self.update_listbox()
        
    # --- Methods ---

    def load_tasks(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as f:
                for line in f:
                    self.tasks.append(line.strip())

    def save_tasks(self):
        with open(self.file_path, "w") as f:
            for task in self.tasks:
                f.write(f"{task}\n")

    def update_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)
            if task.startswith("✓ "):
                index = self.tasks.index(task)
                self.task_listbox.itemconfig(index, fg="green")
            else:
                index = self.tasks.index(task)
                self.task_listbox.itemconfig(index, fg="black")

    def add_task(self, event=None):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.update_listbox()
            self.task_entry.delete(0, tk.END)
            self.save_tasks()
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def delete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            del self.tasks[selected_task_index]
            self.update_listbox()
            self.save_tasks()
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to delete.")

    def complete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            task = self.tasks[selected_task_index]
            if not task.startswith("✓ "):
                self.tasks[selected_task_index] = "✓ " + task
                self.update_listbox()
                self.save_tasks()
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to mark as complete.")

    def edit_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            current_task = self.tasks[selected_task_index]
            
            # Open a new window for editing
            edit_window = tk.Toplevel(self.master)
            edit_window.title("Edit Task")
            edit_window.geometry("300x100")

            edit_label = tk.Label(edit_window, text="Edit the task:", font=("Arial", 12))
            edit_label.pack(pady=5)

            edit_entry = tk.Entry(edit_window, width=30, font=("Arial", 10))
            edit_entry.insert(0, current_task.replace("✓ ", ""))
            edit_entry.pack(pady=5)

            def save_edit():
                new_task = edit_entry.get()
                if new_task:
                    if current_task.startswith("✓ "):
                        self.tasks[selected_task_index] = "✓ " + new_task
                    else:
                        self.tasks[selected_task_index] = new_task
                    self.update_listbox()
                    self.save_tasks()
                    edit_window.destroy()
                else:
                    messagebox.showwarning("Warning", "Task cannot be empty.")
            
            save_button = tk.Button(edit_window, text="Save", command=save_edit, bg="#4CAF50", fg="white")
            save_button.pack(pady=5)
            
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to edit.")

# --- Main application loop ---
root = tk.Tk()
app = ToDoApp(root)
root.mainloop()