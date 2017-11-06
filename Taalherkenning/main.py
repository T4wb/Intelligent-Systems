################################# Remco Cloudt (1551868) & Tawwab Djalielie (1548166) ##################################
import os
import math

### Globale variabelen
USERINPUTPATH = os.path.abspath("") + '\\Input\\'
TEKSTENPATH = os.path.abspath("") + '\\Teksten\\'

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
def turfTekst(dictTurving, ngram, taal):
    tekstpath = TEKSTENPATH + taal + '.txt'
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


def trainTaalherkenning(turfDict, taal):
    # turf bigrammen
    turfTekst(turfDict['Bi'], 2, taal)

    # turf trigrammen
    turfTekst(turfDict['Tri'], 3, taal)


def initTaalHerkenning():
    # train taalherkenning: turving
    for taal in DICTALEN:
        trainTaalherkenning(DICTALEN[taal], taal)


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


## inputverwerking
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
        for taal in DICTALEN:
            if gram not in DICTALEN[taal][ngram]:
                DICTALEN[taal][ngram][gram] = 1


def berekenKansInputTekst(listNgram, ngram, taal):
    kans = 1

    for gram in listNgram:
        kans *= math.log10(DICTALEN[taal][ngram + 'Kans'][gram])

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

# bereken kans van de inputtekst bij een bepaalde taal
for taal in kansenTekst:
    kansTrigrammen = berekenKansInputTekst(trigrammen, 'Tri', taal)
    kansTussenliggendeBigrammen = berekenKansInputTekst(tussenliggendeBigrammen, 'Bi', taal)

    kansenTekst[taal] = kansTrigrammen / kansTussenliggendeBigrammen

# verkrijgt key met de hoogste kans-value
herkendeTaal = max(kansenTekst.keys(), key=(lambda k: kansenTekst[k]))

## output
print('De taal die herkend wordt is: ' + herkendeTaal)
