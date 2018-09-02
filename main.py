import kivy

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from user import User
from validation import Validation

class MyApp(App):

    user = None

    def build(self):
        self.title = "Automated Message"
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
        self.infoLabel = Label(text="", padding=[100, 100])

        #SETUP -> button_grid
        #button_grid Widgets
        self.Load = Button(text="Load", font_size=14)
        self.Load.bind(on_press=self.onLoadClick)
        self.Done = Button(text="Done", font_size=14)
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
        #Return Root Widgets
        return root_widget

    def onDoneClick(self, btn):
        values = Validation().isEmpty(self.mail.text, self.mailPassword.text, self.targetNumber.text, self.targetCarrier.text, self.message.text)
        if values[0]:
            self.infoLabel.text = values[1]
        elif Validation().carrierExist(self.targetCarrier.text) == False:
            self.infoLabel.text += "Carrier Does not exis\n"
            self.infoLabel.text += "Here is a list: \n"
            self.infoLabel.text += "Verizon, ATT, Cricket, MetroPCS, Sprint, T-Mobile"
        else: #sender, Target, Message, Password
            self.infoLabel.text = ""
            MyApp.user = User(sender=self.mail.text, target=self.targetNumber.text, message=self.message.text, password=self.mailPassword.text, target_carrier=self.targetCarrier.text)
            MyApp.user.Save()
        self.onClearClick("None")

    def onExitClick(self, btn):
        exit()
    def onClearClick(self, btn):
        self.mail.text = ""
        self.mailPassword.text = ""
        self.targetNumber.text = ""
        self.targetCarrier.text = ""
        self.message.text = ""
        self.infoLabel.text = ""
    def onSendClick(self, btn):
        try:
            MyApp.user.sendMessage()
            self.infoLabel.text = "Message Sent!"
        except:
            self.infoLabel.text = "Message Can't be send at this moment"

    def onLoadClick(self, btn):
        MyApp.user = User()
        self.infoLabel.text = MyApp.user.Load()


if __name__ == '__main__':
    MyApp().run()
