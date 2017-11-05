################################# Remco Cloudt (1551868) & Tawwab Djalielie (1548166) ##################################
import os

# todo: refactoring: turftekst & trainTaalherkenning; de recursie is niet nodig. Het zorgt voor verwarring en is niet efficiënt, gezien de dict-variable steeds herschreven wordt. Maak gebruik van een loop!
# todo: het aantal woorden in een tekst gelijk maken

### Globale variabelen
USERINPUTPATH = os.path.abspath("") + '\\Input\\'
TEKSTENPATH = os.path.abspath("") + '\\Teksten\\'
AANTALTEKSTEN = \
    {
        'Engels': 0,
        'Nederlands': 0,
        'Frans': 0,
        'Duits': 0,
        'Portugees': 0,
        'Spaans': 0
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
        'Portugees':
            {
                'Bi': {},
                'Tri': {},
                'BiKans': {},
                'TriKans': {}
            },
        'Spaans':
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
    parser = open(tekstpath, 'r', encoding='utf-8')
    tekst = parser.read()
    parser.close()

    # turving
    i = 0
    j = ngram

    while j <= len(tekst):
        string = tekst[i:j]
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

    # train taalherkenning: turving
    for taal in DICTALEN:
        trainTaalherkenning(AANTALTEKSTEN[taal], DICTALEN, taal)


def verkrijgNgram(tekst, ngram):
    gram = []

    i = 0
    j = ngram

    while j <= len(tekst):
        gram.append(tekst[i:j])
        i += 1
        j += 1

    # slice eerste en laatste bigram weg voor de tussenliggende bigrammen
    if ngram == 2 and len(gram) > 2:
        gram = gram[1:len(gram) - 1]

    return gram


def smoothing(grammen, ngram):
    for gram in grammen:
        for each in DICTALEN:
            if gram not in DICTALEN[each][ngram]:
                DICTALEN[each][ngram][gram] = 1


def berekenKansInputTekst(listNgram, ngram, taal):
    kans = 1

    for gram in listNgram:
        kans *= DICTALEN[taal][ngram + 'Kans'][gram]

    return kans


### programmauitvoer
print('Een ogenblik geduld...')

## init taalherkenning
initTaalHerkenning()

## taalherkenning gebruikersinvoer
kansenTekst = \
    {
        'Engels': 0,
        'Nederlands': 0,
        'Frans': 0,
        'Duits': 0,
        'Portugees': 0,
        'Spaans': 0
    }

inputTekst = input("Geef uw tekstinvoer: ")

# kans berekenen voor inputTekst gegeven de taal
trigrammen = verkrijgNgram(inputTekst, 3)
tussenliggendeBigrammen = verkrijgNgram(inputTekst, 2)

# smoothing
smoothing(trigrammen, 'Tri')
smoothing(tussenliggendeBigrammen, 'Bi')

# bereken kansen van de Bi en Tri grammen
for taal in DICTALEN:
    DICTALEN = berekenKansen(DICTALEN, taal)

# bereken kans van de inputstring bij een bepaalde taal
for taal in kansenTekst:
    kansTrigrammen = berekenKansInputTekst(trigrammen, 'Tri', taal)
    kansTussenliggendeBigrammen = berekenKansInputTekst(tussenliggendeBigrammen, 'Bi', taal)

    kansenTekst[taal] = kansTrigrammen / kansTussenliggendeBigrammen

# neem hoogste kans
herkendeTaal = max(kansenTekst.keys(), key=(lambda k: kansenTekst[k]))

## output
print('De taal dat herkend wordt is: ' + herkendeTaal)
