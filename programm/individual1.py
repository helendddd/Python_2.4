#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Ввести список А из 10 элементов, найти сумму элементов,
# больших 3 и меньших 8 и вывести ее на экран.

import sys

if __name__ == "__main__":
    A = list(map(int, input("Введите список из 10 элементов... ").split()))

    if len(A) != 10:
        print("Неверный размер списка", file=sys.stderr)
        exit(1)

    s = sum([a for a in A if a > 5 and a < 8])
    print(s)
