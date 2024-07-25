from kivymd.app import MDApp
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton, MDIconButton, MDFloatingActionButton, MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivy.lang.builder import Builder
from helpers import username_helper, list_helper, screen_helper, navigation_helper, manager_helper
from kivymd.uix.list import ThreeLineListItem, MDList, ThreeLineIconListItem, IconLeftWidget
from kivymd.uix.list import ThreeLineAvatarListItem, ImageLeftWidget
from kivy.uix.scrollview import ScrollView
from kivymd.uix.list import OneLineListItem
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager

Window.size = (300, 500)


class MenuScreen(Screen):
    pass


class ProfileScreen(Screen):
    pass


class UploadScreen(Screen):
    pass


sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(ProfileScreen(name='profile'))
sm.add_widget(UploadScreen(name='upload'))


class AppFun(MDApp):

    def build(self):
        self.theme_cls.primary_palette = 'Red'
        # self.theme_cls.primary_hue = 'A700'
        self.theme_cls.theme_style = 'Dark'

        # Needed for bottom toolbar to show title, icons, and things
        # self.theme_cls.material_style = 'M2'

        # screen = Builder.load_string(list_helper)
        # screen = Builder.load_string(screen_helper)
        # screen = Builder.load_string(navigation_helper)
        screen = Builder.load_string(manager_helper)
        # screen = Screen()

        self.username = Builder.load_string(username_helper)
        # screen.add_widget(self.username)
        button = MDRectangleFlatButton(text='Show',
                                       pos_hint={'center_x': 0.5, 'center_y': 0.4},
                                       on_release=self.show_data)
        # screen.add_widget(button)

        scroll = ScrollView()
        list_view = MDList()
        scroll.add_widget(list_view)

        for i in range(20):
            icon = IconLeftWidget(icon='android')
            image = ImageLeftWidget(source='logo.png')
            # items = ThreeLineListItem(text='Item ' + str(i), secondary_text='fuck', tertiary_text='my life')
            # items = ThreeLineIconListItem(text='Item ' + str(i), secondary_text='fuck', tertiary_text='my life')
            items = ThreeLineAvatarListItem(text='Item ' + str(i), secondary_text='fuck', tertiary_text='my life')
            # items.add_widget(icon)
            items.add_widget(image)
            list_view.add_widget(items)

        # screen.add_widget(scroll)

        table = MDDataTable(size_hint=(0.9, 0.6),
                            pos_hint={'center_x': 0.5, 'center_y': 0.5},
                            check=True,
                            rows_num=10,
                            column_data=[
                                ('No.', dp(18)),
                                ('Food', dp(20)),
                                ('Calories', dp(20)),
                            ],
                            row_data=[
                                ('1', 'Burger', '300'),
                                ('2', 'Oats', '150'),
                                ('3', 'Oats', '150'),
                                ('4', 'Oats', '150'),
                                ('5', 'Oats', '150'),
                                ('6', 'Oats', '150'),
                                ('7', 'Oats', '150'),
                                ('8', 'Oats', '150'),
                                ('9', 'Oats', '150'),
                            ])
        table.bind(on_check_press=self.check_press)
        table.bind(on_row_press=self.check_press)
        # screen.add_widget(table)

        '''
        

        icon_button = MDFloatingActionButton(icon='android',
                                             pos_hint={'center_x': 0.5, 'center_y': 0.3})

        label = MDLabel(text='Hello Cunts',
                        halign='auto',
                        valign='bottom',
                        theme_text_color='Primary',
                        font_style='H3')

        icon_label = MDIcon(icon='language-python',
                            halign='center')

        
        screen.add_widget(icon_button)
        screen.add_widget(label)
        '''
        return screen

    def on_start(self):
        for i in range(20):
            image = ImageLeftWidget(source='logo.png')
            # items = OneLineListItem(text='item ' + str(i))
            items = ThreeLineAvatarListItem(text='Item ' + str(i), secondary_text='fuck', tertiary_text='my life')
            items.add_widget(image)
            # self.root.ids.container.add_widget(items)

    def show_data(self, obj):
        if self.username.text == "":
            check_string = 'Please enter a username'
        else:
            check_string = self.username.text + ' does not exit'
        close_button = MDFlatButton(text='Close',
                                    on_release=self.close_dialog)
        another_button = MDFlatButton(text='Another')
        self.dialog = MDDialog(title='Username Check',
                          text=check_string,
                          size_hint=(0.7, 1),
                          buttons=[close_button, another_button])
        self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()

    def check_press(self, instance_table, current_row):
        print(instance_table, current_row)

    def check_press(self, instance_table, instance_row):
        print(instance_table, instance_row)

    def navigation_draw(self):
        print("navigation")


AppFun().run()
