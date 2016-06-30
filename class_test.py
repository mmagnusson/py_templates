import os

class Domain:
    def __init__(self, domain, port, protocol):
# stores the variables passed inside two(two?  isnt it 3?) variables
        self.domain=domain
        self.port=port
        self.protocol=protocol
# Defines a method to build a URL
    def URL(self):
        if self.protocol == 'https':
            URL = 'https://'+self.domain+':'+self.port+'/'
        if self.protocol == 'http':
            URL = 'http://'+self.domain+':'+self.port+'/'
        return URL
# setup method to lookup resolve domain to IP using host command via os.system
    def lookup(self):
        os.system("host "+self.domain)
