from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

Builder.load_file('kv/booking.kv')
#hello master 2
class BookingScreen(Screen):
    def create_booking(self):
        # Логика создания записи
        pass

    def cancel_booking(self):
        # Логика отмены записи
        pass
