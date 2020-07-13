with open("new_text.txt", "w+", encoding="utf-8") as text_file:
    while True:
        text = input("Введите желаемый текст: ")
        if text:
            text += "\n" # Так я создаю строчку после каждого ввода
            text_file.write(text)
            print(text_file.read())
        elif not text:
            break
