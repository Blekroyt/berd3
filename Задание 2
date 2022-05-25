#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
import sys

if __name__ == '__main__':
    tr1_1 = int(input("x1 точка треугольника"))
    tr1_2 = int(input("y1 точка треугольника"))
    tr2_1 = int(input("x2 точка треугольника"))
    tr2_2 = int(input("y2 точка треугольника"))
    tr3_1 = int(input("x3 точка треугольника"))
    tr3_2 = int(input("y3 точка треугольника"))
    t1 = int(input("x точки"))
    t2 = int(input("y точки"))
    S = 0.5 * abs((tr1_1 - tr2_1) * (tr3_2 - tr2_2) - (tr3_1 - tr2_1) * (tr1_2 - tr2_2))
    S1 = 0.5 * abs((tr1_1 - t1) * (tr3_2 - t2) - (tr3_1 - t1) * (tr1_2 - t2))
    S2 = 0.5 * abs((tr1_1 - t1) * (tr2_2 - t2) - (tr2_1 - t1) * (tr1_2 - t2))
    S3 = 0.5 * abs((tr2_1 - t1) * (tr3_2 - t2) - (tr3_1 - t1) * (tr2_2 - t2))
    if S == S1 + S2 + S3:
        print("Да")
    else:
        print("Нет")
