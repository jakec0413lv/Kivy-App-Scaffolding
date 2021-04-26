from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import json
from datetime import datetime

Builder.load_file('design.kv')

#Shift + alt + F to format JSON data

class LoginScreen(Screen):
    def sign_up(self):
        self.manager.current = "sign_up_screen"

class SignUpScreen(Screen):
    def add_user(self, uname, pwd):
        with open("users.json") as file:
            users = json.load(file)

        users[uname] = {'username': uname, 'password' : pwd,
        'created': datetime.now().strftime("%m-%d-%Y, %H:%M:%S")}

        with open("users.json", 'w') as file:
            json.dump(users, file)
        
        self.manager.current = "sign_up_success"

class SignUpSuccess(Screen):
    def switchToLogin(self):
        self.manager.transition.direction = 'right' #Page switch orientation
        self.manager.current = "login_screen"

class RootWidget(ScreenManager):
    pass

class MainApp(App):
    def build(self):
        return RootWidget()


if __name__ == "__main__":
    MainApp().run()
