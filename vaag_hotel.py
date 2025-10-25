print("=" * 50)
print("🏨 Welkom bij Het Vage Hotel 🏨")
print("=" * 50)
print()

hotel = [[[False for kamer in range(5)] for verdieping in range(3)] for gebouw in range(3)]

print("Hotel aangemaakt met 3 gebouwen, 3 verdiepingen en 5 kamers per verdieping.")
print("Status: False = leeg, True = bezet\n")

while True:
    print("\n--- MENU ---")
    print("1. Laat iemand inchecken")
    print("2. Bekijk overzicht van alle kamers")
    print("3. Laat iemand uitchecken")
    print("4. Stop programma")
    
    keuze = input("\nMaak een keuze (1-4): ")
    
    if keuze == "1":
        print("\n--- INCHECKEN ---")
        try:
            gebouw = int(input("Welk gebouw? (1-3): ")) - 1
            verdieping = int(input("Welke verdieping? (1-3): ")) - 1
            kamer = int(input("Welke kamer? (1-5): ")) - 1
            
            if 0 <= gebouw < 3 and 0 <= verdieping < 3 and 0 <= kamer < 5:
                if hotel[gebouw][verdieping][kamer]:
                    print(f"✗ Kamer {kamer+1} op verdieping {verdieping+1} in gebouw {gebouw+1} is al bezet!")
                else:
                    hotel[gebouw][verdieping][kamer] = True
                    print(f"✓ Inchecken geslaagd! Kamer {kamer+1} op verdieping {verdieping+1} in gebouw {gebouw+1}.")
            else:
                print("✗ Ongeldige kamer, verdieping of gebouw!")
        except ValueError:
            print("✗ Voer geldige nummers in!")
    
    elif keuze == "2":
        print("\n--- OVERZICHT VAN ALLE KAMERS ---")
        print()
        
        for g in range(3):
            print(f"╔═══════════════════════════════════════╗")
            print(f"║         GEBOUW {g+1}                      ║")
            print(f"╚═══════════════════════════════════════╝")
            
            for v in range(3):
                print(f"\n  Verdieping {v+1}:")
                kamer_status = ""
                for k in range(5):
                    status = "🔴" if hotel[g][v][k] else "🟢"
                    kamer_status += f"  Kamer {k+1}: {status}"
                print(kamer_status)
            print()
        
        print("\nLegenda: 🟢 = Vrij | 🔴 = Bezet")
        
        totaal_kamers = 3 * 3 * 5
        bezette_kamers = sum(sum(sum(verdieping) for verdieping in gebouw) for gebouw in hotel)
        vrije_kamers = totaal_kamers - bezette_kamers
        
        print(f"\nStatistieken:")
        print(f"• Totaal kamers: {totaal_kamers}")
        print(f"• Bezette kamers: {bezette_kamers}")
        print(f"• Vrije kamers: {vrije_kamers}")
    
    elif keuze == "3":
        print("\n--- UITCHECKEN ---")
        try:
            gebouw = int(input("Welk gebouw? (1-3): ")) - 1
            verdieping = int(input("Welke verdieping? (1-3): ")) - 1
            kamer = int(input("Welke kamer? (1-5): ")) - 1
            
            if 0 <= gebouw < 3 and 0 <= verdieping < 3 and 0 <= kamer < 5:
                if not hotel[gebouw][verdieping][kamer]:
                    print(f"✗ Kamer {kamer+1} op verdieping {verdieping+1} in gebouw {gebouw+1} is al leeg!")
                else:
                    hotel[gebouw][verdieping][kamer] = False
                    print(f"✓ Uitchecken geslaagd! Kamer {kamer+1} is nu beschikbaar.")
            else:
                print("✗ Ongeldige kamer, verdieping of gebouw!")
        except ValueError:
            print("✗ Voer geldige nummers in!")
    
    elif keuze == "4":
        print("\nBedankt voor je bezoek aan Het Vage Hotel! 🏨")
        print("Tot ziens!")
        break
    
    else:
        print("✗ Ongeldige keuze. Kies tussen 1 en 4.")

