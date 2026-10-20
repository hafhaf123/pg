
def je_prvocislo(cislo):

    if cislo < 2:
        return False

    i = 2

    while i * i <= cislo:
        if cislo % i == 0:
            return False

        i = i + 1

    return True


def vrat_prvocisla(maximum):

    prvocisla = []

    for cislo in range(1, maximum + 1):
        if je_prvocislo(cislo):
            prvocisla.append(cislo)

    return prvocisla


if __name__ == "__main__":
    cislo = int(input("Zadej maximum: "))
    prvocisla = vrat_prvocisla(cislo)
    print(prvocisla)
