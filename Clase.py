a = 24
b = 66
def MCD (a,b):
    print(f" a={a} - b= {b}")
    res = a
    while (b != 0):
        res = MCD(b, a % b)
        a = b
        b = a%b
    return res

c = MCD (a, b)
print ("El MCD de", a, "y", b, "es:", c)