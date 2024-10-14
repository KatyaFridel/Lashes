from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

Builder.load_file('kv/profile.kv')
#Marina
class ProfileScreen(Screen):
    def view_profile(self):
        # Логика просмотра профиля
        pass

    def edit_profile(self):
        # Логика редактирования профиля
        pass
