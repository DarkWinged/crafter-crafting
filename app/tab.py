import tkinter as tk
from tkinter import simpledialog, messagebox
from app.protected_list import PList
from app.value_box import ValueBox  # Import the PList class from your module

class Tab:
    """ Tab is a class that represents a tab in the editor tool."""
    def __init__(self, parent_frame: tk.Frame, tab_name: str, data_list: list[dict[str, str or int]]):
        """ Tab is a class that represents a tab in the editor tool.

        Args:
            parent_frame (tk.Frame): Parent widget for the tab
            tab_name (str): Name of the tab
            data_list (list[dict[str, str or int]]): List of data for the tab
        """        
        self.parent_frame: tk.Frame = parent_frame
        self.tab_name = tab_name
        self.data_list = PList(data_list)  # Use the PList class for data_list
        self.selected_index = None

        self.init_left_frame()
        self.init_right_frame()
        self.listbox.bind("<<ListboxSelect>>", self.show_selected_entry_details)

    def init_left_frame(self):
        """ Initializes the left frame."""
        self.list_frame = tk.Frame(self.parent_frame)
        self.list_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.listbox = tk.Listbox(self.list_frame)
        self.listbox.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.button_frame = tk.Frame(self.list_frame)
        self.button_frame.pack(side=tk.TOP)

        self.add_button = tk.Button(self.button_frame, text="Add", command=self.add_entry)
        self.add_button.pack(side=tk.LEFT)

        self.delete_button = tk.Button(self.button_frame, text="Remove", command=self.delete_entry)
        self.delete_button.pack(side=tk.LEFT)

    def init_right_frame(self):
        """ Initializes the right frame."""
        self.attributes_frame = tk.Frame(self.parent_frame)
        self.attributes_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.id_value_box = ValueBox(self.attributes_frame, "ID", self.update_data_list, 0, 0, 'int')

        self.name_value_box = ValueBox(self.attributes_frame, "Name", self.update_data_list, 1, 0)

        self.confirm_button = tk.Button(self.attributes_frame, text="Confirm", command=self.update_selected_entry)
        self.confirm_button.grid(row=2, column=0, columnspan=2, pady=10)

    def add_entry(self):
        """ Adds an entry to the tab."""
        name = simpledialog.askstring(f"Add {self.tab_name} Entry", f"Enter the {self.tab_name.lower()} name:")
        if name:
            new_id = len(self.data_list) + 1
            new_entry = {"id": new_id, "name": name}
            self.data_list.append(new_entry)
            self.listbox.insert(tk.END, name)
            self.clear_attributes()

    def load_data(self, data: list[dict[str, str or int]]):
        """ Loads data into the tab.

        Args:
            data (list[dict[str, str or int]]): List of data to load
        """
        self.data_list.current = data  # Set the current attribute to the new data
        self.data_list.update()  # Call the data_list's update method
        self.listbox.delete(0, tk.END)
        for entry in self.data_list:
            self.listbox.insert(tk.END, entry['name'])

    def delete_entry(self):
        """ Deletes an entry from the tab."""
        if self.selected_index is not None:
            del self.data_list[self.selected_index]
            self.listbox.delete(self.selected_index)
            self.clear_attributes()

    def show_selected_entry_details(self, event=None):
        """ Shows the details of the selected entry."""
        self.data_list.reset()  # Reset the data_list to discard changes
        selected_index = self.listbox.curselection()
        if selected_index:
            self.selected_index = selected_index[0]
        elif not self.selected_index:
            return

        selected_entry = self.data_list[self.selected_index]
        self.id_value_box.set(selected_entry['id'])  # Update ID entry
        self.name_value_box.set(selected_entry['name'])  # Update Name entry

    def clear_attributes(self):
        """ Clears the attributes of the tab."""
        self.selected_index = None  # Set selected_index to None
        self.id_value_box.set("")  # Clear ID entry
        self.name_value_box.set("")  # Clear Name entry
        self.data_list.update()  # Call the data_list's update method

    def update_selected_entry(self):
        """ Updates the selected entry."""
        self.data_list.update()  # Only call the data_list's update method

    def update_data_list(self, *args):
        """ Updates the data list."""
        if self.selected_index is not None:
            new_id = self.id_value_box.get()
            new_name = self.name_value_box.get()
            if new_id is not None and new_name is not None:
                entry = {'id': new_id, 'name': new_name}
                self.data_list[self.selected_index] = entry
            else:
                self.parent_frame.event_generate("<<Error>>", state=406)
