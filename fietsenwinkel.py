
print("==================================================")
print("Welkom bij fietsenwinkel Trappers")
print("==================================================")
print("")

wielen_voorraad = 10
stuur_voorraad = 15
mountainbike_voorraad = 5
fietsbel_voorraad = 20

doorgaan = "ja"

while doorgaan == "ja":
    print("")
    print("MENU")
    print("1. Bekijk aanbod")
    print("2. Koop een artikel")
    print("3. Bekijk huidige voorraad")
    print("4. Stop het programma")
    print("")
    
    keuze = input("Maak een keuze (1-4): ")
    
    if keuze == "1":
        print("")
        print("ONS AANBOD")
        print("• Wielen: " + str(wielen_voorraad) + " stuks op voorraad")
        print("• Stuur: " + str(stuur_voorraad) + " stuks op voorraad")
        print("• Mountainbike: " + str(mountainbike_voorraad) + " stuks op voorraad")
        print("• Fietsbel: " + str(fietsbel_voorraad) + " stuks op voorraad")
    
    elif keuze == "2":
        print("")
        print("KOOP EEN ARTIKEL")
        print("1. Wielen")
        print("2. Stuur")
        print("3. Mountainbike")
        print("4. Fietsbel")
        print("")
        
        artikel = input("Welk artikel wil je kopen? (1-4): ")
        
        if artikel == "1":
            if wielen_voorraad > 0:
                aantal = int(input("Hoeveel Wielen wil je kopen? "))
                if aantal <= wielen_voorraad:
                    wielen_voorraad = wielen_voorraad - aantal
                    print("Je hebt " + str(aantal) + " Wielen gekocht!")
                    print("Er zijn nog " + str(wielen_voorraad) + " stuks op voorraad.")
                else:
                    print("Sorry, we hebben maar " + str(wielen_voorraad) + " stuks op voorraad.")
            else:
                print("Sorry, Wielen is niet op voorraad!")
        
        elif artikel == "2":
            if stuur_voorraad > 0:
                aantal = int(input("Hoeveel Stuur wil je kopen? "))
                if aantal <= stuur_voorraad:
                    stuur_voorraad = stuur_voorraad - aantal
                    print("Je hebt " + str(aantal) + " Stuur gekocht!")
                    print("Er zijn nog " + str(stuur_voorraad) + " stuks op voorraad.")
                else:
                    print("Sorry, we hebben maar " + str(stuur_voorraad) + " stuks op voorraad.")
            else:
                print("Sorry, Stuur is niet op voorraad!")
        
        elif artikel == "3":
            if mountainbike_voorraad > 0:
                aantal = int(input("Hoeveel Mountainbike wil je kopen? "))
                if aantal <= mountainbike_voorraad:
                    mountainbike_voorraad = mountainbike_voorraad - aantal
                    print("Je hebt " + str(aantal) + " Mountainbike gekocht!")
                    print("Er zijn nog " + str(mountainbike_voorraad) + " stuks op voorraad.")
                else:
                    print("Sorry, we hebben maar " + str(mountainbike_voorraad) + " stuks op voorraad.")
            else:
                print("Sorry, Mountainbike is niet op voorraad!")
        
        elif artikel == "4":
            if fietsbel_voorraad > 0:
                aantal = int(input("Hoeveel Fietsbel wil je kopen? "))
                if aantal <= fietsbel_voorraad:
                    fietsbel_voorraad = fietsbel_voorraad - aantal
                    print("Je hebt " + str(aantal) + " Fietsbel gekocht!")
                    print("Er zijn nog " + str(fietsbel_voorraad) + " stuks op voorraad.")
                else:
                    print("Sorry, we hebben maar " + str(fietsbel_voorraad) + " stuks op voorraad.")
            else:
                print("Sorry, Fietsbel is niet op voorraad!")
        
        else:
            print("Ongeldige keuze!")
    
    elif keuze == "3":
        print("")
        print("HUIDIGE VOORRAAD")
        print("Wielen: " + str(wielen_voorraad) + " stuks")
        print("Stuur: " + str(stuur_voorraad) + " stuks")
        print("Mountainbike: " + str(mountainbike_voorraad) + " stuks")
        print("Fietsbel: " + str(fietsbel_voorraad) + " stuks")
    
    elif keuze == "4":
        print("")
        print("Bedankt voor je bezoek aan de Trappers")
        print("Tot ziens!")
        doorgaan = "nee"
    
    else:
        print("Ongeldige keuze. Kies 1, 2, 3 of 4.")
