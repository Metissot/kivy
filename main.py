import kivy
kivy.require('1.11.1')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config

Config.set('graphics', 'width', 1024)
Config.set('graphics', 'height', 720)

class Contenedor_01(BoxLayout):
    None

class MainApp(App):
    title = 'probando kivy'
    def build(self):
        return Contenedor_01()

if __name__ == '__main__':
    MainApp().run()