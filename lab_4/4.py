# Пусть дана строка, состоящая из слов, пробелов и знаков препинания.
# На основании этой строки создайте новую (и выведите ее на консоль): 
# Содержащую только слова, в которых две последние буквы — «ов».

import random

VOWEL_ALPHABET = ['А', 'Е', 'Ё', 'И', 'О', 'У', 'Ы', 'Э', 'Ю', 'Я']
VOWEL_WEIGHTS  = [0.080, 0.085, 0.004, 0.073, 0.109, 0.026, 0.019, 0.003, 0.006, 0.020]

CONSONANT_ALPHABET = ['Б', 'В', 'Г', 'Д', 'Ж', 'З', 'Й', 'К', 'Л', 'М', 
                      'Н', 'П', 'Р', 'С', 'Т', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ']
CONSONANT_WEIGHTS  = [0.015, 0.045, 0.017, 0.030, 0.007, 0.016, 0.010, 0.028, 0.043, 0.032, 
                      0.067, 0.028, 0.047, 0.054, 0.063, 0.002, 0.009, 0.004, 0.012, 0.006, 0.003]

PUNCTUATION_MARK_ALPHABET = [',', '.', '!', '?', ':', ';']
PUNCTUATION_MARK_WEIGHTS  = [0.35, 0.45, 0.05, 0.05, 0.06, 0.04]

WORDS_COUNT = 200
MINIMUM_WORD_LENGTH = 3
MAX_WORD_LENGTH = 10

P_FIRST_CONSONANT = 0.559
P_AFTER_VOWEL_CONSONANT = 0.872
P_AFTER_CONSONANT_VOWEL = 0.663

def weighted_choice(letters, weights):
    return random.choices(letters, weights, k=1)[0]

def generate_weighted_words(WORDS_COUNT, MIN_WORD_LENGTH, MAX_WORD_LENGTH):
    words = []

    for _ in range(WORDS_COUNT):
        word = []
        
        if random.random() < P_FIRST_CONSONANT:
            word += weighted_choice(CONSONANT_ALPHABET, CONSONANT_WEIGHTS)
        else:
            word += weighted_choice(VOWEL_ALPHABET, VOWEL_WEIGHTS)
        
        length = random.randint(MIN_WORD_LENGTH, MAX_WORD_LENGTH)

        for _ in range(length - 1):
            last = word[-1]
            if last in VOWEL_ALPHABET:
                if random.random() < P_AFTER_VOWEL_CONSONANT:
                    word += weighted_choice(CONSONANT_ALPHABET, CONSONANT_WEIGHTS)
                else:
                    word += weighted_choice(VOWEL_ALPHABET, VOWEL_WEIGHTS)
            else:
                if random.random() < P_AFTER_CONSONANT_VOWEL:
                    word += weighted_choice(VOWEL_ALPHABET, VOWEL_WEIGHTS)
                else:
                    word += weighted_choice(CONSONANT_ALPHABET, CONSONANT_WEIGHTS)
        
        words.append(''.join(word))
        
    return words

words = generate_weighted_words(WORDS_COUNT, MINIMUM_WORD_LENGTH, MAX_WORD_LENGTH)

some_string = ''

for word in words:
    some_string += f'{word}'
    
    random_punctuation_mark_value = random.randint(0, 2) # 1 / 4
    
    if random_punctuation_mark_value == 1:
        some_string += weighted_choice(PUNCTUATION_MARK_ALPHABET, PUNCTUATION_MARK_WEIGHTS)
    
    some_string += ' '
    
some_string = some_string[:-2]
some_string += '.'
    
print(f'Некоторый текст: {some_string}')

sorted_string = ''


for i in some_string:
    if not (i in PUNCTUATION_MARK_ALPHABET):
        sorted_string += i
        
sorted_list = sorted_string.split()

list_of_words_ended_with_OV = []

for word in sorted_list:
    if word[-2:] == 'ОВ':
        list_of_words_ended_with_OV.append(word) 
        
print(f'Слова, заканчивающиеся на "ОВ" {list_of_words_ended_with_OV}.')