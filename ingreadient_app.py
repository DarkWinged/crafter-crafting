import tkinter as tk
import tkinter.filedialog as filedialog
from os import path
from tkinter.ttk import Notebook
from app.data_model import DataModel
from app.ingredients_tab import IngredientsTab
from app.recipes_tab import RecipesTab


class MainApplication:
    def __init__(self, parent_widget: tk.Tk):
        self.parent_widget: tk.Tk = parent_widget
        self.parent_widget.title("Manager")

        self.data_model = DataModel()

        self.tabs = Notebook(self.parent_widget)
        self.tabs.pack(fill=tk.BOTH, expand=True)

        self.ingredients_frame = tk.Frame(self.tabs)
        self.recipes_frame = tk.Frame(self.tabs)

        self.warning_label = tk.Label(self.parent_widget, text="", fg="yellow", anchor="w")
        self.warning_label.pack(fill="x")

        self.error_label = tk.Label(self.parent_widget, text="", fg="red", anchor="w")
        self.error_label.pack(fill="x")

        self.info_label = tk.Label(self.parent_widget, text="", anchor="w")
        self.info_label.pack(fill='x')

        self.tabs.add(self.ingredients_frame, text="Ingredients")
        self.tabs.add(self.recipes_frame, text="Recipes")

        self.ingredients_tab = IngredientsTab(self.ingredients_frame, self.data_model.ingredients)
        self.recipes_tab = RecipesTab(self.recipes_frame, self.data_model.recipes, self.ingredients_tab.data_list)

        self.file_path = None

        menubar = tk.Menu(parent_widget)
        parent_widget.config(menu=menubar)

        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)

        file_menu.add_command(label="New", command=self.new)
        file_menu.add_separator()
        file_menu.add_command(label="Open", command=self.load_data)
        file_menu.add_separator()
        file_menu.add_command(label="Save", command=self.save_data)
        file_menu.add_command(label="Save As", command=self.save_data_as)

        self.parent_widget.after(5000, self.detect_warnings)
        self.parent_widget.bind("<<Error>>", self.display_error)   

    def load_data(self):
        file_path = filedialog.askopenfilename(title="Select a file",
                                               filetypes=(("YAML files", "*.yaml"), ("JSON files", "*.json"),
                                                          ("All files", "*.*")))
        if file_path:
            try:
                self.data_model.load_data(file_path)
                self.ingredients_tab.load_data(self.data_model.ingredients)
                self.recipes_tab.load_data(self.data_model.recipes, self.ingredients_tab.data_list)
                self.file_path = file_path
            except FileNotFoundError:
                self.display_error("File not found")

    def save_data(self):
        if self.file_path:
            try:
                self.data_model.save_data(self.file_path)
                self.show_info("Data saved successfully")
            except FileNotFoundError:
                self.display_error("File not found")
        else:
            self.save_data_as()

    def save_data_as(self):
        file_name = path.basename(self.file_path) if self.file_path else "untitled"
        file_path = filedialog.asksaveasfilename(title="Save As",
                                                 initialfile=file_name,
                                                 filetypes=(("YAML files", "*.yaml"), ("JSON files", "*.json"),
                                                            ("All files", "*.*")))
        if file_path:
            try:
                self.data_model.ingredients = self.ingredients_tab.data_list
                self.data_model.recipes = self.recipes_tab.data_list
                self.data_model.save_data(file_path)
                self.file_path = file_path
                self.show_info("Data saved successfully")
            except FileNotFoundError:
                self.display_error("File not found")

    def new(self):
        self.data_model = DataModel()
        self.ingredients_tab.load_data(self.data_model.ingredients)
        self.recipes_tab.load_data(self.data_model.recipes, self.ingredients_tab.data_list)
        self.file_path = None

    def detect_warnings(self):
        warnings = []
        warnings.extend(self.detect_overlapping_ids(self.ingredients_tab.data_list))
        warnings.extend(self.detect_overlapping_ids(self.recipes_tab.data_list))
        self.warning_label.config(text='\n'.join([f'Warning! {message}' for message in warnings]))
        self.parent_widget.after(5000, self.detect_warnings)

    def detect_overlapping_ids(self, source: list[dict[str, str or int]]) -> list[str]:
        warnings = []
        ids = [
            ingredient.get('id')
            for ingredient
            in source
        ]

        for entry_id in ids:
            if ids.count(entry_id) > 1:
                entries = [entry['name'] for entry in source if entry['id'] == entry_id]
                message = f"Duplicate ID: [{entry_id}] found in entries: {entries}"
                if message not in warnings:
                    warnings.append(message)

        return warnings

    def display_error(self, event: tk.Event):
        if event.state == 406:
            self.error_label.config(text="Invalid input")
        self.parent_widget.after(5000, self.clear_error)
    
    def clear_error(self):
        self.error_label.config(text="")

    def show_info(self, message):
        self.info_label.config(text=message, fg="green")

if __name__ == "__main__":
    root = tk.Tk()
    app = MainApplication(root)
    root.mainloop()
