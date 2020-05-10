i = 0
while i == 0:
    print('Введите два положительных числа')
    a = int(input())
    b = int(input())
    if (a < 0) and (b > 0):
        print('Первое число отрицательное попробуй ещё')
    if (a > 0) and (b < 0):
        print('Второе число отрицательное')
    if (a < 0) and (b < 0):
        print('Оба числа отрицательные')
    if (a > 0) and (b > 0):
        print('Молодец оба числа правильные')
        print(a)
        print(b)
        i = 1
suma: int = (a + b)
print(f'Сумма введёнеых чисел равна: {suma}')
dif: int = (a - b)
print(f'Вычитание чисел дало результат:{dif}')