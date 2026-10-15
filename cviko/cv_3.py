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
        vysledek.append((i + start, iterable[i]))
        i += 1
    return vysledek

def my_zip (*iterables):
    for i in range(len(iterables[0]) and len(iterables[1]) and len(iterables[2])):
       if i > len(iterables[0]) or i > len(iterables[1]) or i > len(iterables[2]):
           break
       else:
        print(f'jmena: {iterables[0][i]}, vek: {iterables[1][i]}, bydliste: {iterables[2][i]}')

def my_zipe (*iterables):
    vysledek = []
    lenght = len(iterables[0])
    i = 0
    while i < lenght:
        value = []
        for iterable in iterables:
            value.append(iterable[i])
        vysledek.append(tuple(value))
        i += 1

    return vysledek

if __name__ == "__main__":
    #my_range(1,10,2)
    #print(my_enum_for(["aaa","bbb","ccc"],100))
    #print(my_enum_while(["aaa","bbb","ccc"],100))
    

    jmena=["Karel","Eva","Adam"]
    vek=[30,25,26]
    bydliste=["Praha","Brno","Ostrava"]

    my_zip(vek,jmena,bydliste)

    my_zipe(vek,jmena,bydliste)