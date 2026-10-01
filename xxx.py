def add(a,b):
    c = a + b
    return c

def mul(a,b,c):
    x = a * b * c
    return x

def dif(a,b):
    if b == 0 :
        return 0
    else:
        x = a / b
        return x 

def even(a,b):
    x = a % b
    
    if x == 0 :
        return f"Cislo {a} je dělitelné beze zbytku"
    else:
        return f"Cislo {a} není dělitelné beze zbytku"

def jd3(a):
    return even(a, 3)
    


if __name__ == "__main__":
    #x = add(10, 20)
    #x = mul(10, 20, 30)
    #x = dif(10, 0)

    vysledek = jd3(10)
    print(vysledek)


