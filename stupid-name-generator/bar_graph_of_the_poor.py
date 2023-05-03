from pprint import pprint

fixture = ['a', 'b', 'c', 'd', 'e', 'g', 'i', 'j',
           'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 
           't', 'u', 'y', 'v']

def graph_of_the_poor(text):
    res = {}

    for char in text.lower():
        if char in fixture:
            res.setdefault(char, []).append(char) 
    return res
