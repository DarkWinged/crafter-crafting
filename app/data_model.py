import json
import yaml


class DataModel:
    """"DataModel is a class that represents the data model for the recipe editor tool."""
    def __init__(self):
        """" DataModel is a class that represents the data model for the recipe editor tool."""
        self.ingredients = []
        self.recipes = []

    def load_data(self, file_path: str):
        """ Loads data from a file.
        
        Args:
            file_path (str): Path to the file
        """
        with open(file_path, "r", encoding="utf-8") as file:
            if file_path.endswith(".json"):
                data = json.load(file)
            elif file_path.endswith(".yaml"):
                data = yaml.safe_load(file)
            self.ingredients = data.get('ingredients', [])
            self.recipes = data.get('recipes', [])

    def save_data(self, file_path: str):
        """ Saves the data to a file.
        
        Args:
            file_path (str): Path to the file
        """
        data = {
            'ingredients': self.ingredients,
            'recipes': self.recipes
        }
        with open(file_path, "w", encoding="utf-8") as file:
            if file_path.endswith(".json"):
                json.dump(data, file, indent=4)
            elif file_path.endswith(".yaml"):
                yaml.dump(data, file, default_flow_style=False)
