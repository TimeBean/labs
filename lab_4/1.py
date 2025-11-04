# Пусть задан список, содержащий строки.
# Выведите все строки, начинающиеся с буквы Л. 

import random

ALPHABET = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З',
           'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р',
           'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ',
           'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я' ]

WORDS_COUNT = 100
WORD_LENGHT = 5

print('Программа для сортировки слов.\n')

words = []

for _ in range(WORDS_COUNT):
    word = ''
    for _ in range(WORD_LENGHT):
        word += ALPHABET[random.randint(0, len(ALPHABET) - 1)]
        
    words.append(word)
    
print(f"Изначальный список: {words}.\n")

sorted_words = []

for word in words:
    if word[0] == 'Л':
        sorted_words.append(word)
        
print(f'Отсортированные слова: {sorted_words}.')