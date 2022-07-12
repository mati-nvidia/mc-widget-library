
import omni.ui as ui
from ._widgets import CheckBoxGroup

class DemoWindow(ui.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        with self.frame:
            with ui.VStack():
                self.cb_group = CheckBoxGroup("My CheckBox Group", ["Red", "Blue", "Green"])
    
    def destroy(self) -> None:
        super().destroy()
        self.cb_group.destroy()