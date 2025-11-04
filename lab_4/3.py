# Сгенерируйте и выведите:
# Случайную строку, состоящую из 8 символов и содержащую цифры и буквы.
# Строка должна содержать хотя бы одну цифру.

import random

LETTER_ALPHABET = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З',
           'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р',
           'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ',
           'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']

NUMBER_ALPHABET = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

for _ in range(10):
    some_string = ''

    for i in range(8):
        some_string += LETTER_ALPHABET[random.randint(0, len(LETTER_ALPHABET) - 1)]
        
    for _ in range(3):
        random_number = NUMBER_ALPHABET[random.randint(0, len(NUMBER_ALPHABET) - 1)]
        random_index = random.randint(0, len(some_string) - 1)    

        some_string = some_string[:random_index] + random_number + some_string[random_index + 1:]

    print(some_string)