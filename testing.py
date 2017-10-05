Elementen:
#legenda
doos = 2
lege positie = 0
doellocatie = 1
muur = 4
Medewerker = 5 
gevulde doellocatie = 3

Speelveld=
	[
		[4,4,4,4,4,4,4,4],
		[4,4,4,0,0,0,4,4],
		[4,1,5,2,0,0,4,4],
		[4,4,4,0,2,1,4,4],
		[4,1,4,4,2,0,4,4],
		[4,0,4,0,1,0,4,4],
		[4,2,0,3,2,2,1,4],
		[4,0,0,0,1,0,0,4],
		[4,4,4,4,4,4,4,4],
	]

if richting=rechts--> x=1
elif richting=links --> x=-1
elif richting = boven --> y=1
else richting = onder --> y=-1
position = [x,y]

#init
doosverplaatsen = true
verplaatsen medewerker = true

#checks
if plaats medewerker+a = Doos and plaats doos + a = Muur:
		doosverplaatsen = false
		verplaatsen medewerker = false
elif plaats medewerker+1 = muur:
	verplaatsenmedewerker= false

#acties
if doosverplaatsen=true and verplaatsenmedewerker=true:
	doos verplaatsen() and medewerker verplaatsen()
elif verplaatsenmedewerker:
	medewerker verplaatsen()
