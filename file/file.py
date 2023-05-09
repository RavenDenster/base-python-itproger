data = input('введите текст: ')

file = open('./text.txt', 'a')  # w - вся информация перезаписывается, a - информация добавляется, r - считать файл

# file.write('Hey!\n')
# file.write('!!!')
file.write(data + '\n')

file.close()


file2 = open('../file/text.txt', 'r')

# print(file2.read(5))
for line in file2:
    print(line, end='')

file2.close()