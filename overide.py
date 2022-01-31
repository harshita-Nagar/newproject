class Bank:
    def getroi(self):
        return 7;

class SBI(Bank):
    def getroi(self):
        return 5;

class ICICI(Bank):
    def getroi(self):
        return 8;

class BOI(Bank):
    def getroi(self):
        return 2

b1=Bank()
b2=SBI()
b3=ICICI()
b4=BOI()

print("bank interest rate is :" , b1.getroi());
print("bank interest rate is :" , b2.getroi());
print("bank interest rate is :" , b3.getroi());
print("bank interest rate is :" , b4.getroi());


