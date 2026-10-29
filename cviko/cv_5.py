






if __name__ == "__main__":
    with open("kitten.jpeg", "rb") as soubor: #Otevření v binárním režimu
        prvni_dva_bajty = soubor.read(2) # Načtení prvních dvou bajtů
        if prvni_dva_bajty == b'\xff\xd8': # Kontrola SOI markeru
            print("Soubor je typu JPEG.")
        else:
            print("Soubor není typu JPEG.")

