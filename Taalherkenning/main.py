################################# Remco Cloudt (1551868) & Tawwab Djalielie (1548166) ##################################
import os
import re

# todo: smoothing!
# todo: evt outputs wegschrijven zodat wanneer programma herstart wordt de oude resultaten behouden blijven.

### Globale variabelen
USERINPUTPATH = os.path.abspath("") + '\\Input\\'
TEKSTENPATH = os.path.abspath("") + '\\Teksten\\'
AANTALTEKSTEN = \
    {
        'Engels': 0,
        'Nederlands': 0,
        'Frans': 0,
        'Duits': 0,
        'Russisch': 0,
        'Hongaars': 0
    }

DICTALEN = \
    {
        'Engels':
            {
                'Bi': {},
                'Tri': {},
                'BiKans': {},
                'TriKans': {}
            },
        'Nederlands':
            {
                'Bi': {},
                'Tri': {},
                'BiKans': {},
                'TriKans': {}
            },
        'Frans':
            {
                'Bi': {},
                'Tri': {},
                'BiKans': {},
                'TriKans': {}
            },
        'Duits':
            {
                'Bi': {},
                'Tri': {},
                'BiKans': {},
                'TriKans': {}
            },
        'Russisch':
            {
                'Bi': {},
                'Tri': {},
                'BiKans': {},
                'TriKans': {}
            },
        'Hongaars':
            {
                'Bi': {},
                'Tri': {},
                'BiKans': {},
                'TriKans': {}
            }

    }


### functies
## training
def turfTekst(tekstnummer, ngram, dictTurving, taal):
    # todo: try-catch
    tekstpath = TEKSTENPATH + taal + '\\tekst' + str(tekstnummer) + '.txt'
    parser = open(tekstpath, 'r')
    tekst = parser.read()
    parser.close()
    woorden = re.findall(r'(?u)\w+', tekst)

    # turving
    for woord in woorden:
        i = 0
        j = ngram

        # todo: bij bigrammen: gooi alles behalve de tussenliggende bigrammen weg

        while j <= len(woord):
            string = woord[i:j]
            if string in dictTurving:
                dictTurving[string] += 1
            else:
                dictTurving[string] = 1
            i += 1
            j += 1


def trainTaalherkenning(tekstnummer, turfDict, taal):
    if tekstnummer < 1:
        return turfDict
    else:
        dictTaal = trainTaalherkenning(tekstnummer - 1, turfDict, taal)

        # turf dictTri
        turfTekst(tekstnummer, 3, dictTaal[taal]['Tri'], taal)

        # turf dictBi
        turfTekst(tekstnummer, 2, dictTaal[taal]['Bi'], taal)

        return dictTaal


def berekenKansen(kansDict, taal):
    # tel respectievelijk Bi & Tri totaal
    BiTotaal = 0
    TriTotaal = 0

    for bigram in kansDict[taal]['Bi']:
        BiTotaal += kansDict[taal]['Bi'][bigram]

    for trigram in kansDict[taal]['Tri']:
        TriTotaal += kansDict[taal]['Tri'][trigram]

    # bereken respectievelijk Bi & Tri kansen
    for bigram in kansDict[taal]['Bi']:
        kansDict[taal]['BiKans'][bigram] = kansDict[taal]['Bi'][bigram] / BiTotaal

    for trigram in kansDict[taal]['Tri']:
        kansDict[taal]['TriKans'][trigram] = kansDict[taal]['Tri'][trigram] / TriTotaal

    return kansDict

def initTaalHerkenning():
    global DICTALEN

    # scan de taal-directory voor het aantal bestanden bij de behorende taal
    for taal in AANTALTEKSTEN:
        AANTALTEKSTEN[taal] = \
            len([filename for filename in os.listdir(TEKSTENPATH + taal) if filename.startswith("tekst")])

    # train taalherkenning
    for taal in DICTALEN:
        DICTALEN = trainTaalherkenning(AANTALTEKSTEN[taal], DICTALEN, taal)

    # kansenberekening Bi- & Tri-grammen
    for taal in DICTALEN:
        DICTALEN = berekenKansen(DICTALEN, taal)

### uitvoer
## init taalherkenning
initTaalHerkenning()

## taalherkenning gebruikersinvoer
inputTeksten =  [filename for filename in os.listdir(USERINPUTPATH) if filename.endswith(".txt")]
# kansenTekst = {
#     'Engels': 0,
#     'Nederlands': 0,
#     'Frans': 0,
#     'Duits': 0,
#     'Russisch': 0,
#     'Hongaars': 0
#     }
#
# for inputTekst in inputTeksten:
#     # verkrijg woorden
#     # todo: try-catch
#     tekstpath = USERINPUTPATH + inputTekst
#     parser = open(tekstpath, 'r')
#     tekst = parser.read()
#     parser.close()
#     woorden = re.findall(r'(?u)\w+', tekst)
#
#     # kans berekenen voor inputTekst gegeven de taal
#     kansWoorden = 0
#
#     for each in woorden:
#         # bepaal trigrammen en tussenliggende bigrammen
#         for each in DICTALEN:
#             # zoek naar kansen en vermenigvuldig met
#             # bereken kans bij elke taal
#             # schrijf naar dict kansenTekst
#             # neem hoogste waarde als waarheid aan
#
#     # todo: output: print(inputTekst + ': ' + herkendeTaal + \n) =-leidt-tot-> print output: 'tekst1.txt': Engels, 'tekst2.txt': Frans, 'tekst3.txt': Nederlands
#     # todo: welke taal?: tekst = kansen van woorden vermenigvuldigen -> pas smoothing toe!

x = 1 #todo: weghalen; dit is debug-code
