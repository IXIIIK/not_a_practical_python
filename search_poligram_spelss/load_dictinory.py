import sys

def load(file):
    try:
        with open(file) as in_file:
            loader_text = in_file.read().strip().split('\n')
            loader_text = [i.lower() for i in loader_text]
            return loader_text
    except IOError as e:
        print('{} \n ошибка при открытие {}. Завершение программы'.
              format(e, file), file=sys.stderr)
        sys.exit(1)
