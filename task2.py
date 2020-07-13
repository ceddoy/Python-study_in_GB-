lines = 0
"""Создаю переменные для подсчета строк (lines) и слов (words)
Скрипт очень короткий, и уверен, что понятный"""
for line in open("text_2.txt", "r", encoding="utf-8"):
    words = 0
    lines += 1
    for word in line.split():
        words += 1
    print(f"{lines} cтрока - количество слов: {words}")

