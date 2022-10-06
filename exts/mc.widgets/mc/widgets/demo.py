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
        with ui.VStack(style={"margin":5}):
            ui.Label("Hello!", alignment=ui.Alignment.CENTER, height=25)
            ui.Label("Check out this TabGroup Widget.", alignment=ui.Alignment.CENTER)
            ui.Spacer(height=40)

class MyTab2(BaseTab):
    def build_fn(self):
        with ui.VStack(style={"margin":5}):
            with ui.HStack(spacing=2):
                color_model = ui.ColorWidget(0.125, 0.25, 0.5, width=0, height=0).model
                for item in color_model.get_item_children():
                    component = color_model.get_item_value_model(item)
                    ui.FloatDrag(component)

class MyTab3(BaseTab):
    def build_fn(self):
        with ui.VStack(style={"margin":5}):
            with ui.HStack():
                ui.Label("Red: ", height=25)
                ui.FloatSlider()
            with ui.HStack():
                ui.Label("Green: ", height=25)
                ui.FloatSlider()
            with ui.HStack():
                ui.Label("Blue: ", height=25)
                ui.FloatSlider()