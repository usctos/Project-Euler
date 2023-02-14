## Программа для подсчета суммы чисел кратных 3 и 5 из числа n
n = int(input('Ввведите число:'))
a = 3
b = 5
sum = 0

for i in range(n):
    if i % a == 0:
        sum += i    
for i in range(n):
    if i % b == 0:
        sum += i
print(sum)