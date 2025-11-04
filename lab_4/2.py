# Пусть дана строка.
# На основе данной строки сформируйте две новые. 
# Первая строка содержит только цифры, вторая — только буквы. Выведите новые строки построчно. 

import random

def getWordByAlphabet(some_string, alphabet):
    result = ''
    
    for letter in some_string:
        if letter in alphabet:
            result += letter    
            
    return result

LETTER_ALPHABET = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З',
           'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р',
           'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ',
           'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']

NUMBER_ALPHABET = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

ALPHABET = LETTER_ALPHABET + NUMBER_ALPHABET

SOME_STRING_LEGHT = 15

print('Программа для сортировки строк.\n')

some_string = ''

for _ in range(SOME_STRING_LEGHT):
    some_string += ALPHABET[random.randint(0, len(ALPHABET) - 1)]

print(f'Некоторая строка: {some_string}')
    
first_string = getWordByAlphabet(some_string, NUMBER_ALPHABET)
second_string = getWordByAlphabet(some_string, LETTER_ALPHABET)

print(f'Первая строка (только цифры): {first_string}')
print(f'Вторая строка (только буквы): {second_string}')