from load_dictinory import load


def find_palingrams():
    words = load('wordlist.txt')
    words = set(words)
    res = []

    for word in words:
        end = len(word)
        rev_word = word[::-1]

        if end > 1:
            for i in range(end):
                if word[i:] == rev_word[:end-1] and rev_word[end-1:] in words:
                    res.append((word, rev_word[end-1:]))
                if word[:i] == rev_word[end-1:] and rev_word[:end-1] in words:
                    res.append((rev_word[:end-1], word))
    return res
        
palingrams = find_palingrams()

print("Число палинграмм = {}\n".format(len(palingrams)))