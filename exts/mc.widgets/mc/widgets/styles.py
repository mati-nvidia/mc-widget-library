import omni.ui as ui

checkbox_group_style = {
    "HStack::checkbox_row" : {
        "margin_width": 18,
        "margin": 2
    },
    "Label::cb_label": {
        "margin_width": 10
    }
}

tab_group_style = {
    "Frame::tab_row" : {
        "background_color": ui.color.blue,
        "color": ui.color.blue
    },
    "Tab": {
        "background_color": ui.color.cyan,
    },
    "Tab:selected": {
        "background_color": ui.color.green,
    }
}