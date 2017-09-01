#! /usr/bin/python34

class mainClass():
    def method1(self):
        print ("mainClass method1")
    
    def method2(self, someString):
        print("mainClass method2: " + someString)
    
class drivedClass(mainClass):
    def method2(self):
        print ("Class method2")
    
    def method1(self):
        mainClass.method1(self);
        print ("anotherClass method1")
      
def main():
    c = mainClass()
    c.method1()
    c.method2("This is a string")
    c2 = drivedClass()
    c2.method1()
  
if __name__ == "__main__":   main()
