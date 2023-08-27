class oddeven:
    def check(num):
        if(num%2==0):
            print("odd")
        else:
            print("even")
n = oddeven()
x=int(input("enter the no: "))
n.check(x)
