from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

Builder.load_file('kv/auth.kv')

class AuthScreen(Screen):
    def login(self):
        # Логика входа
        pass

    def register(self):
        # Логика регистрации
        pass
