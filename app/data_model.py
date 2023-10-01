import json
import yaml


class DataModel:
    def __init__(self):
        self.ingredients = []
        self.recipes = []

    def load_data(self, file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            if file_path.endswith(".json"):
                data = json.load(file)
            elif file_path.endswith(".yaml"):
                data = yaml.safe_load(file)
            self.ingredients = data.get('ingredients', [])
            self.recipes = data.get('recipes', [])

    def save_data(self, file_path):
        # Save ingredients and recipes separately in the file
        data = {
            'ingredients': self.ingredients,
            'recipes': self.recipes
        }
        with open(file_path, "w", encoding="utf-8") as file:
            if file_path.endswith(".json"):
                json.dump(data, file, indent=4)
            elif file_path.endswith(".yaml"):
                yaml.dump(data, file, default_flow_style=False)
