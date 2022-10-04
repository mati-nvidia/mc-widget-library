import carb
import omni.ui as ui
from ._widgets import CheckBoxGroup, CheckBoxGroupModel, TabGroup, BaseTab

class DemoWindow(ui.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        with self.frame:
            with ui.VStack():
                model = CheckBoxGroupModel(["Red", "Blue", "Green"])
                self.cb_group = CheckBoxGroup("My CheckBox Group", model)
                def checkbox_changed(option_name, value):
                    carb.log_info("This checkbox changed.")
                    carb.log_info(f"{option_name} is {value}")

                def checkbox_group_changed(values):
                    carb.log_info("The state of my CheckBoxGroup is now:")
                    for name, value in values:
                        carb.log_info(f"{name} is {value}")
                model.subscribe_value_changed_fn(checkbox_changed)
                model.subscribe_group_changed_fn(checkbox_group_changed)
                tab_group = TabGroup([MyTab1("Tab Header 1"), MyTab2("Tab Header 2"), MyTab3("Tab Header 3"),])

                
    
    def destroy(self) -> None:
        super().destroy()
        self.cb_group.destroy()


class MyTab1(BaseTab):
    def build_fn(self):
        with ui.VStack():
            ui.Button("Hello")

class MyTab2(BaseTab):
    def build_fn(self):
        with ui.VStack():
            ui.Label("Tab 2")
            model = CheckBoxGroupModel(["Red", "Blue", "Green"])
            cb_group = CheckBoxGroup("My CheckBox Group", model)

class MyTab3(BaseTab):
    def build_fn(self):
        with ui.VStack():
            ui.Label("Tab 3")
            with ui.HStack():
                ui.Label("My String Field: ")
                ui.StringField()