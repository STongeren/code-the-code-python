

print("Welkom bij DrerrieShoppa!")

print("Zonnezeil - Sterrenmotor")

print("Brandstofkosten: 1500 credits", end=" ")
print("| Reserve: 500 credits")

brandstofkosten = 1500
reserve = 500
totaal_brandstof = brandstofkosten + reserve


print(f"\nBerekeningen met brandstofkosten ({brandstofkosten} credits):")
print(f"Floor division (//): {totaal_brandstof} // 3 = {totaal_brandstof // 3}")
print(f"Modulo (%): {totaal_brandstof} % 7 = {totaal_brandstof % 7}")
print(f"Exponentiation (**): {brandstofkosten} ** 2 = {brandstofkosten ** 2}")


octaal_serienummer = 0o12345  
hex_serienummer = 0xABCDEF    

print(f"\nSerienummers van ruimteschepen:")
print(f"Zonnezeil serienummer (octaal): {octaal_serienummer} (octaal: {oct(octaal_serienummer)})")
print(f"Sterrenmotor serienummer (hex): {hex_serienummer} (hex: {hex(hex_serienummer)})")

print("\nBedankt voor uw bezoek aan RuimteShoppa!")
