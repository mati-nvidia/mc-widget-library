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
    "TabGroupBorder": {
        "background_color": ui.color.transparent,
        "border_color": ui.color(25), 
        "border_width": 1
    },
    "Rectangle::TabGroupHeader" : {
        "background_color": ui.color(20),
    },
    "ZStack::TabGroupHeader":{
        "margin_width": 1
    }
}

tab_style = {
    "" : {
        "background_color": ui.color(31),
        "corner_flag": ui.CornerFlag.TOP, 
        "border_radius": 4,
        "color": ui.color(127)
    },
    ":selected": {
        "background_color": ui.color(56),
        "color": ui.color(203)
    },
    "Label": {
        "margin_width": 5,
        "margin_height": 3
    }
}