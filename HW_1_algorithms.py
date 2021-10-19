# 1.Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

a = input('Введите трехзначное число')
match list(a):
    case a1, a2, a3:
        print(int(a1) + int(a2) + int(a3))
        print(int(a1) * int(a2) * int(a3))
    case _:
        print('Вы ввели неверное значение.')


# 2. Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6.
# Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака.
# Объяснить полученный результат.
print(f'{bin(5)=}, {bin(6) = }')
print(5 & 6)
print(5 | 6)
print(5 ^ 6)
print(5 >> 2, 5 << 2 )

# 3. По введенным пользователем координатам двух точек вывести уравнение
# прямой вида y=kx+b, проходящей через эти точки.

x1, y1 = float(input('Введите значение Х1: ')), float(input('Введите значение Y1: '))
x2, y2 = float(input('Введите значение Х2: ')), float(input('Введите значение Y2: '))


print("Уравнение прямой, проходящей через эти точки:")
k = (y1 - y2) / (x1 - x2)
b = y2 - k*x2
print(f'y = {k} * x + {b} ')

# 4. Написать программу, которая генерирует в указанных пользователем границах:
# случайное целое число;
# случайное вещественное число;
# случайный символ.

from random import randrange, randint, uniform, choice, triangular

print(randrange(10,50))
print(triangular(10,50))
print(choice([chr(i) for i in range(ord('a'), ord('v'))]))

#5. Пользователь вводит две буквы. Определить,
# на каких местах алфавита они стоят и сколько между ними находится букв.
chars = 'abcdefghijklmnopqrstuvwxyz'

char_range = input('Введите диапазон символов от a до z в формате x,y: ').split(',')
print(char_range)
a = chars.index(char_range[0]) + 1
b = chars.index(char_range[1]) + 1

c = b - a

print('Первая буква: {} - находится на {} позиции,\
      вторая буква {} - находится на {} позиции.\
      Расстояние между ними {}'.format(char_range[0], a, char_range[1], b, c))



#6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

abc_number = int(input('Введите номер буквы в алфавите: '))

# Генерация списка букв
abc_list = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
print(abc_list)
if abc_number <= len(abc_list):
    print(f'Буква под номером {abc_number}: {abc_list[abc_number - 1]}')
else:
    print(
      f'Введено число превышающее количество букв в алфавите ({len(abc_list)})'
    )

#7 По длинам трех отрезков, введенных пользователем, определить возможность
# существования треугольника, составленного из этих отрезков. Если такой
# треугольник существует, то определить, является ли он разносторонним,
# равнобедренным или равносторонним.'''

a, b, c = [
      float(x) for x in input('Введите длины отрезков, через пробел: ').split()
        ]

if a < b + c and b < a + c and c < a + b:
    if a == b and b == c:
        print(f'Треугольник со сторонами {a} {b} {c} - равносторонний')
    elif a == b or b == c or c == a:
        print(f'Треугольник со сторонами {a} {b} {c} - равнобедренный')
    else:
        print(f'Треугольник со сторонами {a} {b} {c} - разносторонний')
else:
    print(f'Треугольника со сторонами {a} {b} {c} не существует')

#8. Определить, является ли год, который ввел пользователем, високосным или невисокосным.

'''-- год, номер которого кратен 400, — високосный;
-- остальные годы, номер которых кратен 100, — невисокосные;
-- остальные годы, номер которых кратен 4, — високосные.'''

year = int(input('Введите год: '))

if year % 400 == 0:
    print(f"Год {year} високосный")
elif year % 100 == 0 and year % 400 != 0:
    print(f"Год {year} невисокосный")
elif year % 4 == 0:
    print(f"Год {year} високосный")
else:
    print(f"Год {year} невисокосный")

#9. Вводятся три разных числа. Найти, какое из них является средним (
# больше одного, но меньше другого).

n1, n2, n3 = [x for x in input('Введите три числа, через пробел: ').split()]

if n2 < n1 < n3 or n3 < n1 < n2:
    print(f'Среднее: {n1}')
elif n1 < n2 < n3 or n3 < n2 < n1:
    print(f'Среднее: {n2}')
else:
    print(f'Среднее: {n3}')