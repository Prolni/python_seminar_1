# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

from decimal import Decimal

digit = Decimal(input('Введите дробное число: '))
digit = digit.quantize(Decimal(input('Введите степень кругления, например: 0.001 - ')))
print('Итог:', digit)