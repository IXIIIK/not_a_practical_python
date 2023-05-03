from load_dictinory import load

def main():
    words = load('wordlist.txt')
    res = []

    for word in words:
        if len(word) > 1 and word == word[::-1]:
            res.append(word)
    print(*res, sep=', ')
    return 'число обнаруженный палидромов = {}'.format(len(res))

if __name__ == '__main__':
    print(main())
