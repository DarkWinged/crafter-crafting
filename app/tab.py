import tkinter as tk
from tkinter import simpledialog, messagebox

class Tab:
    def __init__(self, parent_frame: tk.Frame, tab_name, data_list):
        self.parent_frame: tk.Frame = parent_frame
        self.tab_name = tab_name
        self.data_list = data_list
        self.temp_data = data_list.copy()
        self.selected_index = None

        self.init_left_frame()
        self.init_right_frame()
        self.listbox.bind("<<ListboxSelect>>", self.show_selected_entry_details)

    def init_left_frame(self):
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
        self.attributes_frame = tk.Frame(self.parent_frame)
        self.attributes_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.id_label = tk.Label(self.attributes_frame, text="ID:")
        self.id_label.grid(row=0, column=0)

        self.id_var = tk.StringVar()  # Create StringVar for ID
        self.id_entry = tk.Entry(self.attributes_frame, textvariable=self.id_var)
        self.id_entry.grid(row=0, column=1)
        self.id_var.trace("w", self.update_temp_data)  # Attach trace to update temp_data

        self.name_label = tk.Label(self.attributes_frame, text="Name:")
        self.name_label.grid(row=1, column=0)

        self.name_var = tk.StringVar()  # Create StringVar for Name
        self.name_entry = tk.Entry(self.attributes_frame, textvariable=self.name_var)
        self.name_entry.grid(row=1, column=1)
        self.name_var.trace("w", self.update_temp_data)  # Attach trace to update temp_data

        self.confirm_button = tk.Button(self.attributes_frame, text="Confirm", command=self.update_selected_entry)
        self.confirm_button.grid(row=2, column=0, columnspan=2, pady=10)

    def add_entry(self):
        name = simpledialog.askstring(f"Add {self.tab_name} Entry", f"Enter the {self.tab_name.lower()} name:")
        if name:
            new_id = len(self.temp_data) + 1
            new_entry = {"id": new_id, "name": name}
            self.temp_data.append(new_entry)
            self.data_list.append(new_entry)
            self.listbox.insert(tk.END, name)
            self.clear_attributes()

    def load_data(self, data: list[dict[str, str or int]]):
        self.data_list = data
        self.temp_data = data.copy()
        self.listbox.delete(0, tk.END)
        for entry in self.data_list:
            self.listbox.insert(tk.END, entry['name'])

    def delete_entry(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            selected_index = selected_index[0]
            del self.temp_data[selected_index]
            del self.data_list[selected_index]
            self.listbox.delete(selected_index)
            self.clear_attributes()

    def show_selected_entry_details(self, event=None):
        self.temp_data = self.data_list.copy()
        selected_index = self.listbox.curselection()
        if selected_index:
            self.selected_index = selected_index[0]
            selected_entry = self.temp_data[self.selected_index]
            self.id_var.set(selected_entry['id'])  # Update ID entry
            self.name_var.set(selected_entry['name'])  # Update Name entry

    def clear_attributes(self):
        self.id_var.set("")  # Clear ID entry
        self.name_var.set("")  # Clear Name entry

    def update_selected_entry(self):
        if self.selected_index is not None:
            new_id = self.id_var.get()
            new_name = self.name_var.get()
            if new_id.isdigit():
                new_id = int(new_id)
            else:
                new_id = None
            if new_id is not None and new_name:
                self.data_list[self.selected_index] = self.temp_data[self.selected_index]
                self.listbox.delete(self.selected_index)
                self.listbox.insert(self.selected_index, new_name)
                self.listbox.selection_set(self.selected_index)
            else:
                self.parent_frame.event_generate("<<Error>>", state=406)

    def update_temp_data(self, *args):
        if self.selected_index is not None:
            new_id = self.id_var.get()
            new_name = self.name_var.get()
            if new_id.isdigit():
                new_id = int(new_id)
            else:
                new_id = None
            if new_id is not None and new_name:
                entry = {'id': new_id, 'name': new_name}
                self.temp_data[self.selected_index] = entry
