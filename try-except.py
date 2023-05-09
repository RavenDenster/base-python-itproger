x = 0
while x == 0:
    try:
        x = int(input('Введите число: '))
        x += 5
        print(x)
    except ValueError:
        print('Введите лучше число!')
    except ZeroDivisionError:
        print('деление на ноль!')
    else:
        print('else')
    finally:
        print('end')


try:
    with open('text.txt', 'r', encoding='utf-8') as file:
        print(file.read())
except FileNotFoundError:
    print('Файл не найден')