import re
import csv

filename = 'task3.txt'
with open(filename, 'r', encoding='utf-8') as file:
    content = file.read()

surnames = re.findall(r'[A-Z][a-z]+(?!\d\d@|@)', content)
content = re.sub(r'[A-Z][a-z]+(?!\d\d@|@)', ' ', content)
emails = re.findall(r'[a-z][a-z0-9-]*@[a-z0-9-]+\.[a-z]{2,}', content)
dates = re.findall(r'\d{4}-\d{2}-\d{2}', content)
sites = re.findall(r'https?://[a-zA-Z0-9.-]+/', content)
content = re.sub(r'https?://[a-zA-Z0-9.-]+/', ' ', content)

# Для корректного вывода ID-номера
ids = list(range(1, min(len(surnames), len(emails), len(dates), len(sites)) + 1))

new_content = [
    [ids[i], surnames[i], emails[i], dates[i], sites[i]]
    for i in range(len(ids))
]

csv_filename = 'normalized_data.csv'
with open(csv_filename, 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['ID', 'Фамилия', 'Электронная почта', 'Дата регистрации', 'Сайт'])
    csv_writer.writerows(new_content)

print(f"Данные сохранены в {csv_filename}")