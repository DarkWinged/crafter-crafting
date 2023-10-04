import tkinter as tk


class ValueBox:
    def __init__(self, parent_frame: tk.Frame, label_text: str, update_data: callable, row: int=0, column: int=0, type: str='str'):
        self.label = tk.Label(parent_frame, text=f"{label_text}:")
        self.label.grid(row=row, column=column)
        self.var = tk.StringVar()  # Create StringVar for ID
        self.entry = tk.Entry(parent_frame, textvariable=self.var)
        self.entry.grid(row=row, column=column + 1)
        self.var.trace("w", update_data)  # Attach trace to update data_list
        self.type = type

    def get(self):
        value = self.var.get()
        if self.type == 'int':
            try:
                return int(value)
            except ValueError:
                return None
        elif self.type == 'float':
            try:
                return float(value)
            except ValueError:
                return None
        elif self.type == 'str':
            return value
        elif self.type == 'bool':
            if value.lower() in ["true", "false"]:
                return value.lower() == "true"
            else:
                return None
        elif self.type == 'list':
            return value.split(",")
        elif self.type == 'dict':
            return dict([tuple(item.split(":")) for item in value.split(",")])
        else:
            return None
        
    def set(self, value: any):
        self.var.set(value)

    def destroy(self):
        self.label.destroy()
        self.entry.destroy()