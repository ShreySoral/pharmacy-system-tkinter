import tkinter as tk
from tkinter import messagebox

class PharmacyManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Pharmacy Management System")

        # Initialize variables
        self.medicine_name = tk.StringVar()
        self.quantity = tk.IntVar()
        self.inventory = {}

        # Create GUI elements
        label_name = tk.Label(root, text="Medicine Name:")
        label_name.grid(row=0, column=0, padx=10, pady=10)
        self.entry_name = tk.Entry(root, textvariable=self.medicine_name)
        self.entry_name.grid(row=0, column=1, padx=10, pady=10)

        label_quantity = tk.Label(root, text="Quantity:")
        label_quantity.grid(row=1, column=0, padx=10, pady=10)
        self.entry_quantity = tk.Entry(root, textvariable=self.quantity)
        self.entry_quantity.grid(row=1, column=1, padx=10, pady=10)

        add_button = tk.Button(root, text="Add Medicine", command=self.add_medicine)
        add_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        display_button = tk.Button(root, text="Display Inventory", command=self.display_inventory)
        display_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    def add_medicine(self):
        name = self.medicine_name.get().strip()
        quantity = self.quantity.get()

        if name == "":
            messagebox.showerror("Error", "Please enter a medicine name.")
            return

        if quantity <= 0:
            messagebox.showerror("Error", "Please enter a valid quantity.")
            return

        if name in self.inventory:
            self.inventory[name] += quantity
        else:
            self.inventory[name] = quantity

        messagebox.showinfo("Success", f"{quantity} {name}(s) added to inventory.")

        # Clear entry fields
        self.medicine_name.set("")
        self.quantity.set(0)

    def display_inventory(self):
        if not self.inventory:
            messagebox.showinfo("Inventory", "Inventory is empty.")
        else:
            inventory_text = "Current Inventory:\n"
            for medicine, quantity in self.inventory.items():
                inventory_text += f"{medicine}: {quantity}\n"

            messagebox.showinfo("Inventory", inventory_text)


if __name__ == "__main__":
    root = tk.Tk()
    app = PharmacyManagementSystem(root)
    root.mainloop()
