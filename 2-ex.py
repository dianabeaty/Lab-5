import re

filename = 'task2.html'

with open(filename, 'r', encoding='utf-8') as file:
    content = file.read()

font_parameters = re.findall(r'font-style:\s*([^;]+);|font-weight:\s*([^;]+);', content)

styles = []
weights = []

for style, weight in font_parameters:
    if style:
        styles.append(style.strip())
    if weight:
        weights.append(weight.strip())

print("Используемые стили шрифтов:")
print(*set(styles))
print("\nИспользуемые размеры шрифтов:")
print(*set(weights))