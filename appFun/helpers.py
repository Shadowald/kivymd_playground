username_helper = """
MDTextField:
    hint_text: "Enter Username"
    helper_text: "or click on forget username"
    helper_text_mode: "on_focus"
    icon_right: "android"
    icon_right_color: app.theme_cls.primary_color
    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
    size_hint_x: None
    width: 300    
"""

list_helper = """
Screen:
    ScrollView:
        MDList:
            id: container
"""

screen_helper = """
Screen:
    BoxLayout: 
        orientation: 'vertical'
        MDTopAppBar:
            title: 'Demo'
            left_action_items: [["menu", lambda x: app.navigation_draw()]]
            right_action_items: [["clock", lambda x: app.navigation_draw()]]
            elevation: 8
        MDLabel:
            text: 'Hello World'
            halign: 'center'
            valign: 'top'
        MDBottomAppBar:
        
            MDTopAppBar:
                title: 'Help'
                icon: 'git'
                type: 'bottom'
                mode: 'end'
                left_action_items: [["coffee", lambda x: app.navigation_draw()]]
                on_action_button: app.navigation_draw()
"""