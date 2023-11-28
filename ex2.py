# !/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    str1 = set(input("Введите первую строку: "))
    str2 = set(input("Введите вторую строку: "))

    print(
        f"Общие символы в введенных строках {str1.intersection(str2)}"
    )
