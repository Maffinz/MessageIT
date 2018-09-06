import re
import socket
import dns.resolver
import smtplib
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
    def isEmpty(self, mail, password, target, targetCarrier, message, networkSSID):
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
        if networkSSID == "":
            error += "Empty parameters for : 'NetworkSSID' \n"

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

    def EmailVerification(self, email):
        addressToVerify = email
        match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', addressToVerify)

        if match == None:
        	return False

        #Second part
        records = dns.resolver.query('gmail.com', 'MX')
        mxRecord = records[0].exchange
        mxRecord = str(mxRecord)

        # Get local server hostname
        host = socket.gethostname()

        # SMTP lib setup (use debug level for full output)
        server = smtplib.SMTP()
        server.set_debuglevel(0)

        # SMTP Conversation
        server.connect(mxRecord)
        server.helo(host)
        server.mail('me@domain.com')
        code, message = server.rcpt(str(addressToVerify))
        server.quit()

        # Assume 250 as Success
        if code == 250:
        	return True
        else:
        	return False
    def PhoneNumberValidation(self, phoneNumber):
        #Check that there is 10 Numbers
        validateTarget = phoneNumber.replace(" ", "")
        if len(validateTarget) == 10:
            if validateTarget.isdigit():
                return True
        return False
