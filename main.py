from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from modules.auth import AuthScreen
from modules.booking import BookingScreen
from modules.services import ServicesScreen
from modules.profile import ProfileScreen

class MyScreenManager(ScreenManager):
    pass

class MyApp(App):
    def build(self):
        sm = MyScreenManager()
        sm.add_widget(AuthScreen(name='auth'))
        sm.add_widget(BookingScreen(name='booking'))
        sm.add_widget(ServicesScreen(name='services'))
        sm.add_widget(ProfileScreen(name='profile'))
        return sm

if __name__ == '__main__':
    MyApp().run()
