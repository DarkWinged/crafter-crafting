import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog
from app.entry_row import EntryRow
from app.protected_list import PList
from app.tab import Tab
from app.value_box import ValueBox


class RecipesTab(Tab):
    """RecipesTab class for handling the Recipes tab in the editor tool's main window.
    """
    def __init__(self, parent_frame: tk.Frame, data_list: list[dict[str, str or int]], ingredients_data: PList[list[str, str or int]]):
        """Initialize the RecipesTab class.

        Args:
            parent_frame (tk.Frame): Parent frame for the tab
            data_list (list[dict[str, str or int]]): List of recipe dictionaries to load into the tab
            ingredients_data (PList[list[str, str or int]]): Protected list of ingredient dictionaries to use for the ingredient dropdowns
        """
        self.parent_frame = parent_frame
        self.tab_name = "Recipes"
        self.data_list: PList[list[str, str or int]] = PList(data_list)
        self.ingredients_data = ingredients_data
        self.selected_index = None
        # Create lists to hold the widgets for ingredients and products
        self.ingredient_rows: list[EntryRow] = []
        self.product_rows: list[EntryRow] = []

        self.init_left_frame()
        self.init_right_frame()
        self.listbox.bind("<<ListboxSelect>>", self.show_selected_entry_details)

    def init_right_frame(self):
        """Initialize the right frame with the recipe attributes
        """
        super().init_right_frame()
        self.id_value_box.var.trace("w", self.update_data_list)
        self.name_value_box.var.trace("w", self.update_data_list)

        self.duration_value_box = ValueBox(self.attributes_frame, "Duration", self.update_data_list, 2, 0, 'int')

        self.ingredients_label = tk.Label(self.attributes_frame, text="Ingredients:")
        self.ingredients_label.grid(row=3, column=0, columnspan=2, pady=(10, 0))
        self.ingredients_pane = ttk.PanedWindow(self.attributes_frame, orient=tk.VERTICAL)
        self.ingredients_pane.grid(row=4, column=0, columnspan=2, sticky="nsew", padx=10)
        self.add_ingredient_button = tk.Button(self.attributes_frame, text="Add Ingredient", command=self.add_ingredient_entry)
        self.add_ingredient_button.grid(row=5, column=0, columnspan=2, pady=(0, 10))

        self.products_label = tk.Label(self.attributes_frame, text="Products:")
        self.products_label.grid(row=6, column=0, columnspan=2, pady=(10, 0))
        self.products_pane = ttk.PanedWindow(self.attributes_frame, orient=tk.VERTICAL)
        self.products_pane.grid(row=7, column=0, columnspan=2, sticky="nsew", padx=10)
        self.add_product_button = tk.Button(self.attributes_frame, text="Add Product", command=self.add_product_entry)
        self.add_product_button.grid(row=8, column=0, columnspan=2, pady=(0, 10))

        self.confirm_button.config(command=self.update_selected_entry)
        self.confirm_button.pack_forget()
        self.confirm_button.grid(row=9, column=0, columnspan=2, pady=10)

    def load_data(self, data: list[dict[str, str or int]], ingredients_data: list[dict[str, str or int]]):
        """Load the data into the tab.

        Args:
            data (list[dict[str, str or int]]): List of recipe dictionaries to load into the tab
            ingredients_data (list[dict[str, str or int]]): List of ingredient dictionaries to use for the ingredient dropdowns
        """
        super().load_data(data)
        for entry in self.data_list:
            if entry.get('duration') is None:
                entry['duration'] = 0
        self.ingredients_data = ingredients_data

    def add_entry(self):
        name = simpledialog.askstring(f"Add {self.tab_name} Entry", f"Enter the {self.tab_name.lower()} name:")
        if name:
            new_id = len(self.data_list) + 1
            new_entry = {'id': new_id, 'name': name, 'duration':0, 'ingredients': [], 'products': []}
            self.data_list.append(new_entry)
            self.listbox.insert(tk.END, name)
            self.clear_attributes()

    def show_selected_entry_details(self, event=None):
        self.data_list.reset()  # Reset the data_list to the original state
        selected_index = self.listbox.curselection()
        if selected_index:
            self.selected_index = selected_index[0]
        elif not self.selected_index:
            return
        # Clear the ingredient and product listboxes and their widgets
        self.clear_ingredient_entries()
        self.clear_product_entries()

        selected_entry = self.data_list[self.selected_index]
        self.id_value_box.set(selected_entry['id'])  # Update ID entry
        self.name_value_box.set(selected_entry['name'])  # Update Name entry
        self.duration_value_box.set(selected_entry['duration'])  # Update Duration entry

        # Fill the ingredient listbox with dropdown and amount textbox for each ingredient
        for row, ingredient in enumerate(selected_entry.get('ingredients', [])):
            ingredient_id = ingredient.get('id')
            ingredient_amount = ingredient.get('amount')
            self.create_ingredient_entry(ingredient_id, ingredient_amount, row)

        # Fill the product listbox with dropdown and amount textbox for each product
        for row, product in enumerate(selected_entry.get('products', [])):
            product_id = product.get('id')
            product_amount = product.get('amount')
            self.create_product_entry(product_id, product_amount, row)

    def clear_attributes(self):
        self.duration_value_box.set("")
        return super().clear_attributes()

    def clear_ingredient_entries(self):
        # Clear ingredient widgets and their references
        for ingredient_row in self.ingredient_rows:
            ingredient_row.destroy()
        self.ingredient_rows = []

    def clear_product_entries(self):
        # Clear product widgets and their references
        for product_row in self.product_rows:
            product_row.destroy()
        self.product_rows = []

    def create_ingredient_entry(self, selected_ingredient_id, selected_amount, row):
        ingredient_names = [item.get('name') for item in self.ingredients_data if item.get('id') == selected_ingredient_id]
        if ingredient_names:
            selected_ingredient = ingredient_names[0]
            ingredient_options = [name for name in self.get_ingredient_names() if name != selected_ingredient]  # Remove selected product from options
            ingredient_row = EntryRow(self.ingredients_pane, selected_ingredient, ingredient_options, selected_amount, self.remove_ingredient_entry, row)
            ingredient_row.dropdown_var.trace("w", self.update_data_list)  # Attach trace to update data_list
            ingredient_row.amount_entry.bind("<KeyRelease>", self.update_data_list)
            self.ingredient_rows.append(ingredient_row)
        else:
            selected_ingredient = None
            ingredient_options = self.get_ingredient_names()
            ingredient_row = EntryRow(self.ingredients_pane, selected_ingredient, ingredient_options, selected_amount, self.remove_ingredient_entry, row)
            ingredient_row.dropdown_var.trace("w", self.update_data_list)  # Attach trace to update data_list
            ingredient_row.amount_entry.bind("<KeyRelease>", self.update_data_list)
            self.ingredient_rows.append(ingredient_row)

    def create_product_entry(self, selected_product_id, selected_amount, row):
        product_names = [item.get('name') for item in self.ingredients_data if item.get('id') == selected_product_id]
        if product_names:
            selected_product = product_names[0]
            product_options = [name for name in self.get_ingredient_names() if name != selected_product]  # Remove selected product from options
            product_row = EntryRow(self.products_pane, selected_product, product_options, selected_amount, self.remove_product_entry, row)
            product_row.dropdown_var.trace("w", self.update_data_list)  # Attach trace to update data_list
            product_row.amount_entry.bind("<KeyRelease>", self.update_data_list)
            self.product_rows.append(product_row)
        else:
            selected_product = None
            product_options = self.get_ingredient_names()
            product_row = EntryRow(self.products_pane, selected_product, product_options, selected_amount, self.remove_product_entry, row)
            product_row.dropdown_var.trace("w", self.update_data_list)
            product_row.amount_entry.bind("<KeyRelease>", self.update_data_list)
            self.product_rows.append(product_row)

    def remove_ingredient_entry(self, row):
        # Remove the ingredient widgets and references
        self.ingredient_rows[row].destroy()
        for ingredient_row in range(row, len(self.ingredient_rows)):
            self.ingredient_rows[ingredient_row].row -= 1
        del self.data_list[self.selected_index]['ingredients'][row]
        del self.ingredient_rows[row]
        # Update the ingredients listbox to reflect the changes

    def remove_product_entry(self, row):
        # Remove the product widgets and references
        self.product_rows[row].destroy()
        for product_row in range(row, len(self.product_rows)):
            self.product_rows[product_row].row -= 1
        del self.data_list[self.selected_index]['products'][row]
        del self.product_rows[row]
        # Update the products listbox to reflect the changes

    def get_ingredient_names(self):
        return [item.get('name') for item in self.ingredients_data]
    
    def get_selected_ingredient_ids(self):
        # Get the IDs of the selected ingredients based on the dropdown selections
        selected_ingredient_ids = []
        for ingredient_row in self.ingredient_rows:
            ingredient_name = ingredient_row.dropdown_var.get()
            ingredient_id = next((item.get('id') for item in self.ingredients_data if item.get('name') == ingredient_name), None)
            if ingredient_id is not None:
                selected_ingredient_ids.append(ingredient_id)
        return selected_ingredient_ids

    def get_selected_product_ids(self):
        # Get the IDs of the selected products based on the dropdown selections
        selected_product_ids = []
        for product_row in self.product_rows:
            product_name = product_row.dropdown_var.get()
            product_id = next((item.get('id') for item in self.ingredients_data if item.get('name') == product_name), None)
            if product_id is not None:
                selected_product_ids.append(product_id)
        return selected_product_ids

    def update_data_list(self, *args):
        if self.selected_index is not None:
            new_id = self.id_value_box.get()
            new_name = self.name_value_box.get()
            new_duration = self.duration_value_box.get()
            if new_duration is None:
                new_duration = 0
            if new_id is not None and new_name is not None:
                # Update the selected entry's data in data_list
                entry = {'id': new_id, 'name': new_name, 'duration': new_duration, 'ingredients': [], 'products': []}

                for ingredient_row in self.ingredient_rows:
                    ingredient_dropdown = ingredient_row.dropdown_var
                    ingredient_id = self.get_id_from_name(ingredient_dropdown.get())
                    amount = ingredient_row.amount_entry.get()
                    amount = int(amount) if amount.isdigit() else -1
                    entry['ingredients'].append({'id': ingredient_id, 'amount': amount})

                for product_row in self.product_rows:
                    product_dropdown: tk.StringVar = product_row.dropdown_var
                    product_id = self.get_id_from_name(product_dropdown.get())
                    amount = product_row.amount_entry.get()
                    amount = int(amount) if amount.isdigit() else -1
                    entry['products'].append({'id': product_id, 'amount': amount})
                if not entry['ingredients'] and not entry['products']:
                    return
                self.data_list[self.selected_index] = entry
            else:
                self.parent_frame.event_generate("<<Error>>", state=406)

    def add_ingredient_entry(self):
        # Create an ingredient entry with default values
        ingredient_id = 1
        ingredient_amount = 0
        self.data_list[self.selected_index]['ingredients'].append({'id': ingredient_id, 'amount': ingredient_amount})
        self.create_ingredient_entry(ingredient_id, ingredient_amount, len(self.data_list[self.selected_index]['ingredients'])-1)

    def add_product_entry(self):
        # Create a product entry with default values
        product_id = 1
        product_amount = 0
        self.data_list[self.selected_index]['products'].append({'id': product_id, 'amount': product_amount})
        self.create_product_entry(product_id, product_amount, len(self.data_list[self.selected_index]['products'])-1)

    def get_id_from_name(self, name):
        for item in self.ingredients_data:
            if item.get('name') == name:
                return item.get('id')
        return None
