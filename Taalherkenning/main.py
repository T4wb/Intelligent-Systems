import os

# to do: smoothing
# evt to do: outputs wegschrijven zodat wanneer programma herstart wordt de oude resultaten behouden blijven.

# Talen:
# Engels
# Nederlands
# Frans
# Duits
# Russisch
# Hongaars

# init
TEKSTENPATH = os.path.abspath("") + '\\Teksten\\'# todo: maak een apart project & TEKSTENPATH aanpassen!

dictTalen = \
    {
        'Engels':
            {
                'Bi': {},
                'Tri': {}
            },
        'Nederlands':
            {
                'Bi': {},
                'Tri': {}
            },
        'Frans':
            {
                'Bi': {},
                'Tri': {}
            },
        'Duits':
            {
                'Bi': {},
                'Tri': {}
            },
        'Russisch':
            {
                'Bi': {},
                'Tri': {}
            },
        'Hongaars':
            {
                'Bi': {},
                'Tri': {}
            }

    }


def turf(tekstnummer, ngram, dictTurving, taal):
    # todo: pen bijbehorende tekst
    tekstpath = TEKSTENPATH + taal + '\\tekst' + str(tekstnummer) +'.txt'
    parser = open(tekstpath, 'r')
    tekst = parser.read()
    parser.close()

    x=1
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
    x=1


def tekstTraining(tekstnummer, turfDict, taal):
    if tekstnummer < 1:
        return turfDict
    else:
        dictTaal = tekstTraining(tekstnummer-1, turfDict, taal)

        ## turf dictTri
        turf(tekstnummer, 3, dictTaal[taal]['Tri'], taal)

        ## turf dictBi
        turf(tekstnummer, 2, dictTaal[taal]['Bi'], taal)

        return dictTaal

        # berekenen kansen

tekstTraining(2, dictTalen, 'Engels')
x=1
# todo: herkenning inputstring


