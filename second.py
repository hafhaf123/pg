def cislo_text(cislo):
    if cislo < 0 or cislo > 100:
        return "Číslo musí být mezi 0 a 100"
    
    jednotky = {
        0: "nula",1: "jedna", 2: "dva", 3: "tři", 4: "čtyři", 5: "pět",
        6: "šest", 7: "sedm", 8: "osm", 9: "devět"
    }
    nactiny = {
        10:"deset",11: "jedenáct", 12: "dvanáct", 13: "třináct", 14: "čtrnáct", 15: "patnáct",
        16: "šestnáct", 17: "sedmnáct", 18: "osmnáct", 19: "devatenáct", 20: "dvacet"
    }
    desitky = {  30: "třicet", 40: "čtyřicet", 50: "padesát",
                60: "šedesát", 70: "sedmdesát", 80: "osmdesát", 90: "devadesát",100: "sto"
               }
    if cislo == 100:
        return desitky[100]
    elif cislo == 0:
        return jednotky[0]
    elif cislo < 10:
        return jednotky[cislo]
    elif 10 <= cislo <= 20:
        return nactiny[cislo]
    else:
        desitka = (cislo // 10) * 10 # vydelení čísla 10 a zaokrouhlení dolů na celé číslo, pak vynásobení 10
        jednotka = cislo % 10 # zbytek po dělení čísla 10
        if jednotky == 0:
            return desitka[desitky]
        else:
            return f"{desitky[desitka]} {jednotky[jednotka]}"

if __name__ == "__main__":
    print("Program převádí čísla na text (0-100).")
    cislo = float(input("Zadej číslo: "))
    text = cislo_text(cislo)
    print(text)