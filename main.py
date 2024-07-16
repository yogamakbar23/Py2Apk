import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup

kivy.require('1.11.1')

class LoginScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.spacing = 80
        self.padding = [80, 80, 80, 80]

        self.add_widget(Label(text='Username', color=(0, 1, 0, 1)))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)

        self.add_widget(Label(text='Password', color=(0, 1, 0, 1)))
        self.password = TextInput(password=True, multiline=False)
        self.add_widget(self.password)

        self.login_button = Button(text='Login', background_color=(1, 0, 0, 1))
        self.login_button.bind(on_press=self.validate_login)
        self.add_widget(self.login_button)

    def validate_login(self, instance):
        username = self.username.text
        password = self.password.text

        if username == 'admin' and password == '1234':
            self.show_popup('Login Success', 'Welcome, ' + username)
        else:
            self.show_popup('Login Failed', 'Invalid username or password')

    def show_popup(self, title, message):
        popup_layout = BoxLayout(orientation='vertical', padding=10)
        popup_layout.add_widget(Label(text=message))
        close_button = Button(text='Close', size_hint=(1, 0.2))
        popup_layout.add_widget(close_button)

        popup = Popup(title=title, content=popup_layout, size_hint=(None, None), size=(400, 200))
        popup.open()
        close_button.bind(on_press=popup.dismiss)

class LoginApp(App):
    def build(self):
        return LoginScreen()

if __name__ == '__main__':
    LoginApp().run()
