
print("Welkom bij Het Vage Hotel")
print("")

gebouw1 = [
    ["vrij", "vrij", "vrij"],
    ["vrij", "vrij", "vrij"],
    ["vrij", "vrij", "vrij"]
]

gebouw2 = [
    ["vrij", "vrij", "vrij"],
    ["vrij", "vrij", "vrij"],
    ["vrij", "vrij", "vrij"]
]

print("Hotel aangemaakt met 2 gebouwen, 3 verdiepingen en 3 kamers per verdieping.")
print("Status: vrij of bezet")
print("")

doorgaan = "ja"

while doorgaan == "ja":
    print("")
    print("MENU")
    print("1. Laat iemand inchecken")
    print("2. Bekijk overzicht van alle kamers")
    print("3. Laat iemand uitchecken")
    print("4. Stop programma")
    print("")
    
    keuze = input("Maak een keuze (1-4): ")
    
    if keuze == "1":
        print("")
        print("INCHECKEN")
        print("")
        gebouw_nummer = input("Welk gebouw? (1 of 2): ")
        verdieping_nummer = input("Welke verdieping? (1, 2 of 3): ")
        kamer_nummer = input("Welke kamer? (1, 2 of 3): ")
        
        verdieping_index = int(verdieping_nummer) - 1
        kamer_index = int(kamer_nummer) - 1
        
        if gebouw_nummer == "1":
            if gebouw1[verdieping_index][kamer_index] == "bezet":
                print("Deze kamer is al bezet!")
            else:
                gebouw1[verdieping_index][kamer_index] = "bezet"
                print("Inchecken geslaagd!")
        elif gebouw_nummer == "2":
            if gebouw2[verdieping_index][kamer_index] == "bezet":
                print("Deze kamer is al bezet!")
            else:
                gebouw2[verdieping_index][kamer_index] = "bezet"
                print("Inchecken geslaagd!")
        else:
            print("Ongeldige keuze!")
    
    elif keuze == "2":
        print("")
        print("OVERZICHT VAN ALLE KAMERS")
        print("")
        
        print("GEBOUW 1")
        print("")
        for v in range(3):
            print("  Verdieping " + str(v + 1) + ":")
            for k in range(3):
                print("    Kamer " + str(k + 1) + ": " + gebouw1[v][k])
            print("")
        
        print("GEBOUW 2")
        print("")
        for v in range(3):
            print("  Verdieping " + str(v + 1) + ":")
            for k in range(3):
                print("    Kamer " + str(k + 1) + ": " + gebouw2[v][k])
            print("")
    
    elif keuze == "3":
        print("")
        print("UITCHECKEN")
        print("")
        gebouw_nummer = input("Welk gebouw? (1 of 2): ")
        verdieping_nummer = input("Welke verdieping? (1, 2 of 3): ")
        kamer_nummer = input("Welke kamer? (1, 2 of 3): ")
        
        verdieping_index = int(verdieping_nummer) - 1
        kamer_index = int(kamer_nummer) - 1
        
        if gebouw_nummer == "1":
            if gebouw1[verdieping_index][kamer_index] == "vrij":
                print("Deze kamer is al leeg!")
            else:
                gebouw1[verdieping_index][kamer_index] = "vrij"
                print("Uitchecken geslaagd!")
        elif gebouw_nummer == "2":
            if gebouw2[verdieping_index][kamer_index] == "vrij":
                print("Deze kamer is al leeg!")
            else:
                gebouw2[verdieping_index][kamer_index] = "vrij"
                print("Uitchecken geslaagd!")
        else:
            print("Ongeldige keuze!")
    
    elif keuze == "4":
        print("")
        print("Bedankt voor je bezoek aan Het Vage Hotel!")
        print("Tot ziens!")
        doorgaan = "nee"
    
    else:
        print("Ongeldige keuze. Kies tussen 1 en 4.")

