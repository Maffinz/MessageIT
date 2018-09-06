import kivy

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from user import User
from validation import Validation

user = None
sm = ScreenManager()

def changeScreen(screenName):
    sm.current = screenName

class Running(Screen):

    def __init__(self, **kwargs):
        super(Running, self).__init__(**kwargs)
        self.cols = 2;
        self.runningLabel = Label(text="Status: ")
        self.Status = Label(text="Running", color=[0,1,0,1])

        infoGrid = GridLayout(cols=2, row_force_default=True, row_default_height=40, padding=100)
        button_grid = GridLayout(col=1, row_force_default=True, row_default_height=40, padding=100)
        root = BoxLayout(orientation="vertical")

        infoGrid.add_widget(self.runningLabel)
        infoGrid.add_widget(self.Status)

        self.back = Button(text="Back", font_size=14)
        self.back.bind(on_press=self.onBackPress)

        button_grid.add_widget(self.back)

        root.add_widget(infoGrid)
        root.add_widget(button_grid)

        self.add_widget(root)

    def onBackPress(self, btn):
        changeScreen("Log In")

class LogIn(Screen):
    def __init__(self, **kwargs):
        super(LogIn, self).__init__(**kwargs)
        self.cols = 2;
        userInfo = GridLayout(cols=1, row_force_default=True, row_default_height=40, padding=100, size_hint_x=4)
        button_grid = GridLayout(cols=1, row_force_default=True, row_default_height=40, padding=100, size_hint_x=3)
        root_widget = BoxLayout(orientation='horizontal')

        #SETUP -> userInfo
        #TextInput For User userInfo
        self.mail = TextInput(multiline=False, hint_text="example123@gmail.com", write_tab=False)
        self.mailPassword = TextInput(multiline=False, hint_text="password", password=True, write_tab=False)
        self.targetNumber = TextInput(multiline=False, hint_text="123 456 7890", write_tab=False)
        self.targetCarrier = TextInput(multiline=False, hint_text="Verizon", write_tab=False)
        self.message = TextInput(multiline=True, hint_text="Message", write_tab=False)
        self.networkSSID = TextInput(multiline=False, hint_text="Desire Network SSID", write_tab=False)
        self.infoLabel = Label(text="", padding=[100, 100])

        #SETUP -> button_grid
        #button_grid Widgets
        self.Load = Button(text="Load", font_size=14)
        self.Load.bind(on_press=self.onLoadClick)
        self.Done = Button(text="Save", font_size=14)
        self.Done.bind(on_press=self.onDoneClick)
        self.Clear = Button(text="Clear", font_size=14)
        self.Clear.bind(on_press=self.onClearClick)
        self.Send = Button(text="Send", font_size=14)
        self.Send.bind(on_press=self.onSendClick)
        self.Exit = Button(text="Exit", font_size=14)
        self.Exit.bind(on_press=self.onExitClick)



        #ADDING -> USERINFO
        #Adding To userInfo Widgets
        userInfo.add_widget(self.mail)
        userInfo.add_widget(self.mailPassword)
        userInfo.add_widget(self.targetNumber)
        userInfo.add_widget(self.targetCarrier)
        userInfo.add_widget(self.message)
        userInfo.add_widget(self.networkSSID)
        userInfo.add_widget(self.infoLabel)

        #ADDING -> BUTTON_GRID
        #Adding to button_grid Widgets
        button_grid.add_widget(self.Load)
        button_grid.add_widget(self.Done)
        button_grid.add_widget(self.Clear)
        button_grid.add_widget(self.Send)
        button_grid.add_widget(self.Exit)

        #ADDING -> ROOT_WIDGET
        #Adding to the root Layout
        root_widget.add_widget(userInfo)
        root_widget.add_widget(button_grid)

        self.add_widget(root_widget)

    def onDoneClick(self, btn):
        global user
        values = Validation().isEmpty(self.mail.text, self.mailPassword.text, self.targetNumber.text, self.targetCarrier.text, self.message.text, self.networkSSID.text)
        if values[0]:
            self.infoLabel.text = values[1]
        if Validation().carrierExist(self.targetCarrier.text) == False: #Checks if Carrier Exists
            self.infoLabel.text += "Carrier Does not exis\n"
            self.infoLabel.text += "Here is a list: \n"
            self.infoLabel.text += "Verizon, ATT, Cricket, MetroPCS, Sprint, T-Mobile \n"
        if Validation().EmailVerification(self.mail.text) == False: #Checks if Email Is valid
            self.infoLabel.text += "Enter a Valid Email \n"
        if Validation().PhoneNumberValidation(self.targetNumber.text) == False:
            self.infoLabel.text += "Not a valid phone number"
        else: #sender, Target, Message, Password
            self.infoLabel.text = ""
            user = User(sender=self.mail.text, target=self.targetNumber.text, message=self.message.text, password=self.mailPassword.text, target_carrier=self.targetCarrier.text, network=self.networkSSID.text)
            user.Save()
            self.onClearClick("None")
            self._start()


    def onExitClick(self, btn):
        exit()
    def onClearClick(self, btn):
        self.mail.text = ""
        self.mailPassword.text = ""
        self.targetNumber.text = ""
        self.targetCarrier.text = ""
        self.message.text = ""
        self.networkSSID.text = ""
        self.infoLabel.text = ""
    def onSendClick(self, btn):
        try:
            user.sendMessage()
        except:
            self.infoLabel.text = "Message Can't be send at this moment"

    def onLoadClick(self, btn):
        global user
        global sm
        user = User()
        self.infoLabel.text = user.Load()
        self._start()

    def _start(self):
        if user.checkSetNetwork(user.getSSID()):
            user.sendMessage()
        else:
            self.infoLabel.text = "Not Set Network \n" + self.networkSSID.text
        changeScreen("Status")


sm.add_widget(LogIn(name="Log In"))
sm.add_widget(Running(name="Status"))
class MyApp(App):
    def build(self):
        self.title = "Automated Message"
        #Start with log in
        return sm




if __name__ == '__main__':
    MyApp().run()
