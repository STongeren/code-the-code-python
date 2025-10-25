print("=" * 60)
print("🦝 Hallo, welkom bij De Grote Wasberenwinkel! 🦝")
print("=" * 60)
print()

wasberen_aanbod = [
    "baby wasbeer",
    "rare wasbeer",
    "oude wasbeer",
    "vieze wasbeer",
    "wasbeer met zonnebril",
    "dansende wasbeer"
]

prijzen = {
    "baby wasbeer": 25.99,
    "rare wasbeer": 49.99,
    "oude wasbeer": 15.99,
    "vieze wasbeer": 10.99,
    "wasbeer met zonnebril": 39.99,
    "dansende wasbeer": 44.99
}

winkelwagen = []

while True:
    print("\n--- MENU ---")
    print("1. Bekijk ons aanbod")
    print("2. Koop een wasbeer")
    print("3. Bekijk winkelwagen")
    print("4. Verwijder uit winkelwagen")
    print("5. Afreken en stop")
    print("6. BONUS: Sorteer wasberen alfabetisch")
    print("7. BONUS: Tel hoe vaak een wasbeer is gekocht")
    
    keuze = input("\nMaak een keuze (1-7): ")
    
    if keuze == "1":
        print("\n--- ONS WASBEREN AANBOD ---")
        for i, wasbeer in enumerate(wasberen_aanbod, 1):
            print(f"{i}. {wasbeer.capitalize()} - €{prijzen[wasbeer]:.2f}")
    
    elif keuze == "2":
        print("\n--- KOOP EEN WASBEER ---")
        for i, wasbeer in enumerate(wasberen_aanbod, 1):
            print(f"{i}. {wasbeer.capitalize()} - €{prijzen[wasbeer]:.2f}")
        
        try:
            nummer = int(input("\nKies een nummer (1-6): "))
            if 1 <= nummer <= len(wasberen_aanbod):
                gekozen_wasbeer = wasberen_aanbod[nummer - 1]
                winkelwagen.append(gekozen_wasbeer)
                print(f"✓ {gekozen_wasbeer.capitalize()} is toegevoegd aan je winkelwagen!")
            else:
                print("✗ Ongeldig nummer!")
        except ValueError:
            print("✗ Voer een geldig nummer in!")
    
    elif keuze == "3":
        print("\n--- JOUW WINKELWAGEN ---")
        if len(winkelwagen) == 0:
            print("Je winkelwagen is leeg.")
        else:
            totaal = 0
            for i, wasbeer in enumerate(winkelwagen, 1):
                prijs = prijzen[wasbeer]
                print(f"{i}. {wasbeer.capitalize()} - €{prijs:.2f}")
                totaal += prijs
            print(f"\nSubtotaal: €{totaal:.2f}")
    
    elif keuze == "4":
        print("\n--- VERWIJDER UIT WINKELWAGEN ---")
        if len(winkelwagen) == 0:
            print("Je winkelwagen is leeg.")
        else:
            for i, wasbeer in enumerate(winkelwagen, 1):
                print(f"{i}. {wasbeer.capitalize()}")
            
            try:
                nummer = int(input("\nWelk item wil je verwijderen? (nummer): "))
                if 1 <= nummer <= len(winkelwagen):
                    verwijderd = winkelwagen.pop(nummer - 1)
                    print(f"✓ {verwijderd.capitalize()} is verwijderd uit je winkelwagen.")
                else:
                    print("✗ Ongeldig nummer!")
            except ValueError:
                print("✗ Voer een geldig nummer in!")
    
    elif keuze == "5":
        print("\n" + "=" * 60)
        print("AFREKENEN")
        print("=" * 60)
        
        if len(winkelwagen) == 0:
            print("Je winkelwagen is leeg. Tot ziens!")
        else:
            print("\n--- JOUW BESTELLING ---")
            totaal = 0
            for wasbeer in winkelwagen:
                prijs = prijzen[wasbeer]
                print(f"• {wasbeer.capitalize()} - €{prijs:.2f}")
                totaal += prijs
            
            print(f"\n--- TOTAAL: €{totaal:.2f} ---")
            print(f"\nJe hebt {len(winkelwagen)} wasberen gekocht!")
            print("\nBedankt voor je bestelling bij De Grote Wasberenwinkel! 🦝")
        
        break
    
    elif keuze == "6":
        print("\n--- BONUS: GESORTEERDE WASBEREN (ALFABETISCH) ---")
        gesorteerd = sorted(wasberen_aanbod)
        for i, wasbeer in enumerate(gesorteerd, 1):
            print(f"{i}. {wasbeer.capitalize()}")
    
    elif keuze == "7":
        print("\n--- BONUS: AANTAL KEER GEKOCHT ---")
        wasbeer_naam = input("Welke wasbeer wil je tellen? ").strip().lower()
        
        if wasbeer_naam in wasberen_aanbod:
            aantal = winkelwagen.count(wasbeer_naam)
            print(f"\n'{wasbeer_naam.capitalize()}' zit {aantal} keer in je winkelwagen.")
        else:
            print(f"✗ '{wasbeer_naam}' staat niet in ons aanbod.")
    
    else:
        print("✗ Ongeldige keuze. Kies tussen 1 en 7.")

