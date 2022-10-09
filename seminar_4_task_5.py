# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов. 2*x² + 4*x + 5  3*x² +10*x + 6 Вывод: 5*x² + 14*x + 11

import sympy

x = sympy.Symbol('x')
with open("path1.txt", 'r') as path1:
    a = path1.read()
print(a)

with open("path2.txt", 'r') as path2:
    b = path2.read()
print(b)

c = sympy.simplify(a+'+'+b)

with open("sum=path1+path2.txt", 'w') as f:
    f.write(str(c))

print(c)