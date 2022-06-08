#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
import sys

if __name__ == '__main__' :

    day = int(input("Введите день: "))
    if day > 0 and 31 >= day:
        m = 1

    elif day > 31 and 59 >= day:
        m = 2

    elif day > 59 and 90 >= day:
        m = 3

    elif day > 90 and 120 >= day:
        m = 4

    elif day > 120 and 151 >= day:
        m = 5

    elif day > 151 and 181 >= day:
        m = 6

    elif day > 181 and 212 >= day:
        m = 7

    elif day > 212 and 243 >= day:
        m = 8

    elif day > 243 and 273 >= day:
        m = 9

    elif day > 273 and 304 >= day:
        m = 10

    elif day > 304 and 334 >= day:
        m = 11

    elif day >= 334 and 366 >= day:
        m = 12
    else:
        print("ошибочка.")
        exit(1)
    if m==1 :
        Dy=day-0
        print(f"{Dy} января")
    if m==2 :
        Dy=day-31
        print(f"{Dy} февраля")
    if m==3 :
        Dy=day-59
        print(f"{Dy} марта")
    if m==4 :
        Dy=day-90
        print(f"{Dy} апреля")
    if m==5 :
        Dy=day-120
        print(f"{Dy} мая")
    if m==6 :
        Dy=day-151
        print(f"{Dy} июня")
    if m==7 :
        Dy=day-181
        print(f"{Dy} июля")
    if m==8 :
        Dy=day-212
        print(f"{Dy} августа")
    if m==9 :
        Dy=day-243
        print(f"{Dy} сентября")
    if m==10 :
        Dy=day-273
        print(f"{Dy} октября")
    if m==11:
        Dy=day-304
        print(f"{Dy} ноября")
    if m==12:
        Dy=day-334
        print(f"{Dy} декабря")
