def je_tah_mozny(figurka, cilova_pozice, obsazene_pozice):
    """
    Ověří, zda se král nebo jezdec může přesunout na danou pozici.
    
    :param figurka: Slovník s klíči 'typ' a 'pozice' (např. {"typ": "král", "pozice": (4, 4)})
    :param cilova_pozice: N-tice (řádek, sloupec)
    :param obsazene_pozice: Množina obsazených pozic
    :return: True, pokud je tah možný, jinak False
    """
    aktualni_pozice = figurka["pozice"]
    typ = figurka["typ"]
    
    radek, sloupec = cilova_pozice
    
    if radek < 1 or radek > 8 or sloupec < 1 or sloupec > 8: # je mimo šachovnici?
        return False
    
    if cilova_pozice in obsazene_pozice:# je obsazená?
        return False
    
    rozdil_radku = abs(radek - aktualni_pozice[0])
    rozdil_sloupcu = abs(sloupec - aktualni_pozice[1])
    
    if typ == "král":
        return rozdil_radku <= 1 and rozdil_sloupcu <= 1 and (rozdil_radku + rozdil_sloupcu) > 0 # je to o 1 pole v libovolném směru
        
    elif typ == "jezdec": # je to tvar L: 2 pole v jednom směru a 1 v druhém směru
        return (rozdil_radku == 2 and rozdil_sloupcu == 1) or \
               (rozdil_radku == 1 and rozdil_sloupcu == 2)
        
    return False


if __name__ == "__main__":
    kral = {"typ": "král", "pozice": (4, 4)}
    jezdec = {"typ": "jezdec", "pozice": (3, 3)}
    obsazene_pozice = {(4, 4), (5, 5), (3, 5)}

    # Testy pro krále
    print(je_tah_mozny(kral, (5, 5), obsazene_pozice))  # False (obsazeno) 
    print(je_tah_mozny(kral, (5, 4), obsazene_pozice))  # True (o 1 pole dolů)
    print(je_tah_mozny(kral, (6, 6), obsazene_pozice))  # False (příliš daleko - o 2 pole)
    print(je_tah_mozny(kral, (0, 4), obsazene_pozice))  # False (mimo šachovnici)

    # Testy pro jezdce
    print(je_tah_mozny(jezdec, (5, 4), obsazene_pozice))  # True (tvar L: 2 dolů, 1 doprava)
    print(je_tah_mozny(jezdec, (5, 5), obsazene_pozice))  # False (obsazeno)
    print(je_tah_mozny(jezdec, (4, 6), obsazene_pozice))  # False (rozdíl 1 a 3, není tvar L)
    print(je_tah_mozny(jezdec, (4, 5), obsazene_pozice))  # True (tvar L: 1 dolů, 2 doprava)
    print(je_tah_mozny(jezdec, (10, 3), obsazene_pozice)) # False (mimo šachovnici)