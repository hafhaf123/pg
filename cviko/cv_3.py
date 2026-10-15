def my_range (start,stop,step=+1):
    
    x = start
    vysledek = []
    while (x < stop if step > 0 else x > stop):
        vysledek.append(x)    
        x += step
        
    return vysledek

def my_enum_for (iterable, start=0):
    vysledek = []

    for i in range(0,len(iterable)):
        vysledek.append((i + start , iterable[i]))
        
    return vysledek

def my_enum_while (iterable, start=0):
    vysledek = []
    i = 0
    while i < len(iterable):
        vysledek.append(i + start , iterable[i])
        i += 1
    return vysledek


if __name__ == "__main__":
    #my_range(1,10,2)
    #print(my_enum_for(["aaa","bbb","ccc"],100))
    print(my_enum_while(["aaa","bbb","ccc"],100))