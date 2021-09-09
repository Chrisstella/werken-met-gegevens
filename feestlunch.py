#Feestlunch
#17 croissantjes van elk 39 eurocent
#2 stokbroden van elk 2,78 euro kopen.
#3 kortingsbonnen van 50 eurocent.
aantal_c = 17.0
aantal_s = 2.0
aantal_k = 3.0
prijs_c = 0.39
prijs_s = 2.78
korting_k = 0.50

kosten = aantal_c * prijs_c + (aantal_s * prijs_s) - (aantal_k * korting_k)

kostenbericht = 'De feestlunch kost je bij de bakker ' + str(kosten) + ' euro voor de 17 croissantjes en de 2 stokbroden als de 3 kortingsbonnen nog geldig zijn!'

print(kostenbericht)
