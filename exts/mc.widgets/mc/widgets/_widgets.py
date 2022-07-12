import carb
from typing import List
import omni.ui as ui
from .styles import checkbox_group_style

class CheckBoxGroup:
    def __init__(self, group_name:str, checkbox_options:List[str]):
        self.group_name = group_name
        self.checkbox_options = checkbox_options
        self.cb_group_model = CheckBoxGroupModel()
        self._build_widget()

    def _build_widget(self):
        with ui.VStack(width=0, height=0, style=checkbox_group_style):
            ui.Label(f"{self.group_name}:")
            for item in self.checkbox_options:
                with ui.HStack(name="checkbox_row", width=0, height=0):
                    model = self.cb_group_model.add_bool_model()
                    ui.CheckBox(model=model)
                    ui.Label(item, name="cb_label")
    
    def destroy(self):
        self.cb_group_model.destroy()

class CheckBoxGroupModel:
    def __init__(self):
        self.sub_models = []
        self.subscriptions = []
    
    def add_bool_model(self):
        model = ui.SimpleBoolModel()
        self.sub_models.append(model)
        self.subscriptions.append(model.subscribe_value_changed_fn(self.on_model_value_changed))
        return model

    def on_model_value_changed(self, model:ui.SimpleBoolModel):
        for i, model in enumerate(self.sub_models):
            carb.log_info(f"Checkbox[{i}] is: {model.as_bool}")
    
    def destroy(self):
        self.subscriptions = None
    