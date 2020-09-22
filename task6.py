def init_func(txt):
    return txt.title()


def init_func2(txt):
    new_words = []
    txt = txt.split()
    for word in txt:
        new_letter = chr(ord(word[0]) - 32)
        new_word = new_letter + word[1:]
        new_words.append(new_word)
    return " ".join(new_words)


text = input("Введите текст: ")
print(init_func(text))

print("*" * 50)
print("Решение через chr()")

print(init_func2(text))
