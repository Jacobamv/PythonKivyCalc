from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
import kivy
from kivy.properties import *


class Screen(Widget):
    innput = NumericProperty()
    first = NumericProperty()
    znak = StringProperty()
    def __init__(self, **kwargs):
        super(Screen, self).__init__(**kwargs)
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)

    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        if keycode[1] == 'numpad1' or keycode[1] == '1':
            self.write(1)
        elif keycode[1] == 'numpad2' or keycode[1] == '2':
            self.write(2)
        elif keycode[1] == 'numpad3' or keycode[1] == '3':
            self.write(3)
        elif keycode[1] == 'numpad4' or keycode[1] == '4':
            self.write(4)
        elif keycode[1] == 'numpad5' or keycode[1] == '5':
            self.write(5)
        elif keycode[1] == 'numpad6' or keycode[1] == '6':
            self.write(6)
        elif keycode[1] == 'numpad7' or keycode[1] == '7':
            self.write(7)
        elif keycode[1] == 'numpad8' or keycode[1] == '8':
            self.write(8)
        elif keycode[1] == 'numpad9' or keycode[1] == '9':
            self.write(9)
        elif keycode[1] == 'numpadadd' or keycode[1] == '+':
            self.plus()
        elif keycode[1] == 'enter':
            self.solve()
        elif keycode[1] == 'numpaddivide' or keycode[1] == '/':
            self.divide()
        elif keycode[1] == 'numpadmul':
            self.multiply()
        elif keycode[1] == 'numpadsubstract' or keycode[1] == '-':
            self.divide()
    
    
    def plus(self):
        self.first = self.innput
        self.innput = 0
        self.znak = '+'
        print(self.innput)

    def minus(self):
        self.first = self.innput
        self.innput = 0
        self.znak = '-'

    def divide(self):
        self.first = self.innput
        self.innput = 0
        self.znak = '/'

    def multiply(self):
        self.first = self.innput
        self.innput = 0
        self.znak = '*'
    
    def solve(self):
        if self.znak == '+':
            self.innput = self.first + self.innput
            print(self.innput)
        elif self.znak == '-':
            self.innput = self.first - self.innput
        elif self.znak == '/':
            self.innput = self.first / self.innput
        elif self.znak == '*':
            self.innput = self.first * self.innput

    def write(self, number):
        if len(str(self.innput)) >= 25:
            return 0
        self.innput = int(str(int(self.innput)) + str(number))

    def clean(self):
        self.first = 0
        self.znak = ''
        self.innput = 0


class Calculator(App):
    def build(self):
        return Screen()

if __name__ == '__main__':
    Calculator().run()
