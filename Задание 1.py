#!/usr/bin/env python3
# -*- кодировка: utf-8 -*-
import math
import sys

if __name__ == '__main__':
    n = int(input("n = "))
    if n > 20:
        print("Ошибка", file=sys.stderr)
        exit(1)
    if n == 1:
        b = " экзаменов"
    elif n <= 20:
        b = " экзаменов"
    else:
        b = " экзаменов"
    print("Мы успешно сдали ", n, b)
