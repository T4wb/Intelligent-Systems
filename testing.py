Elementen:
#legenda
'''
doos = 2
lege positie = 0
doellocatie = 1
muur = 4
Medewerker = 5 
gevulde doellocatie = 3
'''
class Speelveld:
	speelveld=\
		[
			[4,4,4,4,4,4,4,4],
			[4,4,4,0,0,0,4,4],
			[4,1,5,2,0,0,4,4],
			[4,4,4,0,2,1,4,4],
			[4,1,4,4,2,0,4,4],
			[4,0,4,0,1,0,4,4],
			[4,2,0,3,2,2,1,4],
			[4,0,0,0,1,0,0,4],
			[4,4,4,4,4,4,4,4]
		]
	positionMedewerker=[2,2]

class Kindknoop:

	def __init__(self,ouder, actie, coordinatenPositie2, coordinatenPositie3, positie2, positie3):
		self.ouder=ouder
		self.actie=actie
		self.speelveld = ouder.speelveld

		# nieuwe positie medewerker
		self.positionMedewerker = [ouder.positionMedewerker[0] + actie[0], ouder.positionMedewerker[1] + actie[1]]

		#berekenen van de verplaatsing
		#positie1 = de start positie van de medewerker aan het begin van een kindknoop

		# tel waarde positie2 op bij positie3
		self.speelveld[coordinatenPositie3, coordinatenPositie3] += positie2

		# trek waarde positie2 af van positie2
		self.speelveld[self.positionMedewerker[0], self.positionMedewerker[1]] -= positie2

		# medewerker verplaatsen naar positie 2
		# waarde medewerker optellen bij positie2
		self.speelveld[self.positionMedewerker[0], self.positionMedewerker[1]]+= 5

		# waarde positie1 terugzetten naar oude status (0 of 1)
		self.speelveld[ouder.positionMedewerker[0], ouder.positionMedewerker[1]] -= 5

def GenereerKinderen(ouder)
	kinderen=[]
	acties=\
		[
			[1,0], 	#Rechts
			[-1,0], #Links
			[0,1],	#Boven
			[0,-1]	#Onder
		]
	#rules


	for actie in acties:
		### generate speelveld
		## initiele waardes
		# x-y posities van positie 2
		coordinatenPositie2 = ouder.speelveld[ouder.positionMedewerker[0]+actie[0], ouder.positionMedewerker[1]+actie[1]]

		# x-y posities van positie 3
		coordinatenPositie3 = ouder.speelveld[coordinatenPositie2[0] + actie[0], coordinatenPositie2[1] + actie[1]]

		# verkrijg waarde bij positie2
		positie2 = [coordinatenPositie2[0], coordinatenPositie2[1]]

		# verkrijg waarde bij positie3
		positie3 = [coordinatenPositie3[0], coordinatenPositie3[1]]

		# kinderen lijst
		kinderen = []

		## checks
		geldigeActie = True

		# testen of een speler naast een doos staat en er een muur achter de doos staat
		if positie2 == 2 and positie3 == 4:
			geldigeActie = False
		
		#testen of er een muur naast de medewerker staat
		elif positie2 == 4:
			geldigeActie = False

		# genereer kinderen
		if geldigeActie:
			kind = Kindknoop(ouder, actie, coordinatenPositie2, coordinatenPositie3, positie2, positie3)
			kinderen.append(kind)

		return kinderen

# #checks
# if plaats medewerker+a = Doos and plaats doos + a = Muur:
# 		doosverplaatsen = false
# 		verplaatsen medewerker = false
# elif plaats medewerker+1 = muur:
# 	verplaatsenmedewerker= false
#
# #acties
# if doosverplaatsen=true and verplaatsenmedewerker=true:
# 	doos verplaatsen() and medewerker verplaatsen()
# elif verplaatsenmedewerker:
# 	medewerker verplaatsen()
