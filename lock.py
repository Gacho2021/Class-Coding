class lock():
    def __init__(self, locked, locationid, securitylevel):
      self.locked=lockid
      self.locationid=locactionid
      self.securitylevel =securitylevel
      self.status='locked'


    def getLocked(self):
        return self.lockid

    def getLocationid(self):
        return self.getLocationid

    def getSecurityLevel(self):
        return self.securitylevel

    def getStatus(self):
        return self.status

    def setStatus(self, status):
        self.status=status

    def __str__(self):
        return self.lockid + ' ' + self.status
