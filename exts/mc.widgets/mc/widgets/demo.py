import carb
import omni.ui as ui
from ._widgets import CheckBoxGroup, CheckBoxGroupModel

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
    
    def destroy(self) -> None:
        super().destroy()
        self.cb_group.destroy()