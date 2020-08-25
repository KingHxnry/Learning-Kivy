import kivy
from kivy.app import App
from kivy.graphics import Rectangle
from kivy.uix.widget import Widget
from kivy.graphics import Color
from kivy.graphics import Line


class Touch(Widget):
    def __init__(self, **kwargs):
        super(Touch, self).__init__(**kwargs)

        with self.canvas:
            Color(100, 255, 50, mode='rgb')
            Line(points=(20, 30, 400, 500, 60, 500))
            Color(255, 0, 0, mode='rgb')
            for j in range(0, 600, 100):
                for i in range(0, 600, 100):
                    self.rect = Rectangle(pos=(i, j), size=(50, 50))
            for j in range(50, 600, 100):
                for i in range(50, 600, 100):
                    self.rect = Rectangle(pos=(i, j), size=(50, 50))


    def on_touch_down(self, touch):
        self.rect.pos = touch.pos
        print("Mouse Down", touch)

    def on_touch_move(self, touch):
        self.rect.pos = touch.pos
        print("Mouse Move", touch)

    def on_touch_up(self, touch):
        print("Mouse Up", touch)


class MyApp(App):
    def build(self):
        return Touch()


if __name__ == "__main__":
    MyApp().run()
