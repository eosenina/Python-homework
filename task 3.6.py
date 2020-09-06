print('Задание №6')

letters_dict = {'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D', 'e': 'E', 'f': 'F', 'g': 'G',
                'h': 'H', 'i': 'I', 'j': 'J', 'k': 'K', 'l': 'L', 'm': 'M', 'n': 'N',
                'o': 'O', 'p': 'P', 'q': 'Q', 'r': 'R', 's': 'S', 't': 'T', 'u': 'U',
                'v': 'V', 'w': 'W', 'x': 'X', 'y': 'Y', 'z': 'Z'}
small_letters = set('abcdefghijklmnopqrstuvwxyzабвгдеёжзийклмнопрстуфхцчшщъыьэюя')


def my_capitalize(word):
    """
    Функция выполняет замену строчной буквы латинского
    или русского алфавита в первом символе входной строки
    на заглавную, обращаясь к кодам символов букв и вычисляя
    код заглавной буквы.
    :param word: строка
    :return: исходная строка с заглавной буквы
    """
    if word[0] in small_letters:
        diff = 80 if word[0] == 'ё' else 32
        return chr(ord(word[0]) - diff) + word[1::]
    else:
        return word


def my_capitalize1(word):
    """
    Функция выполняет замену строчной буквы латинского
    алфавита в первом символе входной строки на
    заглавную с помощью словаря.
    :param word: строка
    :return: исходная строка с заглавной буквы
    """
    if word[0] in letters_dict.keys():
        return letters_dict[word[0]] + word[1::]
    else:
        return word


line = input('Введите строку: ')
words_list = line.split()
for i in range(0, len(words_list)):
    words_list[i] = my_capitalize(words_list[i])
new_line = ' '.join(words_list)
print(new_line)


