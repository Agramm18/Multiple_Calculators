
Operator = input("Geben sie Plus/Minus/Mal/Geteilt oder Prozent ein: ")

#Zahlen für Operatoren
Zahl_1 = float(input("Geben sie eine Dezimal Zahl ein: "))
Zahl_2 = float(input("Geben sie eine zweite Zahl ein: "))


def Taschenrechner():
    def Plus():
        if Operator == "Plus":
            Ergebnis = Zahl_1 + Zahl_2
            print(f"Ihr Ergebnis ist: {Ergebnis}")

        elif Operator == "":
            print("Eingabe ist Ungültig")
            print("Bitte geben sie Plus/Minus/Mal oder Geteilt ein um fortzufahren")
    Plus()

    def Minus():
        if Operator == "Minus":
            Ergebnis = Zahl_1 - Zahl_2
            print(f"Ihr Ergebnis ist: {Ergebnis}")

        elif Operator == "":
            print("Eingabe ist Ungültig")
            print("Bitte geben sie Plus/Minus/Mal oder Geteilt ein um fortzufahren")
    Minus()

    def Mal():
        if Operator == "Mal":
            Ergebnis = Zahl_1 * Zahl_2
            print(f"Ihr Ergebnis ist: {Ergebnis}")

        elif Operator == "":
            print("Eingabe ist Ungültig")
            print("Bitte geben sie Plus/Minus/Mal oder Geteilt ein um fortzufahren")
    Mal()

    def Geteilt():
        if Operator == "Geteilt":
            Ergebnis = Zahl_1 / Zahl_2
            print(f"Ihr Ergebnis ist: {Ergebnis}")

        elif Operator == "":
            print("Eingabe ist Ungültig")
            print("Bitte geben sie Plus/Minus/Mal oder Geteilt ein um fortzufahren")

    Geteilt()

Taschenrechner()
