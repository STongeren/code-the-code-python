

print("Welkom bij DrerrieShoppa!")
print("")

print("Zonnezeil - Sterrenmotor")
print("")

print("Brandstofkosten: 1500 credits", end=" ")
print("| Reserve: 500 credits")
print("")

brandstofkosten = 1500
reserve = 500
totaal_brandstof = brandstofkosten + reserve

print("Berekeningen met brandstofkosten:")
print("Totaal brandstof: " + str(totaal_brandstof) + " credits")
print("")

floor_deling = totaal_brandstof // 3
print("Floor division (//): " + str(totaal_brandstof) + " // 3 = " + str(floor_deling))

modulo = totaal_brandstof % 7
print("Modulo (%): " + str(totaal_brandstof) + " % 7 = " + str(modulo))

macht = brandstofkosten ** 2
print("Exponentiation (**): " + str(brandstofkosten) + " ** 2 = " + str(macht))
print("")

octaal_serienummer = 0o12345
hex_serienummer = 0xABCDEF

print("Serienummers van ruimteschepen:")
print("Zonnezeil serienummer (octaal): " + str(octaal_serienummer))
print("Sterrenmotor serienummer (hex): " + str(hex_serienummer))
print("")

print("Bedankt voor uw bezoek aan RuimteShoppa!")
