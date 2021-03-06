import smtplib
from enum import Enum
import os

carrier = {
        "Verizon" : "@vtext.com",
        "ATT": "@txt.att.net",
        "Cricket": "@mms.cricketwireless.net",
        "MetroPCS" : "@mymetropcs.com",
        "Sprint" : "@messaging.sprintpcs.com",
        "T-Mobile": "@tmomail.net",
        }

class User:
    networkInfo = dict()
    class Data(Enum):
        sender = 0
        password = 1
        target = 2
        message = 3
        network = 4

    def __init__(self, **kwarg):
        if kwarg:
            targetFullNumber = kwarg["target"].replace(" ", "") + carrier[kwarg["target_carrier"].replace(" ", "")]
            senderMail = kwarg["sender"].replace(" ", "")
            self.sender = senderMail
            self.target = targetFullNumber
            self.message = kwarg["message"]
            self.password = kwarg["password"]
            self.networkSSID = kwarg["network"]
        else:
            self.sender = ""
            self.target = ""
            self.message = ""
            self.password = ""
            self.networkSSID = ""

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
        #Reset Info Label
        self.info.label = ""
        #Save User Info
        myFile = open("dat.inf", "w+")
        myFile.write(self.sender + '\n' + self.password + '\n' + self.target + '\n' + self.message + '\n' + self.networkSSID + '\n')
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
            self.networkSSID = content[self.Data.network.value]
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

    def checkNetwork(self): # ghttunbmqppmhqnf
        os.system("/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport -I > network.inf")
        with open("network.inf") as netWorkFile:
            netowkrInfo = dict(line.strip().split(":", 1) for line in netWorkFile)
            return str(netowkrInfo["SSID"].strip())
        return "NA"

    def checkSetNetwork(self, setNetwork):
        if setNetwork == self.checkNetwork():
            return True
        return False

    #Functional Functions
    def getSender(self):
        return self.sender
    def getSSID(self):
        return self.networkSSID
