# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# 14 вариант

if __name__ == "__main__":
    u = set("abcdefghijklmnoprqrstuvwxyz")

    a = {"c", "m", "n", "o", "q"}
    b = {"c", "d", "m", "w"}
    c = {"m", "n", "q"}
    d = {"c", "m", "p"}

    x = (a.union(b)).intersection(c)

    an = u.difference(a)
    y = (an.intersection(d)).union(c.difference(b))

    print(f"x = {x}")
    print(f"y = {y}")
