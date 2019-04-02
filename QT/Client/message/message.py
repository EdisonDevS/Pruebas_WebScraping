class message:
    def __init__(self,contact,message):
        self.actualContact=contact
        self.actualMessage=message
        self.packagedMessage=""

    def getContact(self):
        return self.contact
    
    def getMessage(self):
        return self.message
    
    def updatePackagedMessage(self):
        self.packagedMessage=self.actualContact+'€'+self.actualMessage

    def getPackagedMessage(self):
        self.updatePackagedMessage()
        return self.packagedMessage.encode('utf-8')