################################# Remco Cloudt (1551868) & Tawwab Djalielie (1548166) ##################################

import copy
from enum import Enum

'''
Legenda:
	+ Lege positie        = 0
	+ Doellocatie         = 1
	+ Doos                = 2
	+ Gevulde doellocatie = 3
	+ Muur                = 4
	+ Medewerker          = 5
	
Aannames:
	+ Speelveld is altijd een matrix.
'''


### classes
## initiele waardes
class Element(Enum):
    DOELLOCATIE = 1
    DOOS = 2
    GEVULDELOCATIE = 3
    MUUR = 4
    MEDEWERKER = 5


class Speelveld:
    def __init__(self):
        self.padkosten = 0
        self.speelveld = \
            [
                [4, 4, 4, 4, 4, 4, 4, 4],
                [4, 4, 4, 0, 0, 0, 4, 4],
                [4, 1, 5, 2, 0, 0, 4, 4],
                [4, 4, 4, 0, 2, 1, 4, 4],
                [4, 1, 4, 4, 2, 0, 4, 4],
                [4, 0, 4, 0, 1, 0, 4, 4],
                [4, 2, 0, 3, 2, 2, 1, 4],
                [4, 0, 0, 0, 1, 0, 0, 4],
                [4, 4, 4, 4, 4, 4, 4, 4]
            ]
        self.positionMedewerker = vindPositionMedewerker(self.speelveld)


## kinderen
class Kindknoop:
    def __init__(self, ouder, actie, coordinatenPositie2, coordinatenPositie3, waardePositie2, waardePositie3):
        self.ouder = ouder
        self.actie = actie
        self.padkosten = ouder.padkosten + 1
        self.speelveld = [list(x) for x in ouder.speelveld] # dit is sneller dan copy.deepcopy(ouder.speelveld)

        # nieuwe positie medewerker
        self.positionMedewerker = \
            [
                ouder.positionMedewerker[0] + actie[0],
                ouder.positionMedewerker[1] + actie[1]
            ]

        ## berekenen van de verplaatsing
        # positie1 = de start positie van de medewerker aan het begin van een kindknoop

        # tel waarde positie2 op bij positie3 enkel als positie2 een doos of een gevulde locatie is
        if waardePositie2 == Element.DOOS.value or waardePositie2 == Element.GEVULDELOCATIE.value:  # fix: aangepast: verplaats doos op doellocatie ook
            self.speelveld[coordinatenPositie3[0]][
                coordinatenPositie3[1]] += Element.DOOS.value  # fix: aangepast: verplaats doos i.p.v. waardePositie2
            # trek waarde positie2 af van positie2
            self.speelveld[self.positionMedewerker[0]][self.positionMedewerker[
                1]] -= Element.DOOS.value  # fix: aangepast: verplaats doos i.p.v. waardePositie2

        # medewerker verplaatsen naar positie 2
        self.speelveld[self.positionMedewerker[0]][self.positionMedewerker[1]] += Element.MEDEWERKER.value

        # waarde positie1 terugzetten naar oude status (waarde: 0 of 1)
        self.speelveld[ouder.positionMedewerker[0]][ouder.positionMedewerker[1]] -= Element.MEDEWERKER.value


### functions
def vindPositionMedewerker(speelveld):
    y = 0
    x = 0
    gevonden = False
    positionMedewerker = [len(speelveld), len(speelveld[0])]  # Is nodig: list index out of bounds als positie niet gevonden wordt

    while not gevonden and y < len(speelveld):
        while not gevonden and x < len(speelveld[0]):
            if speelveld[y][x] == Element.MEDEWERKER.value:
                gevonden = True
                positionMedewerker = [y, x]
            x += 1
        y += 1
        x = 0

    return positionMedewerker


def GenereerKinderen(ouder):
    kinderen = []
    acties = \
        [
            [0, 1],  # Rechts
            [0, -1],  # Links
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

        ## checks of geldige coordinaten positie 3
        geldigeActie = False

        # checks worden alleen uitgevoerd als de coordinaat van positie3 binnen het matrix ligt
        if coordinatenPositie3[0] < len(ouder.speelveld) and coordinatenPositie3[1] < len(ouder.speelveld[0]):
            geldigeActie = True

            waardePositie2 = ouder.speelveld[coordinatenPositie2[0]][coordinatenPositie2[1]]
            waardePositie3 = ouder.speelveld[coordinatenPositie3[0]][coordinatenPositie3[1]]

            # check of een medewerker naast een doos staat en er een muur achter de doos staat
            if waardePositie2 == Element.DOOS.value and waardePositie3 == Element.MUUR.value:
                geldigeActie = False

            # check of er een muur naast de medewerker staat
            elif waardePositie2 == Element.MUUR.value:
                geldigeActie = False

            # check of er achter de doos een andere doos staat
            elif waardePositie2 == Element.DOOS.value & waardePositie3 == Element.DOOS.value:
                geldigeActie = False  # aangevuld

            # check of speler naast een doos staat dat op een doellocatie staat, terwijl hierachter een muur staat
            elif waardePositie2 == Element.DOOS.value + Element.DOELLOCATIE.value and waardePositie3 == Element.MUUR.value:
                geldigeActie = False

            # check of speler naast een doos staat dat op een doellocatie staat, terwijl hierachter een andere doos staat
            elif waardePositie2 == Element.DOOS.value + Element.DOELLOCATIE.value and waardePositie3 == Element.DOOS.value:
                geldigeActie = False

        ## genereer kinderen
        if geldigeActie:
            kind = Kindknoop(ouder, actie, coordinatenPositie2, coordinatenPositie3, waardePositie2, waardePositie3)

            if ouder.padkosten != 0:
                # controleer of het speelveld van de voorouder van het kind gelijk is aan zijn speelveld
                i = 0
                inverseActie = True
                while inverseActie and i < len(ouder.speelveld):
                    if kind.speelveld[i] != kind.ouder.ouder.speelveld[i]:
                        inverseActie = False
                    i += 1

                if not inverseActie:
                    kinderen.append(kind)

            elif ouder.padkosten == 0:
                kinderen.append(kind)

    return kinderen


## controles
def Controleerspeelveld(knoop):
    for y in range(0, len(knoop.speelveld)):
        for x in range(0, len(knoop.speelveld[0])):
            if knoop.speelveld[y][x] == Element.DOOS.value:
                return False

    return True


## zoeken
def DepthLimited(root, zoekdiepte):
    teDoorzoekenLijst = []
    teDoorzoekenLijst.append(root)

    while teDoorzoekenLijst != []:
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
        print(i)
        i += 1

    return False  # overbodig: candidate for refactoring


### execution
root = Speelveld()
IterativeDeepening(root)