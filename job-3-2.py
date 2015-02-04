#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
 ПРАКТИЧНЕ ЗАВДАННЯ №3.2
(2 можливих балів)

Програма має розраховувати числа послідовності Фібоначчі. Послідовність Фібоначчі -- це послідовність чисел, в якій кожний елемент дорівнює сумі двох попередніх. При цьому нульовий елемент вважається за 0, а перший 1. Отже, сама послідовність виглядає наступним чином:
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, …

Вхідні дані: ціле невід'ємне число n. Передається в програму як аргумент командного рядка.

Результат роботи: значення n-го числа послідовності Фібоначчі.

Будь ласка, не використовуйте рекурсію.

Наприклад
Вхідні дані: 0
Результат: 0
Вхідні дані: 10
Результат: 55
"""

import sys
a=int(sys.argv[1])
l=range(2)
z=0
if a > 0:
	while z <= a-1:
		l2=l[-1]+l[-1-1]
		l.append(l2)
		z=z+1
	print l[-1-1]

elif a == 0:
	print l[-1-1]

