def custom_write(file_name, strings):
    file = open(file_name, 'a', encoding='utf-8')
    strings_positions = dict()
    string = 1
    for i in strings:
        position = file.tell()
        file.write(i)
        file.write('\n')
        strings_positions[(string, position)] = i
        string += 1
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)