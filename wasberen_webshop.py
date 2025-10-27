
print("Hallo, welkom bij De Wasberenwinkel")
print("")

wasbeer1 = "Baby wasbeer"
wasbeer2 = "Rare wasbeer"
wasbeer3 = "Oude wasbeer"
wasbeer4 = "Vieze wasbeer"
wasbeer5 = "Wasbeer met zonnebril"
wasbeer6 = "Dansende wasbeer"

prijs1 = 25.99
prijs2 = 49.99
prijs3 = 15.99
prijs4 = 10.99
prijs5 = 39.99
prijs6 = 44.99

winkelwagen_wasbeer = []
winkelwagen_prijs = []

doorgaan = "ja"

while doorgaan == "ja":
    print("")
    print("--- MENU ---")
    print("1. Bekijk ons aanbod")
    print("2. Koop een wasbeer")
    print("3. Bekijk winkelwagen")
    print("4. Verwijder uit winkelwagen")
    print("5. Afreken en stop")
    print("")
    
    keuze = input("Maak een keuze (1-5): ")
    
    if keuze == "1":
        print("")
        print("ONZE WASBEREN")
        print("1. " + wasbeer1 + " - €" + str(prijs1))
        print("2. " + wasbeer2 + " - €" + str(prijs2))
        print("3. " + wasbeer3 + " - €" + str(prijs3))
        print("4. " + wasbeer4 + " - €" + str(prijs4))
        print("5. " + wasbeer5 + " - €" + str(prijs5))
        print("6. " + wasbeer6 + " - €" + str(prijs6))
    
    elif keuze == "2":
        print("")
        print("KOOP EEN WASBEER")
        print("1. " + wasbeer1 + " - €" + str(prijs1))
        print("2. " + wasbeer2 + " - €" + str(prijs2))
        print("3. " + wasbeer3 + " - €" + str(prijs3))
        print("4. " + wasbeer4 + " - €" + str(prijs4))
        print("5. " + wasbeer5 + " - €" + str(prijs5))
        print("6. " + wasbeer6 + " - €" + str(prijs6))
        print("")
        
        nummer = input("Kies een nummer (1-6): ")
        
        if nummer == "1":
            winkelwagen_wasbeer.append(wasbeer1)
            winkelwagen_prijs.append(prijs1)
            print(wasbeer1 + " is toegevoegd aan je winkelwagen!")
        elif nummer == "2":
            winkelwagen_wasbeer.append(wasbeer2)
            winkelwagen_prijs.append(prijs2)
            print(wasbeer2 + " is toegevoegd aan je winkelwagen!")
        elif nummer == "3":
            winkelwagen_wasbeer.append(wasbeer3)
            winkelwagen_prijs.append(prijs3)
            print(wasbeer3 + " is toegevoegd aan je winkelwagen!")
        elif nummer == "4":
            winkelwagen_wasbeer.append(wasbeer4)
            winkelwagen_prijs.append(prijs4)
            print(wasbeer4 + " is toegevoegd aan je winkelwagen!")
        elif nummer == "5":
            winkelwagen_wasbeer.append(wasbeer5)
            winkelwagen_prijs.append(prijs5)
            print(wasbeer5 + " is toegevoegd aan je winkelwagen!")
        elif nummer == "6":
            winkelwagen_wasbeer.append(wasbeer6)
            winkelwagen_prijs.append(prijs6)
            print(wasbeer6 + " is toegevoegd aan je winkelwagen!")
        else:
            print("Ongeldig nummer!")
    
    elif keuze == "3":
        print("")
        print("JOUW WINKELWAGEN")
        aantal_items = len(winkelwagen_wasbeer)
        
        if aantal_items == 0:
            print("Je winkelwagen is leeg.")
        else:
            totaal = 0
            i = 0
            while i < aantal_items:
                print(str(i + 1) + ". " + winkelwagen_wasbeer[i] + " - €" + str(winkelwagen_prijs[i]))
                totaal = totaal + winkelwagen_prijs[i]
                i = i + 1
            print("")
            print("Subtotaal: €" + str(totaal))
    
    elif keuze == "4":
        print("")
        print("VERWIJDER UIT WINKELWAGEN")
        aantal_items = len(winkelwagen_wasbeer)
        
        if aantal_items == 0:
            print("Je winkelwagen is leeg.")
        else:
            i = 0
            while i < aantal_items:
                print(str(i + 1) + ". " + winkelwagen_wasbeer[i])
                i = i + 1
            print("")
            
            nummer = input("Welk item wil je verwijderen? (nummer): ")
            nummer_int = int(nummer)
            
            if nummer_int >= 1 and nummer_int <= aantal_items:
                verwijderde_wasbeer = winkelwagen_wasbeer.pop(nummer_int - 1)
                winkelwagen_prijs.pop(nummer_int - 1)
                print(verwijderde_wasbeer + " is verwijderd uit je winkelwagen.")
            else:
                print("Ongeldig nummer!")
    
    elif keuze == "5":
        print("")
        print("AFREKENEN")
        
        aantal_items = len(winkelwagen_wasbeer)
        
        if aantal_items == 0:
            print("Je winkelwagen is leeg. Tot ziens!")
        else:
            print("")
            print("JOUW BESTELLING")
            totaal = 0
            i = 0
            while i < aantal_items:
                print("• " + winkelwagen_wasbeer[i] + " - €" + str(winkelwagen_prijs[i]))
                totaal = totaal + winkelwagen_prijs[i]
                i = i + 1
            
            print("")
            print("--- TOTAAL: €" + str(totaal) + " ---")
            print("")
            print("Je hebt " + str(aantal_items) + " wasberen gekocht!")
            print("")
            print("Bedankt voor je bestelling bij De Wasberenwinkel!")
        
        doorgaan = "nee"
    
    else:
        print("Ongeldige keuze. Kies tussen 1 en 5.")

