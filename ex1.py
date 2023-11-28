# !/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    vowel = set("ауоиэыяюеё")
    user_input = input("Введите текст: ")
    c = len([i for i in user_input.lower() if i in vowel])

    # c = 0
    # for i in user_input.lower():
    #     if i in user_input:
    #         c += 1

    print(f"Количество гласных букв = {c}")
