##Подсчет числа Фмбоначчи в пределах числа n
n = int(input('Введите предел суммы чисел Фибоначчи:'))
sum = 0
a = 1
count = -1
while n >= sum + a:
    sum += a
    a = sum - a
    count += 1        
print('Число Фебоначчи равно:', count)
print('Сумма чисел равна:', sum)