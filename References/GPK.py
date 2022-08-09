import requests
import time
import keys

class GPK:
    def __init__(self, interval, medicines):
        self.interval = interval
        self.medicines = medicines

    def sendToDiscord(self):
        message = ""
        for i in self.medicines:
            #["med1", "med2", "med3"...]
            message += self.medicines[i] + ", "

        #send to discord every interval
        while(True):

            #create payload
            payload = {
                'content': message
            }
            #get Authorization
            header = {
                'authorization': keys.auth
            }






