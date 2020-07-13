import json

dict_firm = {}  # словарь с фирмами
average_profit = {}  # словь со средней прибылью
list_firm_estimate = []  # в этом списке, я буду объединять вышеуказанные словари
profit = 0
i = 0  # Счетчик фирм
with open("text_7.txt", "r", encoding="utf-8") as file_firm:
    for line in file_firm.readlines():
        name, firm, revenue, cost = line.split()
        name = name + " " + firm  # Объединяю название с правовой формой
        dict_firm[name] = int(revenue) - int(cost)
        if dict_firm.setdefault(name) >= 0:
            profit += dict_firm.setdefault(name)
            i += 1
    average_profit["averge_profit"] = profit / i
    list_firm_estimate.append(dict_firm)  # Объединяю в 1 список словарь с фирмами и со средней прибылью
    list_firm_estimate.append(average_profit)
    print(f"Итоговый список:\n{list_firm_estimate}")

with open('file_7.json', 'w', encoding="utf-8") as write_js:
    json.dump(list_firm_estimate, write_js)

    js_str = json.dumps(list_firm_estimate)
    print(f'Создан файл с расширением json со следующим содержимым:\n{js_str}')