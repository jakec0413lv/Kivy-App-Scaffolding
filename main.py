from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import json, glob
from pathlib import Path
import random

Builder.load_file('design.kv')

#Shift + alt + F to format JSON data

class LoginScreen(Screen):
    def sign_up(self):
        self.manager.current = "sign_up_screen"

    def login(self, uname, pwd):
        with open("users.json") as file:
            users = json.load(file)
        if uname in users and users[uname]['password'] == pwd:
            self.manager.current = "login_screen_success"
        else:
            self.ids.login_wrong.text = "Wrong username or password!"

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

class LoginScreenSuccess(Screen):
    def logout(self):
        self.manager.transition.direction = 'right'
        self.manager.current = "login_screen"

    def showText(self, emotion):
        emotion = emotion.lower()
        availableEmotions = glob.glob("quotes/*txt")
        availableEmotions = [Path(filename).stem for filename in availableEmotions]
        if emotion in availableEmotions:
            with open(f"quotes/{emotion}.txt", encoding="utf-8") as file:
                quotes = file.readlines()
            self.ids.quote.text = random.choice(quotes) #random.choice returns randomly selected list element
        else:
            self.ids.quote.text = "Try another feeling..."


class RootWidget(ScreenManager):
    pass

class MainApp(App):
    def build(self):
        return RootWidget()


if __name__ == "__main__":
    MainApp().run()
