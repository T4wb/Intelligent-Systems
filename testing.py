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
        self.positionMedewerker = [2, 2] # deze waarde mee aanpassen wanneer er een ander speelveld gebruikt wordt!



a = Speelveld()
b = Speelveld()

b.positionMedewerker = [1,4]

i=0
while i < len(a.speelveld):
    if a.speelveld[i] != b.speelveld[i]:
        print('exception')
        break
    i += 1


stappen = ['onder', 'boven', 'links', 'rechts']

for stap in stappen:
    print(stap, end=' ')