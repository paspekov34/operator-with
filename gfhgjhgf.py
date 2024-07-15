import io
from pprint import pprint

name = 'test_file.txt'

# Пишем в файл
with open(name, 'w', encoding='utf-8') as file:
    file.write("It's a TEXT for task Найти везде,\n")
    file.write("Используйте его для самопроверки.\n")
    file.write("Успехов в решении задачи!\n")
    file.write("text, text, text\n")

# Читаем из файла
with open(name, encoding='utf-8') as file:
    content = file.read()
    print(content)

