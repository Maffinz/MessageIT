import smtplib
from enum import Enum

carrier = {
        "Verizon" : "@vtext.com",
        "ATT": "@txt.att.net",
        "Cricket": "@mms.cricketwireless.net",
        "MetroPCS" : "@mymetropcs.com",
        "Sprint" : "@messaging.sprintpcs.com",
        "T-Mobile": "@tmomail.net",
        }

class User:

    class Data(Enum):
        sender = 0
        password = 1
        target = 2
        message = 3

    def __init__(self, **kwarg):
        if kwarg:
            self.sender = kwarg["sender"]
            self.target = kwarg["target"] + carrier[kwarg["target_carrier"]]
            self.message = kwarg["message"]
            self.password = kwarg["password"]
        else:
            self.sender = ""
            self.target = ""
            self.message = ""
            self.password = ""

    #Set up Functions
    def setUpSender(self, gmail, AuthPass):
        self.sender = gamail
        self.password = AuthPass
    def setUpTarget(self, phoneNumber, targetCarrier):
        self.target = phoneNumber + carrier[targetCarrier]
    def setUpMessage(self, userMessage):
        self.message = userMessage

    #Save
    def Save(self):
        myFile = open("dat.inf", "w+")
        myFile.write(self.sender + '\n' + self.password + '\n' + self.target + '\n' + self.message + '\n')
        myFile.close()
    #Load
    def Load(self):
        try:
            myFile = open("dat.inf", "r+")
            content = myFile.readlines()
            content = [x.strip() for x in content]
            self.sender = content[self.Data.sender.value]
            self.password = content[self.Data.password.value]
            self.target = content[self.Data.target.value]
            self.message = content[self.Data.message.value]
            myFile.close()
            return "Loaded!"
        except IOError:
            return "File Cannot be Opened"

    #Send Message
    def sendMessage(self):
        server = smtplib.SMTP( "smtp.gmail.com", 587 )
        server.starttls()
        server.login( self.sender, self.password ) #login
        server.sendmail( self.sender, self.target, self.message )

    def getSender(self):
        return self.sender
