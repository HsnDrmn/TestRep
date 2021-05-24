class Calculator :
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def add (self):
        return self.a + self.b
    def mul (self):
        return self.a * self.b
    def div (self):
        return self.a / self.b
    def sub (self):
        return self.a - self.b

if  __name__ == '__main__' :
    a = int(input("birinci sayıyı gir"))
    b = int(input("ikinci sayıyı gir"))
    obj = Calculator(a,b)
    choice = 1
    while choice != 0:
        print("1. topla")
        print("2. çıkar")
        print("3. çarp")
        print("4. bol")
        print("0. çıkış")
        choice = int(input("seçimini giriniz: "))

        if choice == 1:
            print ("Result: ",obj.add())
        elif choice == 2:
            print ("Result: ",obj.sub())
        elif choice == 3:
            print ("Result: ",obj.mul())
        elif choice == 4:
            print ("Result: ",round(obj.div()),2)
        elif choice == 0:
            print ("Existing!")
        else:
            print("invalid")
       
