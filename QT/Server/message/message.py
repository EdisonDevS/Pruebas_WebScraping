class message:
    def __init__(self,newPackagedMessage):
        self.packagedMessage=newPackagedMessage
        partitions=self.packagedMessage.split('€')
        self.contact=partitions[0]
        self.message=partitions[1]

    def getContact(self):
        return self.contact
    
    def getMessage(self):
        return self.message
    
    def getPackagedMessage(self):
        return self.packagedMessage