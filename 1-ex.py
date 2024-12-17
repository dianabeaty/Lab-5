import re

filename = 'task1-ru.txt'

with open(filename, 'r', encoding='utf-8') as file:
    content = file.read()

figures = re.findall(r'(рис\. \d+|Fig\. \d+)', content)

four_letter_words = re.findall(r'\b\w{4}\b', content)

print("Конструкции 'рис. #' или 'Fig. #':")
print(figures)

print("\nСлова из 4 букв:")
print(four_letter_words)