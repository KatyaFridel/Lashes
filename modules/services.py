from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

Builder.load_file('kv/services.kv')

class ServicesScreen(Screen):
    def list_services(self):
        # Логика отображения услуг
        pass
