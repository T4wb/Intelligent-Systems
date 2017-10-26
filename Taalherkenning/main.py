# to do: smoothing
#evt to do: outputs wegschrijven zodat wanneer programma herstart wordt de oude resultaten behouden blijven.

# Talen:
# Engels
# Nederlands
# Frans
# Duits
# Russisch
# Hongaars


# voor elke taal een dict

# tekst analyseren:
tekst= "hello world"

def tekstTraining(x, taal, ngram):
    if x < 1:
        return dictEngels
    else:
        dictTaal, = TekstTraining(x-1, tekst, taal, ngram)


        return dictEngels

    dictEngels={}
    dictDuits={}
    dictFrans={}
    dictNederlands={}
    dictRussisch={}
    dictHongaars = {}

    dictionaryCases = \
        {
            'Engels': dictEngels,
            'Nederlands' : dictNederlands,
            'Frans' : dictFrans,
            'Duits' : dictDuits,
            'Russisch' : dictRussisch,
            'Hongaars' : dictHongaars
        }

    dict = dictionaryCases[taal]

    # ......
    i=0
    j=ngram
    while j <= len(tekst):
        str=tekst[i:j]
        if str in dict:
            dict[str] += 1
        else:
            dict[str] = 1
        i += 1
        j += 1
    print(dict)

    # return
    return dictNederlands

dictTalen = \
    {
        'Engels' :
            {
                'Bi' : {},
                'Tri' : {}
            },
        'Nederlands' :
            {
                'Bi' : {},
                'Tri' : {}
            },
        'Frans' :
            {
                'Bi' : {},
                'Tri' : {}
            },
        'Duits' :
            {
                'Bi' : {},
                'Tri' : {}
            },
        'Russisch' :
            {
                'Bi' : {},
                'Tri' : {}
            },
        'Hongaars' :
            {
                'Bi' : {},
                'Tri' : {}
            }

    }

dictNederlandsTri = tekstTraining("hello world hel","Nederlands",3)
dictNederlandsBi = tekstTraining("hello world hel","Nederlands",3)

# aantal teksten in getallen = 2
dictEngels, = tekstTraining(x, taal, ngram)




i=0
while i < aantalTeksten:
    dictNederlands =
    i += 1

    #bigrams

    #berekenen kansen

#scannen string

#





