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

navigation_helper = """
Screen:
    MDNavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'
                    MDTopAppBar:
                        title: 'Demo Application'
                        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
                        elevation: 10
                        
                    Widget: 
                    
        MDNavigationDrawer:
            id: nav_drawer
            BoxLayout:
                orientation: 'vertical'
                spacing: '8dp'
                padding: '8dp'
                Image:
                    source: 'logo.png'
                MDLabel:
                    text: 'Name'
                    font_style: 'Subtitle1'
                    size_hint_y: None
                    height: self.texture_size[1]
                MDLabel:
                    text: 'email@address.com'
                    font_style: 'Caption'
                    size_hint_y: None
                    height: self.texture_size[1]
                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text: 'Profile'
                            IconLeftWidget:
                                icon: 'face-profile-woman'
                        OneLineIconListItem:
                            text: 'Upload'
                            IconLeftWidget:
                                icon: 'file-upload'
                        OneLineIconListItem:
                            text: 'Logout'
                            IconLeftWidget:
                                icon: 'logout'
                                
                    
"""

manager_helper = """
ScreenManager:
    MenuScreen:
    ProfileScreen:
    UploadScreen:
    
<MenuScreen>:
    name: 'Menu'
    MDRectangleFlatButton:
        text: 'Profile'
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        on_press: root.manager.current = 'Profile'
    MDRectangleFlatButton:
        text: 'Upload'
        pos_hint: {'center_x': 0.5, 'center_y': 0.6}
        on_press: root.manager.current = 'Upload'

<ProfileScreen>:
    name: 'Profile'
    MDLabel:
        text: 'Welcome dude'
        halign: 'center'
    MDRectangleFlatButton:
        text: 'Back'
        pos_hint: {'center_x': 0.5, 'center_y': 0.2}
        on_press: root.manager.current = 'Menu'
        
<UploadScreen>:
    name: 'Upload'
    MDLabel:
        text: 'Upload files'
        halign: 'center'
    MDRectangleFlatButton:
        text: 'Back'
        pos_hint: {'center_x': 0.5, 'center_y': 0.2}
        on_press: root.manager.current = 'Menu'
"""