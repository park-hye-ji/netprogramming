import math

def cir_area(r):
    area=math.pi * r * r
    return area

def cir_circum(r):
    circum=2 * math.pi * r
    return circum


a=cir_area(3.5)
b=cir_circum(3.5)
print("%2.2f"%(a))
print("%2.2f"%(b))

