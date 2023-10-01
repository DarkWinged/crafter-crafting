import tkinter as tk


class EntryRow:
    def __init__(self, parent_frame: tk.Widget, selected, options, amount, remove_function: callable, row: int):
        self.parent_frame = parent_frame
        self.dropdown_var = tk.StringVar(self.parent_frame)
        self.dropdown_var.set(selected)
        self.dropdown = tk.OptionMenu(self.parent_frame, self.dropdown_var, selected, *options)
        self.dropdown.grid(row=row, column=1, padx=(0, 5), pady=5, sticky="e")
        self.amount_label = tk.Label(self.parent_frame, text="Amount:")
        self.amount_label.grid(row=row, column=2, padx=(5, 0), pady=5, sticky="w")
        self.amount_entry = tk.Entry(self.parent_frame, width=10)
        self.amount_entry.insert(tk.END, amount)
        self.amount_entry.grid(row=row, column=3, padx=(0, 5), pady=5, sticky="e")
        self.remove_function = remove_function
        self.remove_button = tk.Button(self.parent_frame, text="Remove", command=self.remove_button_callback)
        self.remove_button.grid(row=row, column=4, padx=(5, 0), pady=5, sticky="w")
        self.row = row

    def remove_button_callback(self):
        self.remove_function(self.row)

    def destroy(self):
        self.dropdown.destroy()
        self.amount_label.destroy()
        self.amount_entry.destroy()
        self.remove_button.destroy()
