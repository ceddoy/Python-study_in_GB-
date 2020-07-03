print("Добро пожаловать в мясную лаву Tony!")
print("*" * 60)
assortment_meat = []
num = 1
an_dict = {"название": [], "цена": [], "вес": [], "ед": []}
while True:
    print("Если хотите сформировать товар, то наберите 'добавить'\n"
          "Если хотите провести аналитику, то наберите 'аналитика'")
    print("Если хотите заглянуть в холодильник, то наберите 'холодильник'")
    print("*" * 60)
    print("Для выхода наберите 'q'")
    user_answer = input("Что вы хотите сделать: ").lower()
    if user_answer == "q":
        print("Выход из программы.")
        break
    elif user_answer == "добавить":
        meat_name = input(f"Введите название {num} товара: ")
        measure_unit = input(f"В какой единице измерения вы хотите считать {meat_name}(у): ")
        meat_price = float(input(f"Какая будет цена {meat_name}(и/ы) за {measure_unit}: "))
        storage = float(input(f"Сколько у вас {measure_unit} {meat_name}(и/ы) хранится в холодильнике: "))
        meat = (num, {"название": meat_name, "цена": meat_price, "вес": storage, "ед": measure_unit})
        print("*" * 60)
        print(f" Вы добавили в холодильник:{meat}")
        print("*" * 60)
        num += 1
        assortment_meat.append(meat)
        an_dict["название"].append(meat_name)
        an_dict["цена"].append(meat_price)
        an_dict["вес"].append(storage)
        an_dict["ед"].append(measure_unit)
        an_dict["ед"] = list(set(an_dict["ед"]))
    elif user_answer == "холодильник":
        print("*" * 60)
        print(f"В вашем холодильнике хранятся:\n{assortment_meat}")
        print("*" * 60)
    elif user_answer == "аналитика":
        print("*" * 60)
        print(an_dict)
        print("*" * 60)
