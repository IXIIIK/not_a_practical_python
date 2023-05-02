import collections
from pprint import pprint

def graph_of_the_poor(text):
    res = {}

    for char in text.lower().replace(' ', '').replace('—', '').replace(',', '').replace('1', ''):
        res.setdefault(char, []).append(char) 
    return res
