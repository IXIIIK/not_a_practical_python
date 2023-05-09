import sys
sys.path.insert(1 ,'/Users/ilyasinitsyn/not_a_practical_python/search_poligram_spelss')

from load_dictinory import load
from collections import Counter

dict_file = load('../search_poligram_spelss/wordlist.txt')
ini_name = input('Введите слово: ')

def find_anagrams(name, world_list):
    name_letter_map = Counter(name)
    anagrams = []

    for word in world_list:
        test = ''
        word_letter_map = Counter(word.lower())
        for letter in word:
            if word_letter_map[letter] <= name_letter_map[letter]:
                test += letter
            if Counter(test) == word_letter_map:
                anagrams.append(word)
    print(*anagrams, sep='\n')
    print()
    print("Остальные буквы = {}".format(name)) 
    print("Число остальных букв = {}".format(len(name)))
    print("Число остальных анаграмм (реальных слов) = {}".format(len(anagrams)))


def process_choice(name):
    while True:
        msg = '\nВыберите либо введите Enter, чтобы начать сначала, либо # для выхода '
        choice = input(msg)

        if choice == '':
            main()
        elif choice == '#':
            sys.exit()
        else:
            canditate = ''.join(choice.lower().split())
            left_over_list = list(name)

        for letter in canditate:
            if letter in left_over_list:
                left_over_list.remove(letter)
        if len(name) - len(left_over_list) == len(canditate):
            break
        else:
            print("He сработает! Попробовать еще один вариант!", file=sys.stderr)
    name = ''.join(left_over_list)

    return choice, name


def main():
    name = ''.join(ini_name.lower().split())
    name = name.replace('-', '') 
    limit = len(name)
    phrase = ''
    running = True

    while running:
        temp_phrase = phrase.replace(' ', '')
        if len(temp_phrase) < limit:
            print("Длина анаграммного словосочетания = {}". format(len(temp_phrase))) 
            find_anagrams(name, dict_file)
            print("Текущее анаграммное словосочетание =", end=" ")
            print(phrase, file=sys.stderr)  

            choice, name = process_choice(name)
            phrase += choice + ''
        elif len(temp_phrase) == limit:
            print("\n***** ГОТОВО!!! *****\n")
            print("Анаграмма имени =", end=" ")
            print(phrase, file=sys.stderr)
            print()
            msg = '\n\nПробуете еще раз? (Нажмите Enter либо "n" для выхода)\n '
            try_again = input(msg)
            if try_again.lower() == 'n':
                running = False
                sys.exit()
            else:
                main()



if __name__ == '__main__':
    main()


