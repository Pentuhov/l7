#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# import sys

if __name__ == '__main__':
    a = tuple(map(int, input("Введите список: ").split()))
    if a.count(0) < 2:
        print('Не хватает нулевых элементов')
    x1 = x2 = -1
    amax = a[0]
    indmax = 0
    for i in range(len(a)):
        if amax < a[i]:
            amax = a[i]
            indmax = i
        if a[i] == 0:
            if x1 == -1:
                x1 = i
            elif x2 == -1:
                x2 = i
        if x1 != -1 and x2 != -1:
            break
    m = 1
    for i in range(x1 + 1, x2):
        m *= a[i]
    print("Произведение элементов списка, расположенных между первым и вторым"
          " нулевыми элементами равно:", m)
    b = []
    for i in range(len(a)):
        if i % 2 == 0:
            b.append(a[i])
    for i in range(len(a)):
        if i % 2 == 1:
            b.append(a[i])
    print(*b)