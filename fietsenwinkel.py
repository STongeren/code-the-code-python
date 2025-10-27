print("=" * 50)
print("Welkom bij fietsenwinkel De Snelle Trappers!")
print("=" * 50)
print()

voorraad = {
    "Wielen": 10,
    "Stuur": 15,
    "Mountainbike": 5,
    "Fietsbel": 20
}

while True:
    print("\nMENU")
    print("1. Bekijk aanbod")
    print("2. Koop een artikel")
    print("3. Bekijk huidige voorraad")
    print("4. Stop het programma")
    
    keuze = input("\nMaak een keuze (1-4): ")
    
    if keuze == "1":
        print("\nONS AANBOD")
        for item, aantal in voorraad.items():
            print(f"• {item}: {aantal} stuks op voorraad")
    
    elif keuze == "2":
        print("\nKOOP EEN ARTIKEL")
        artikel = input("Welk artikel wil je kopen? ").strip()
        
        gevonden = False
        for item in voorraad.keys():
            if item.lower() == artikel.lower():
                artikel = item
                gevonden = True
                break
        
        if not gevonden:
            print(f"Sorry, '{artikel}' hebben we niet in ons assortiment.")
        elif voorraad[artikel] > 0:
            aantal = int(input(f"Hoeveel {artikel} wil je kopen? "))
            if aantal <= voorraad[artikel]:
                voorraad[artikel] -= aantal
                print(f"Je hebt {aantal} {artikel} gekocht!")
                print(f"  Er zijn nog {voorraad[artikel]} stuks op voorraad.")
            else:
                print(f"Sorry, we hebben maar {voorraad[artikel]} stuks op voorraad.")
        else:
            print(f"Sorry, {artikel} is niet op voorraad!")
    
    elif keuze == "3":
        print("\nHUIDIGE VOORRAAD")
        for item, aantal in voorraad.items():
            status = "Op voorraad" if aantal > 0 else "NIET OP VOORRAAD"
            print(f"{item}: {aantal} stuks - {status}")
    
    elif keuze == "4":
        print("\nBedankt voor je bezoek aan De Snelle Trappers!")
        print("Tot ziens! ")
        break
    
    else:
        print("Ongeldige keuze. Kies 1, 2, 3 of 4.")

