import tkinter as tk


class ValueBox:
    def __init__(self, parent_frame: tk.Frame, label_text: str, update_data: callable, row: int=0, column: int=0, type: str='str'):
        """ ValueBox is a class that represents a value box in the editor tool.

        Args:
            parent_frame (tk.Frame): Parent widget for the value box
            label_text (str): Text for the label
            update_data (callable): A function that updates the data model
            row (int, optional): Row number. Defaults to 0.
            column (int, optional): Column number. Defaults to 0.
            type (str, optional): Type of the value. Defaults to 'str'.
        """
        self.label = tk.Label(parent_frame, text=f"{label_text}:")
        self.label.grid(row=row, column=column)
        self.var = tk.StringVar()
        self.entry = tk.Entry(parent_frame, textvariable=self.var)
        self.entry.grid(row=row, column=column + 1)
        self.var.trace("w", update_data)
        self.type = type

    def get(self) -> None or int or float or str or bool or list or dict:
        """ Returns the value of the entry as the specified type. If the value cannot be converted to the specified type, None is returned.
        
        Returns:
            None or int or float or str or bool or list or dict: The value of the entry as the specified type. If the value cannot be converted to the specified type, None is returned.
        """
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
            return value.lower() == 'true'
        elif self.type == 'list':
            return value.split(",")
        elif self.type == 'dict':
            return dict([tuple(item.split(":")) for item in value.split(",")])
        else:
            return None
        
    def set(self, value: int or float or str or bool or list or dict):
        """ Sets the value of the entry.
        
        Args:
            value (int or float or str or bool or list or dict): The value to set the entry to.
        """
        self.var.set(f'{value}')

    def destroy(self):
        """ Destroys the value box.
        """
        self.label.destroy()
        self.entry.destroy()