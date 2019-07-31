class config:
    def __init__(self):
        self.host="localhost"
        self.port=10000

    def setHost(self, newHost):
        self.host=newHost
    
    def setPort(self, newPort):
        self.port=newPort
    
    def getHost(self):
        return self.host
    
    def getPort(self):
        return str(self.port)
    
    def getConfig(self):
        return (self.host, self.port)
