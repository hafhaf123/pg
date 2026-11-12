class Osoba:
    def __init__(self, jmeno, vek):
        self.jmeno = jmeno
        self.vek = vek

    def __str__(self):
        return f'Osoba {self.jmeno} ma {self.vek} let'

    def pridat_rok(self):
        self.vek += 1


class Student(Osoba):
    def __init__(self, jmeno, vek, rocnik):
        super().__init__(jmeno, vek)
        self.rocnik = rocnik

    def __str__(self):
        return f'Student {self.jmeno} ma {self.vek} let a je v {self.rocnik}. rocniku'

    def pridat_rok(self):
        if self.rocnik < 5:
            self.rocnik += 1
            self.vek += 1
        else:
            self.rocnik = 5
            self.vek +=1


class Ucitel(Osoba):
    def __init__(self, jmeno, vek, praxe):
        super().__init__(jmeno, vek)
        self.praxe = praxe

    def __str__(self):
        return f'Učitel {self.jmeno} ma {self.vek} let a má {self.praxe}. let praxe'

    def pridat_praxe(self):
        self.vek += 1
        self.praxe += 1

class Udrzbar(Osoba):
    def __init__(self, jmeno, vek):
        super().__init__(jmeno, vek)
        

    def __str__(self):
        return f'Udržbář {self.jmeno} ma {self.vek} let a je to údržbář'

    def pridat_vek(self):
        self.vek += 1

if __name__ == "__main__":
    osoba = Osoba("Vlada", 44)
    student = Student("Petr", 20, 2)
    ucitel = Ucitel("Jana", 35, 10)
    udrzbar = Udrzbar("Karel", 50)

    print(osoba)
    osoba.pridat_rok()
    print(osoba)
    print(student)
    student.pridat_rok()
    print(student)
    student.pridat_rok()#4
    student.pridat_rok()#5
    student.pridat_rok()#6
    print(student)
    print(ucitel)
    ucitel.pridat_praxe()
    print(ucitel)
    print(udrzbar)