def geringoso(words):
    geringoso_dictionary = {}

    for word in words:
        capadepenapa = ''
        for letter in word:
            if letter in 'aeiou':
                capadepenapa += letter + 'p' + letter
            else:
                capadepenapa += letter
            geringoso_dictionary[word] = capadepenapa

    return geringoso_dictionary


print(geringoso(['banana', 'manzana', 'mandarina']))
