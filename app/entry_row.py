import tkinter as tk


class EntryRow:
    """ EntryRow is a class that represents a row of items in the recipe editor tool's ingredients tab."""
    def __init__(self, parent_frame: tk.Widget, selected: str, options: list[str], amount: int, remove_function: callable, row: int):
        """ EntryRow is a class that represents a row in the recipe editor tool's ingredients tab.

        Args:
            parent_frame (tk.Widget): Parent widget for the row
            selected (str): Name of the selected option
            options (list[str]): List of options for the dropdown
            amount (int): Amount of item represented by the row
            remove_function (callable): Function to call when the remove button is pressed
            row (int): Row number of the row
        """
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
        """ Callback function for the remove button.
        """
        self.remove_function(self.row)

    def destroy(self):
        """ Destroys the row.
        """
        self.dropdown.destroy()
        self.amount_label.destroy()
        self.amount_entry.destroy()
        self.remove_button.destroy()
