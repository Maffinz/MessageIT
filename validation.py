carrier = {
        "Verizon" : "@vtext.com",
        "ATT": "@txt.att.net",
        "Cricket": "@mms.cricketwireless.net",
        "MetroPCS" : "@mymetropcs.com",
        "Sprint" : "@messaging.sprintpcs.com",
        "T-Mobile": "@tmomail.net",
        }
class Validation:
    def __init__(self):
        self.values = []
    #Checks if Text are not empty
    def isEmpty(self, mail, password, target, targetCarrier, message):
        error = ""
        if mail == "":
            error += "Empty parameters for : 'Gmail' \n"
        if password == "":
            error += "Empty parameters for : 'password' \n"
        if target == "":
            error += "Empty parameters for : 'target' \n"
        if targetCarrier == "":
            error += "Empty parameters for : 'targetCarrier' \n"
        if message == "":
            error += "Empty parameters for : 'Message' \n"

        if error != "":
            self.values.append(True)
            self.values.append(error)
        else:
            self.values.append(False)
            self.values.append("")
        return self.values

    def carrierExist(self, targetCarrier):
        if targetCarrier in carrier:
            return True
        else:
            return False
