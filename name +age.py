huidige_leeftijd = int(input('Hoe oud ben je?'))
leeftijd_over_een_jaar = huidige_leeftijd + 1
print(leeftijd_over_een_jaar)

def omtrek_cirkel_berekenen(straal):
     omtrek =3,1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132823066470938446095505822317253594081284811174502841027019385211055596446229489549303819644288109756659334461284756482337867831652712019091456485669234603 * straal
     return omtrek
     
    #sayHello("Maxim")

print("de omtrek van de cirkel met straal 5 is:", omtrek_cirkel_berekenen(5))

def vraag_input(onderwerp):
     return input("geef me een" + onderwerp +": ")
