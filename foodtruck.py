

print("Welkom bij De Derrie Foodtruck!")

print("\n=== ONZE GEREICHTEN ===")
gerechten = [
    "1. Galactische Burger",
    "2. Ruimte-Taco's", 
    "3. Sterren-Pizza",
    "4. Maan-Wrap",
    "5. Komeet-Hotdog",
    "6. Nebula-Salade"
]

for gerecht in gerechten:
    print(gerecht)


print("\n=== EXTRA TOPPINGS ===")
toppings = [
    "1. Ruimte-Kaas",
    "2. Sterren-Avocado", 
    "3. Galactische Bacon",
    "4. Maan-Uien",
    "5. Komeet-Tomaat",
    "6. Nebula-Sla",
    "7. Zon-Pickles",
    "8. Melkweg-Champignons"
]

for topping in toppings:
    print(topping)

print("\n=== DANKJES ===")
drankjes = [
    "1. Galactische Limonade",
    "2. Sterren-Milkshake", 
    "3. Ruimte-Cola"
]

for drankje in drankjes:
    print(drankje)

print("\n" + "="*50)
print("TIJD OM TE BESTELLEN!")
print("="*50)


gerecht_keuze = input("Kies een gerecht (1-6): ")
gerecht_nummer = int(gerecht_keuze)
gekozen_gerecht = gerechten[gerecht_nummer - 1].split(". ", 1)[1]

topping_keuze = input("Kies een topping (1-8): ")
topping_nummer = int(topping_keuze)
gekozen_topping = toppings[topping_nummer - 1].split(". ", 1)[1] 

drankje_keuze = input("Kies een drankje (1-3): ")
drankje_nummer = int(drankje_keuze)
gekozen_drankje = drankjes[drankje_nummer - 1].split(". ", 1)[1]  


print(f"\n🚀 BESTELLING BEVESTIGD! 🚀")
print(f"Gerecht: {gekozen_gerecht} | Topping: {gekozen_topping} | Drankje: {gekozen_drankje}")
print("Bedankt voor je bestelling bij De Galactische Foodtruck!")
