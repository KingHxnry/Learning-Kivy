import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import ButtonBehavior
from kivy.vector import Vector
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.config import Config
from kivy.core.window import Window


class CircleButton(ButtonBehavior, Label):
    def collide_point(self, x, y):
        return Vector(x, y).distance(self.center) <= self.width / 2

class ZeroButton(ButtonBehavior, Label):
    def collide_point(self, x, y):
        return Vector(x, y).distance(self.center) <= self.width / 2

class OrangeCircleButton(ButtonBehavior, Label):
    def collide_point(self, x, y):
        return Vector(x, y).distance(self.center) <= self.width / 2

class LightCircleButton(ButtonBehavior, Label):
    def collide_point(self, x, y):
        return Vector(x, y).distance(self.center) <= self.width / 2

class MyGrid(GridLayout):
    Config.set('graphics', 'width', '200')
    Config.set('graphics', 'height', '200')
    def calculate(self, temp):
        if temp:
            try:
                self.display.text = str(eval(temp))
            except Exception:
                self.display.text = "Error"

    Window.size = (367, 525)


class MyApp(App):
    def build(self):
        return MyGrid()




if __name__ == "__main__":
    MyApp().run()