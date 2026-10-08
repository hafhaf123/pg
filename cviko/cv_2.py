def vxp(seznam,x,nasobek):
    if x > len(seznam):
        print(f"Seznam má {len(seznam)} prvků.")
    else:
        seznam[x-1] = seznam[x-1] * nasobek
    return seznam
    
if __name__ == "__main__":
   

    seznam = vxp([1,2,3,4,5], 3, 10)
    print(seznam) # [1, 2, 30, 4, 5]






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
    