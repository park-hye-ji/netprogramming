a = int(input("insert num1: "))
b = int(input("insert num2: "))

def gcd(a,b):
    if a>b:
        while(b!=0):
            a,b=b,a%b
        return a
    elif a<b:
        while(a!=0):
            b,a=a,b%a
        return b
    
print(gcd(a,b))







        