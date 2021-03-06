from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager , Screen
from kivy.uix.gridlayout import GridLayout
Builder.load_file('design.kv')
import json
from datetime import datetime

class LoginScreen(Screen):
    def sign_up(self):
       self.manager.current = "sign_up_screen"
    
    def login(self,uname,pword):
        with open("users.json") as file:
            users = json.load(file)
        print(users)
        if uname in users and users[uname]['password'] == pword:
            self.manager.current = 'Login_screen_success'
        else:
            self.ids.login_wrong.text = "Wrong username or password!"



class RootWidget(ScreenManager):
    pass


class SignUpScreen(Screen):
    def add_user(self,uname,pword):
        with open("users.json") as file:
            users = json.load(file)
        
        users[uname] = {'username':uname, 
        'password':pword, 'created':datetime.now().strftime("%Y-%m-%d %H-%M-%S")}
        print(users)

        with open("users.json", 'w') as file:
            json.dump(users, file)
        self.manager.current = "sign_up_screen_success"

class SignUpScreenSuccess(Screen):
    def go_to_Login(self):
        self.manager.transition.direction = 'right'
        self.manager.current = "Login_screen"

class LoginScreenSuccess(Screen):
    def log_out(self):
        self.manager.transition.direction = "right"
        self.manager.current = "Login_screen"



class MainApp(App): 
    def build(self):
        return RootWidget()

if __name__ == "__main__":
    MainApp().run()

