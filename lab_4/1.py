# Пусть задан список, содержащий строки.
# Выведите все строки, начинающиеся с буквы Л. 

import random

WORDS_COUNT = 100
WORD_LENGHT = 5

print('Программа для сортировки слов.\n')

words = []

for _ in range(WORDS_COUNT):
    word = ''
    for _ in range(WORD_LENGHT):
        word += chr(random.randint(1073, 1073 + 31))
        
    words.append(word)
    
print(f"Изначальный список: {words}.\n")

sorted_words = []

for word in words:
    if word[0] == 'Л':
        sorted_words.append(word)
        
print(f'Отсортированные слова: {sorted_words}.')