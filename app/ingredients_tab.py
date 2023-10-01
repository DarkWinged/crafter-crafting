from app.tab import Tab


class IngredientsTab(Tab):
    def __init__(self, parent_frame, data_list):
        super().__init__(parent_frame, "Ingredients", data_list)
