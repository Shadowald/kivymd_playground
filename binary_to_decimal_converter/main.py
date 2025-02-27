from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivy.uix.image import Image
from kivymd.uix.button import MDFillRoundFlatIconButton, MDFillRoundFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDTopAppBar


class ConverterApp(MDApp):

    def flip(self):
        if self.state == 0:
            # convert to decimal state
            self.state = 1
            self.toolbar.title = "Decimal to Binary"
            self.input.text = "enter a decimal number"
        else:
            # convert to binary state
            self.state = 0
            self.toolbar.title = "Binary to Decimal"
            self.input.text = "enter a binary number"
        # hide labels until needed
        self.converted.text = ""
        self.label.text = ""

    def convert(self, args):
        try:
            if "." not in self.input.text:
                # a function to fint the decimal/binary equivalent
                if self.state == 0:
                    # binary to decimal
                    value = str(int(self.input.text, 2))
                    self.label.text = "in decimal is:"
                else:
                    # decimal to binary
                    value = bin(int(self.input.text))[2:]
                    self.label.text = "in binary is:"
                self.converted.text = value
            else:
                # floating point numbers conversion
                whole, fract = self.input.text.split(".")

                if self.state == 0:
                    # convert binary to decimal
                    whole = int(whole, 2)
                    floating = 0
                    for idx, digit in enumerate(fract):
                        floating += int(digit) * 2 ** (-(idx + 1))
                    self.label.text = "in decimal is:"
                    self.converted.text = str(whole + floating)
                else:
                    # convert decimal to binary
                    decimal_places = 10
                    whole = bin(int(whole))[2:]
                    fract = float("0." + fract)
                    floating = []
                    for i in range(decimal_places):
                        if fract*2 < 1:
                            floating.append("0")
                            fract *= 2
                        elif fract*2 > 1:
                            floating.append("1")
                            fract = fract*2 - 1
                        elif fract*2 == 1.0:
                            floating.append("1")
                            break
                        self.label.text = "in binary is:"
                        self.converted.text = whole + "." + "".join(floating)
        except ValueError:
            self.converted.text = ""
            if self.state == 0:
                self.label.text = "please enter a valid binary number"
            else:
                self.label.text = "please enter a valid decimal number"

    def build(self):
        self.state = 0
        self.theme_cls.primary_palette = "Indigo"
        screen = MDScreen()

        self.toolbar = MDTopAppBar(title="Binary to Decimal")
        self.toolbar.pos_hint = {"top": 1}
        self.toolbar.right_action_items = [["rotate-3d-variant", lambda x: self.flip()]]
        screen.add_widget(self.toolbar)

        # Logo
        screen.add_widget(Image(
            source="LOGO.png",
            pos_hint={"center_x": 0.5, "center_y": 0.7}
        ))

        # Collect user input
        self.input = MDTextField(
            text="enter a binary number",
            halign="center",
            size_hint=(0.8, 1),
            pos_hint={"center_x": 0.5, "center_y": 0.45},
            font_size=22
        )
        screen.add_widget(self.input)

        # secondary + primary Labels
        self.label = MDLabel(
            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.35},
            theme_text_color="Secondary"
        )

        self.converted = MDLabel(
            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.3},
            theme_text_color="Primary",
            font_style="H5"
        )
        screen.add_widget(self.label)
        screen.add_widget(self.converted)

        # 'Convert' button
        screen.add_widget(MDFillRoundFlatButton(
            text="CONVERT",
            font_size=17,
            pos_hint={"center_x": 0.5, "center_y": 0.15},
            on_press=self.convert
        ))

        return screen


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    ConverterApp().run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
