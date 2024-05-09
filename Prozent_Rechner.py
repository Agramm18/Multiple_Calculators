


def Prozent():

        Wert = input("Suchen sie den Prozentwert oder Prozentsatz: ")

        if Wert == "Prozentwert":
            PW = float(input("Was ist Ihr Grundwert also was entspricht 100%: "))
            Ergebnis_PW = 100 / PW
            print(f"1% Entspricht {Ergebnis_PW}")

            Anzahl_Prozent = float(input("Wie hoch sind Ihre Prozent: "))

            Ergebnis_Gesamt_PW = Anzahl_Prozent * Ergebnis_PW
            print(f"Ihr Prozentewrt Entspricht: {Ergebnis_Gesamt_PW}")

        elif Wert == "Prozentsatz":
            PW = float(input("Wie hoch sind die Prozent: "))
            Ergebnis_PW = 100 * PW
            Grundwert = float(input("Wie hoch ist Ihr Grundwert: "))
            Ergebnis_G = Grundwert / Ergebnis_PW
            print(f"Ihr Prozentsatz ist: {Ergebnis_G}")

Prozent()
