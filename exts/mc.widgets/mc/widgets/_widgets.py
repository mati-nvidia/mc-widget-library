from functools import partial
from typing import List

import carb
import omni.ui as ui
from .styles import checkbox_group_style

class CheckBoxGroupModel:
    def __init__(self, option_names:List):
        self.options = []
        self.bool_models = []
        self.subscriptions = []
        self._single_callbacks = []
        self._group_callbacks = []
        for option in option_names:
            self.add_checkbox_option(option)
    
    def add_checkbox_option(self, option_name):
        self.options.append(option_name)
        bool_model = ui.SimpleBoolModel()
        next_index = len(self.bool_models)
        self.bool_models.append(bool_model)
        self.subscriptions.append(bool_model.subscribe_value_changed_fn(partial(self.on_model_value_changed, next_index)))
        return bool_model
    
    def subscribe_value_changed_fn(self, callback_fn):
        self._single_callbacks.append(callback_fn)
    
    def subscribe_group_changed_fn(self, callback_fn):
        self._group_callbacks.append(callback_fn)

    def on_model_value_changed(self, index:int, model:ui.SimpleBoolModel):
        for callback in self._single_callbacks:
            option = self.options[index]
            callback(option, model.as_bool)
        
        for callback in self._group_callbacks:
            checkbox_values = []
            for name, bool_model in zip(self.options, self.bool_models):
                checkbox_values.append((name, bool_model.as_bool))
            callback(checkbox_values)
    
    def get_bool_model(self, option_name):
        index = self.options.index(option_name)
        return self.bool_models[index]

    def get_checkbox_options(self):
        return self.options

    def destroy(self):
        self.subscriptions = None
        self._single_callbacks = None
        self._group_callbacks = None

class CheckBoxGroup:
    def __init__(self, group_name:str, model:CheckBoxGroupModel):
        self.group_name = group_name
        self.model = model
        self._build_widget()

    def _build_widget(self):
        with ui.VStack(width=0, height=0, style=checkbox_group_style):
            ui.Label(f"{self.group_name}:")
            for option in self.model.get_checkbox_options():
                with ui.HStack(name="checkbox_row", width=0, height=0):
                    ui.CheckBox(model=self.model.get_bool_model(option))
                    ui.Label(option, name="cb_label")
    
    def destroy(self):
        self.model.destroy()
