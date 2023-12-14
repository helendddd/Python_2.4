#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Составить программу с использованием одномерных массивов
# для решения задачи на переупорядочивание элементов массива.
# Для сортировки допускается использовать метод sort с заданным
# параметром key и объединение нескольких списков.

# В списке, состоящем из вещественных элементов, вычислить:
# 1. максимальный элемент списка;
# 2. сумму элементов, расположенных до последнего положительного элемента.

import sys

if __name__ == "__main__":
    A = list(map(float, input("Enter list ").split()))

    if len(A) == 0:
        print("The list is empty!", file=sys.stderr)
        exit(1)

    sum = 0
    a_max = float('-inf')

    for i in A:
        if i > a_max:
            a_max = i

    for i in A:
        if i > 0:
            sum += i
        else:
            break

    print(f"Sum of first positive elements is {sum}.")
    print(f"Max element is {a_max}.")
