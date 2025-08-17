import tkinter as tk
from tkinter import messagebox
import re

class ContactBookApp:
    def __init__(self, master):
        self.master = master
        master.title("Contact Book")
        master.geometry("700x500")
        master.config(bg="#f0f0f0")

        self.contacts = []
        
        # --- Main Frames ---
        self.input_frame = tk.Frame(master, bg="#e0e0e0", padx=10, pady=10, relief=tk.GROOVE, bd=2)
        self.input_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)

        self.list_frame = tk.Frame(master, bg="#f0f0f0", padx=10, pady=10)
        self.list_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        # --- Input Frame Widgets ---
        tk.Label(self.input_frame, text="Contact Details", font=("Arial", 14, "bold"), bg="#e0e0e0").pack(pady=5)
        
        self.labels = ["Name", "Phone", "Email", "Address"]
        self.entries = {}
        for label_text in self.labels:
            tk.Label(self.input_frame, text=f"{label_text}:", bg="#e0e0e0", anchor="w").pack(fill=tk.X, pady=(10, 0))
            entry = tk.Entry(self.input_frame, bd=2, relief=tk.SUNKEN)
            entry.pack(fill=tk.X, pady=(0, 5))
            self.entries[label_text] = entry
            
        self.add_button = tk.Button(self.input_frame, text="Add Contact", command=self.add_contact, bg="#4CAF50", fg="white", relief=tk.RAISED)
        self.add_button.pack(fill=tk.X, pady=10)
        
        self.update_button = tk.Button(self.input_frame, text="Update Contact", command=self.update_contact, bg="#FFC107", fg="black", relief=tk.RAISED)
        self.update_button.pack(fill=tk.X, pady=5)
        
        self.delete_button = tk.Button(self.input_frame, text="Delete Contact", command=self.delete_contact, bg="#F44336", fg="white", relief=tk.RAISED)
        self.delete_button.pack(fill=tk.X, pady=5)

        # --- List Frame Widgets ---
        tk.Label(self.list_frame, text="Contact List", font=("Arial", 14, "bold"), bg="#f0f0f0").pack(pady=5)
        
        self.search_entry = tk.Entry(self.list_frame, bd=2, relief=tk.SUNKEN)
        self.search_entry.insert(0, "Search by name or phone...")
        self.search_entry.bind("<FocusIn>", self.clear_search_placeholder)
        self.search_entry.bind("<FocusOut>", self.add_search_placeholder)
        self.search_entry.pack(fill=tk.X, pady=5)
        
        self.search_button = tk.Button(self.list_frame, text="Search", command=self.search_contact, bg="#2196F3", fg="white", relief=tk.RAISED)
        self.search_button.pack(pady=5)
        
        self.view_all_button = tk.Button(self.list_frame, text="View All", command=self.view_contacts, bg="#9E9E9E", fg="white", relief=tk.RAISED)
        self.view_all_button.pack(pady=5)

        self.contact_listbox = tk.Listbox(self.list_frame, selectmode=tk.SINGLE, height=15, bd=2, relief=tk.SUNKEN)
        self.contact_listbox.pack(fill=tk.BOTH, expand=True)
        self.contact_listbox.bind("<<ListboxSelect>>", self.on_listbox_select)
        
        self.view_contacts()
        
    def add_contact(self):
        name = self.entries["Name"].get().strip()
        phone = self.entries["Phone"].get().strip()
        email = self.entries["Email"].get().strip()
        address = self.entries["Address"].get().strip()

        if not name or not phone:
            messagebox.showerror("Error", "Name and Phone number are required.")
            return

        contact = {"Name": name, "Phone": phone, "Email": email, "Address": address}
        self.contacts.append(contact)
        messagebox.showinfo("Success", f"Contact '{name}' added successfully!")
        self.clear_entries()
        self.view_contacts()
    
    def view_contacts(self):
        self.contact_listbox.delete(0, tk.END)
        if not self.contacts:
            self.contact_listbox.insert(tk.END, "No contacts found.")
        else:
            for contact in self.contacts:
                self.contact_listbox.insert(tk.END, f"{contact['Name']} | {contact['Phone']}")

    def search_contact(self):
        query = self.search_entry.get().strip().lower()
        if not query or query == "search by name or phone...":
            messagebox.showwarning("Warning", "Please enter a search query.")
            return

        self.contact_listbox.delete(0, tk.END)
        found_contacts = []
        for contact in self.contacts:
            if query in contact['Name'].lower() or query in contact['Phone']:
                found_contacts.append(contact)
        
        if not found_contacts:
            self.contact_listbox.insert(tk.END, "No matching contacts found.")
        else:
            for contact in found_contacts:
                self.contact_listbox.insert(tk.END, f"{contact['Name']} | {contact['Phone']}")
    
    def on_listbox_select(self, event):
        try:
            selected_index = self.contact_listbox.curselection()[0]
            if not self.contacts:
                return

            contact = self.contacts[selected_index]
            self.clear_entries()
            self.entries["Name"].insert(0, contact["Name"])
            self.entries["Phone"].insert(0, contact["Phone"])
            self.entries["Email"].insert(0, contact["Email"])
            self.entries["Address"].insert(0, contact["Address"])
        except IndexError:
            pass

    def update_contact(self):
        try:
            selected_index = self.contact_listbox.curselection()[0]
            if not self.contacts:
                messagebox.showerror("Error", "No contacts to update.")
                return

            name = self.entries["Name"].get().strip()
            phone = self.entries["Phone"].get().strip()
            email = self.entries["Email"].get().strip()
            address = self.entries["Address"].get().strip()

            if not name or not phone:
                messagebox.showerror("Error", "Name and Phone number are required.")
                return

            self.contacts[selected_index]["Name"] = name
            self.contacts[selected_index]["Phone"] = phone
            self.contacts[selected_index]["Email"] = email
            self.contacts[selected_index]["Address"] = address
            
            messagebox.showinfo("Success", "Contact updated successfully!")
            self.clear_entries()
            self.view_contacts()
        except IndexError:
            messagebox.showerror("Error", "Please select a contact to update.")

    def delete_contact(self):
        try:
            selected_index = self.contact_listbox.curselection()[0]
            if not self.contacts:
                messagebox.showerror("Error", "No contacts to delete.")
                return

            contact_name = self.contacts[selected_index]["Name"]
            if messagebox.askyesno("Confirm Deletion", f"Are you sure you want to delete {contact_name}?"):
                del self.contacts[selected_index]
                messagebox.showinfo("Success", f"Contact '{contact_name}' deleted successfully!")
                self.clear_entries()
                self.view_contacts()
        except IndexError:
            messagebox.showerror("Error", "Please select a contact to delete.")

    def clear_entries(self):
        for entry in self.entries.values():
            entry.delete(0, tk.END)

    def clear_search_placeholder(self, event):
        if self.search_entry.get() == "Search by name or phone...":
            self.search_entry.delete(0, tk.END)
            
    def add_search_placeholder(self, event):
        if not self.search_entry.get():
            self.search_entry.insert(0, "Search by name or phone...")

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBookApp(root)
    root.mainloop()