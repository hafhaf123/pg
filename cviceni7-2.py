class moje_vyjimka(Exception):
    pass

class banovni_ucet:
    def __init__(self, jmeno, urok):
        self.jmeno = jmeno
        self.urok = urok
        self.zustatek = 0

    def __str__(self):
        return f"Na ucte {self.jmeno} je zustatek {self.zustatek:.2f}"

    def vloz(self, castka):
        if castka < 0:
            raise moje_vyjimka("Nelze vložit zápornou částku.")
        self.zustatek += castka

    def vyber(self, castka):
        if castka < 0:
            raise moje_vyjimka("Nelze vybrat zápornou částku.")
        if castka > self.zustatek:
            raise moje_vyjimka("Nedostatečný zůstatek na účtu.")
        self.zustatek -= castka

    def pricti_uroky(self):
        self.zustatek += self.zustatek * self.urok

if __name__ == "__main__":
    ucet = banovni_ucet("Sporici", 0.05)
    try:
        ucet.vloz(200)
        ucet.vyber(100)
        ucet.pricti_uroky()
        print(ucet)
    except moje_vyjimka as e:
        print(f"Chyba: {e}")
    