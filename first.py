def sude_nebo_liche(cislo):
   def even(a,b):
    x = a % b
    
    if x == 0 :
        return f"Cislo {a} je dělitelné beze zbytku"
    else:
        return f"Cislo {a} není dělitelné beze zbytku"

    print(f"Cislo {cislo} je sude")


if __name__ == "__main__":
    sude_nebo_liche(5)
    sude_nebo_liche(1000000)
