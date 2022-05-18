from item import Item

class __Inventory():
    def _init__(self):
        self.items=[]

    def addItem(self, i):
        self.items.append(i)

    def getItems(self):
        return self.items

    def getItemByNumber(self, number):
        reqItem=None
        for i in self.items:
            if i.itemnum==number:
                reqItem=i
                break
            return reqItem
