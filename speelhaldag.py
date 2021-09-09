#speelhaldag
#3 vrienden, toegangsticket per persoon 7,45
# met zijn allen voor 45 minuten GameSeat
# GameSeat kost per persoon 37 eurocent per 5 minuten.
aantal_p = 4
prijs_t = 7.45
prijs_gs = 0.37
tijd_op_gs = 45
tijd_betaal = 5

kosten = aantal_p * prijs_t + (prijs_gs * (tijd_op_gs / tijd_betaal))

kostenbericht = 'Dit geweldige dagje-uit met 4 mensen in de Speelhal met 45 minuten VR kost je maar ' + str(kosten) + ' euro'

print(kostenbericht)
