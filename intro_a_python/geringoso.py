def geringoso(word):
    capadepenapa = ''
    for letter in word:
        if letter in 'aeiou':
            capadepenapa += letter + 'p' + letter
        else:
            capadepenapa += letter
    return capadepenapa


capadepenapa = geringoso('Geringoso')
print(capadepenapa)
capadepenapa = geringoso('apa')
print(capadepenapa)
capadepenapa = geringoso('boligoma')
print(capadepenapa)
