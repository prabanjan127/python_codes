class string:
    def __init__(self):
        self.upper=0
        self.lower=0
        self.vowels=0
        self.consonent=0
        self.space=0
        self.str=""
    def getstr(self):
        self.str = input("enter the string: ")
    def check(self):
        for i in self.str:
            if(i.isupper()):
                self.upper+=1
            if(i.islower()):
                self.lower+=1
            if(i in ('A','E','I','O','U','a','e','i','o','u')):
                self.vowels+=1
            else:
                self.consonent+=1
            if(i.isspace()):
               self.space+=1
    def display(self):
        print(self.str)
        print("upper ",self.upper)
        print("lower ",self.lower)
        print("lower ",self.vowels)
        print("consonent ",self.consonent)
        print("space",self.space)
s = string()
s.getstr()
s.check()
s.display()
