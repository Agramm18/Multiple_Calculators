

def Umrechner():
    def von_in():
        Länge_Aktuell = input("Geben sie bitte die Aktuelle länge an mm/cm/dm/m: ")
        Länge_Neu = input("Geben sie bitte die Länge an die Neu ist also von mm in m z.B: ")

        Maße_Länge = float(input("Geben sie die Aktuelle Maße an: "))

        if Länge_Aktuell == "" and Länge_Neu == "":
            print("Eingabe ungültig bitte geben sie eine gültige Maße an mm/cm/dm/m")

        elif Länge_Aktuell == "mm" and Länge_Neu == "cm":
                Umrechnung = Maße_Länge / 10
                print(f"Ihre neue Maße beträgt nun {Umrechnung} cm")

        elif Länge_Aktuell == "mm" and Länge_Neu == "dm":

                Umrechnung = Maße_Länge / 100
                print(f"Ihre neue Maße beträgt nun {Umrechnung} dm")

        elif Länge_Aktuell == "mm" and Länge_Neu == "m":

                Umrechnung = Maße_Länge / 100
                print(f"Ihre Neue Maße beträgt nun {Umrechnung} m")

        elif Länge_Aktuell == "cm" and Länge_Neu == "mm":

                Umrechnung = Maße_Länge * 100
                print(f"Ihre neue Maße beträgt: {Umrechnung} mm")

        elif Länge_Aktuell == "cm" and Länge_Neu == "dm":

                Umrechnung = Maße_Länge / 10
                print(f"Ihre neue Maße beträg nun: {Umrechnung} dm")

        elif Länge_Aktuell == "cm" and Länge_Neu == "m":

                Umrechnung = Maße_Länge / 100
                print(f"Ihre neue Maße ist nun: {Umrechnung} m")

        elif Länge_Aktuell == "dm" and Länge_Neu == "mm":

                Umrechnung = Maße_Länge * 100
                print(f"Ihre neue Maße beträgt nun: {Umrechnung} mm")

        elif Länge_Aktuell == "dm" and Länge_Neu == "cm":

                Umrechnung = Maße_Länge * 10
                print(f"Ihre neue Maße ist nun: {Umrechnung} cm")

        elif Länge_Aktuell == "dm" and Länge_Neu == "m":

                Umrechnung = Maße_Länge / 10
                print(f"Ihre neue Maße ist nun: {Umrechnung} m")

        elif Länge_Aktuell == "m" and Länge_Neu == "mm":

                Umrechnung = Maße_Länge * 100
                print(f"Ihre neue Maße ist nun: {Umrechnung} mm")

        elif Länge_Aktuell == "m" and Länge_Neu == "cm":

                Umrechnung = Maße_Länge / 100
                print(f"Ihre neue Maße ist nun: {Umrechnung} cm")

        elif Länge_Aktuell == "m" and Länge_Neu == "dm":

                Umrechnung = Maße_Länge / 10
                print(f"Ihre Neue Maße ist nun: {Umrechnung} dm")

    von_in()
Umrechner()