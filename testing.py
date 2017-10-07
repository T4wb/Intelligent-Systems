################################# Remco Cloudt (1551868) & Tawwab Djalielie (1548166) ##################################

import copy

'''
Legenda:
	doos = 2
	lege positie = 0
	doellocatie = 1
	muur = 4
	Medewerker = 5
	gevulde doellocatie = 3
	
	Aanname:
	speelveld is altijd een matrix
'''


class Speelveld:
    def __init__(self):
        self.speelveld = \
            [
                [4, 4, 4, 4, 4],
                [4, 5, 1, 0, 4],
                [4, 0, 2, 0, 4],
                [4, 0, 0, 0, 4],
                [4, 4, 4, 4, 4]
            ]
        self.positionMedewerker = [1, 1]
        self.padkosten = 0


class Kindknoop:
    def __init__(self, ouder, actie, coordinatenPositie2, coordinatenPositie3, positie2, positie3):
        self.ouder = ouder
        self.actie = actie
        self.speelveld = copy.deepcopy(ouder.speelveld)
        self.padkosten = ouder.padkosten + 1

        # nieuwe positie medewerker
        self.positionMedewerker = \
            [
                ouder.positionMedewerker[0] + actie[0],
                ouder.positionMedewerker[1] + actie[1]
            ]

        ## berekenen van de verplaatsing
        # positie1 = de start positie van de medewerker aan het begin van een kindknoop

        # tel waarde positie2 op bij positie3 enkel als positie2 een doos is
        if positie2 == 2:
            self.speelveld[coordinatenPositie3[0]][coordinatenPositie3[1]] += positie2

        # trek waarde positie2 af van positie2
        self.speelveld[self.positionMedewerker[0]][self.positionMedewerker[1]] -= positie2

        # medewerker verplaatsen naar positie 2
        # waarde medewerker optellen bij positie2
        self.speelveld[self.positionMedewerker[0]][self.positionMedewerker[1]] += 5

        # waarde positie1 terugzetten naar oude status (0 of 1)
        self.speelveld[ouder.positionMedewerker[0]][ouder.positionMedewerker[1]] -= 5


def GenereerKinderen(ouder):
    kinderen = []
    acties = \
        [
            [0, 1],  # Rechts
            [0, -1], # Links
            [1, 0],  # Boven
            [-1, 0]  # Onder
        ]

    #### rules
    for actie in acties:
        ### generate speelveld
        ## initiele waardes
        coordinatenPositie2 = \
            [
                ouder.positionMedewerker[0] + actie[0],
                ouder.positionMedewerker[1] + actie[1]
            ]

        coordinatenPositie3 = \
            [
                coordinatenPositie2[0] + actie[0],
                coordinatenPositie2[1] + actie[1]
            ]

        # checks of geldige coordinaten positie 3
        geldigeActie = False

        if coordinatenPositie3[0] < len(ouder.speelveld) and coordinatenPositie3[1] < len(ouder.speelveld[0]):
            # verkrijg waarde bij positie2
            positie2 = ouder.speelveld[coordinatenPositie2[0]][coordinatenPositie2[1]]

            # verkrijg waarde bij positie3
            positie3 = ouder.speelveld[coordinatenPositie3[0]][coordinatenPositie3[1]]

            ## checks
            geldigeActie = True

            # testen of een speler naast een doos staat en er een muur achter de doos staat
            if positie2 == 2 and positie3 == 4:
                geldigeActie = False

            # testen of er een muur naast de medewerker staat
            elif positie2 == 4:
                geldigeActie = False

        # genereer kinderen
        if geldigeActie:
            kind = Kindknoop(ouder, actie, coordinatenPositie2, coordinatenPositie3, positie2, positie3)
            kinderen.append(kind)

    return kinderen


def Controleerspeelveld(knoop):
    for y in range(0, len(knoop.speelveld)):
        for x in range(0, len(knoop.speelveld[0])):
            if knoop.speelveld[y][x] == 2:
                return False

    return True


def DepthLimited(root, zoekdiepte):
    teDoorzoekenLijst = []
    teDoorzoekenLijst.append(root)

    while teDoorzoekenLijst:
        huidigeKnoop = teDoorzoekenLijst.pop(0)

        if Controleerspeelveld(huidigeKnoop):
            return True

        if huidigeKnoop.padkosten < zoekdiepte:
            kinderen = GenereerKinderen(huidigeKnoop)

            for kind in kinderen:
                teDoorzoekenLijst.insert(0, kind)

    return False


def IterativeDeepening(root):
    i = 1

    while True:
        if DepthLimited(root, i) == True:
            return True
        i += 1

    return False


## uitvoer
root = Speelveld()
IterativeDeepening(root)
