import re

filename = 'task_add.txt'
with open(filename, 'r', encoding='utf-8') as file:
    content = file.read()

dates = re.findall(r'\b(\d{2,4}[./-]\d{2,4}[./-]\d{2,4})', content)
emails = re.findall(r'\s([\w.%+-]+@[\w.-]+\.[a-zA-Z]{2,})', content)
urls = re.findall(r'\s(https?://[a-zA-Z0-9.-]+)', content)

found_dates = dates[:5]
found_emails = emails[:5]
found_urls = urls[:5]

print("Найденные даты:", found_dates)
print("Найденные адреса электронной почты:", found_emails)
print("Найденные адреса сайтов:", found_urls)