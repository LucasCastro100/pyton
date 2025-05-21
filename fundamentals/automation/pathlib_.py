from pathlib import Path

file_1 = Path('files', 'a.txt')

# print(file_1)
# print(type(file_1))
# print(file_1.name)
# print(file_1.stem)
# print(file_1.suffix)
# print(file_1.parent)
# print(file_1.exists())

if file_1.exists():
    with open(file_1, 'r', encoding='utf-8') as file:
        print(file.read())