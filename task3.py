with open("text_3.txt", "r", encoding="utf-8") as lines:
    list_worker_salaryLess_20 = []  # Список сотрудников, зарабатывающих меньше 20 тыс. руб.
    total_salary_amount = []  # Список зарплат всех сотрудников
    """Каждую строку интерпретирую в список и работаю с индексами"""
    for line in lines.read().split("\n"):
        line = line.split()
        if float(line[1]) < 20000:
            list_worker_salaryLess_20.append(line[0])
        total_salary_amount.append(line[1])
print("Список сотрудников, зарабатывающих меньше 20 тыс. руб.:")
print('\n'.join(list_worker_salaryLess_20))
print(f"Средний заработок всех сотрудников составляет: {sum(map(float, total_salary_amount)) / len(total_salary_amount)} руб.")