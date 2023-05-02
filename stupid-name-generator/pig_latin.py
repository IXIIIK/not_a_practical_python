def pig_latin(string):
    consonants = [
                'B', 'C', 'D', 'F', 'G', 'H', 'J', 'K',
                'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T',
                'V', 'W', 'X', 'Y', 'Z'
                ]
    vowels = ['A', 'E', 'I', 'O', 'U', 'Y']

    if string[0].upper() in consonants:
        string += string[0] + 'ay'
    elif string[0].upper() in vowels:
        string = string[0:] + 'way'

    return string
