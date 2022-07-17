class Atm(object):
    def __init__(self, cardnumber, pinnumber):
        self.cardnumber = cardnumber
        self.pinnumber = pinnumber

    def transaction(self):
        print("transaction completed")
    
    def balance(self, name):
        print("balance credited")

Aaryan=Atm("01490324070140014874", "017")
print(Aaryan.transaction)
Yeezys=Atm("12412491241240", "780")
print(Yeezys.balance)