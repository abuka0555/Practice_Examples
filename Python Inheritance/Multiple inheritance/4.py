class Class1:
    def m(self):
        print("In Class1") 
      
class Class2(Class1):
    def m(self):
        print("In Class2")


obj = Class2()
obj.m()