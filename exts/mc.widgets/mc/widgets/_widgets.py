from functools import partial
from typing import List

import omni.ui as ui
from . import styles

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
        with ui.VStack(width=0, height=0, style=styles.checkbox_group_style):
            ui.Label(f"{self.group_name}:")
            for option in self.model.get_checkbox_options():
                with ui.HStack(name="checkbox_row", width=0, height=0):
                    ui.CheckBox(model=self.model.get_bool_model(option))
                    ui.Label(option, name="cb_label")
    
    def destroy(self):
        self.model.destroy()

class BaseTab:
    def __init__(self, name):
        self.name = name
    
    def build_fn(self):
        """Builds the contents for the tab.

        You must implement this function with the UI construction code that you want for
        you tab. This is set to be called by a ui.Frame so it must have only a single
        top-level widget.
        """
        raise NotImplementedError("You must implement Tab.build_fn")

class TabGroup:
    def __init__(self, tabs: List[BaseTab]):
        self.frame = ui.Frame(build_fn=self._build_widget)
        if not tabs:
            raise ValueError("You must provide at least one BaseTab object.")
        self.tabs = tabs
        self.tab_containers = []
        self.tab_headers = []
    
    def _build_widget(self):
        with ui.ZStack(style=styles.tab_group_style):
            ui.Rectangle(style_type_name_override="TabGroupBorder")
            with ui.VStack():
                ui.Spacer(height=1)
                with ui.ZStack(height=0, name="TabGroupHeader"):
                    ui.Rectangle(name="TabGroupHeader")
                    with ui.VStack():
                        ui.Spacer(height=2)
                        with ui.HStack(height=0, spacing=4):
                            for x, tab in enumerate(self.tabs):
                                tab_header = ui.ZStack(width=0, style=styles.tab_style)
                                self.tab_headers.append(tab_header)
                                with tab_header:
                                    rect = ui.Rectangle()
                                    rect.set_mouse_released_fn(partial(self._tab_clicked, x))
                                    ui.Label(tab.name)
                with ui.ZStack():
                    for x, tab in enumerate(self.tabs):
                        container_frame = ui.Frame(build_fn=tab.build_fn)
                        self.tab_containers.append(container_frame)
                        container_frame.visible = False
        
        # Initialize first tab
        self.select_tab(0)
    
    def select_tab(self, index: int):
        for x in range(len(self.tabs)):
            if x == index:
                self.tab_containers[x].visible = True
                self.tab_headers[x].selected = True
            else:
                self.tab_containers[x].visible = False
                self.tab_headers[x].selected = False
    
    def _tab_clicked(self, index, x, y, button, modifier):
        if button == 0:
            self.select_tab(index)
    
    def append_tab(self, tab: BaseTab):
        pass
    
    def destroy(self):
        self.frame.destroy()

