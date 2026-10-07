def vstup():
    a = int(input("Zadejte první číslo: "))
    b = int(input("Zadejte druhé číslo: "))

    return a, b


def menu():
    
            print("calculator menu")
            print("1. + ")
            print("2. - ")
            print("3. * ")
            print("4. / ")
            print("5.  Vyměnit čísla ")
            print("6. exit")
            ch = int(input("Enter your choice: "))
            return ch

def kolo(a, b, ch):
    if ch == 1:
        print(a + b)
    elif ch == 2:
        print(a - b)
    elif ch == 3:
        print(a * b)
    elif ch == 4:
        print(a / b)
    elif ch == 5:
        a, b = vstup()
    elif ch == 6:
        return a, b, True
    else:
        print("invalid input was registered")

    return a, b, False

if __name__ == "__main__":
    a, b = vstup()

    while True:
        ch = menu()
        a, b, exit_program = kolo(a, b, ch)
        if exit_program:
            break
    