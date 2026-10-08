def vxp(seznam,x,nasobek):
    if x > len(seznam):
        print(f"Seznam má jenom {len(seznam)} prvků.")
        return seznam
    
    x -= 1
    
    if x < 0:
        print(f"Seznam má jenom {len(seznam)} prvků.")
        return seznam
    
    seznam[x] *= nasobek
    return seznam

def prumer(seznam):
    if len(seznam) <= 0:
        print("Seznam je prázdný.")
        return 0
    
    vysledek = sum(seznam) / len(seznam)
    print(f"Průměr seznamu je {vysledek}.")
    return vysledek
    
if __name__ == "__main__":
   

    seznam = vxp([1,2,3,4,5], 3, 10)
    print(seznam) # [1, 2, 30, 4, 5]

    vysledek = sum(seznam)
    print(f"Součet seznamu je {vysledek}.")
    prumer(seznam)




    #vek = int(input("Zadej svůj věk: "))
    #vek=1

    #print(f"Za rok ti bude {vek+1} let.")

    #if vek >=21:
        #print("Meš pít v USA.")
    #else:
        #print("Dej si colu.")
    
    #seznam =[1,2,3,"ctyri",5]
    #print(seznam)
    #seznam.append("šest")
    #print(seznam[2])

    #print(f"Seznam ma {len(seznam)} prvků.")
    