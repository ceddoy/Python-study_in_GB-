user_input = list(input("Введите несколько строк через пробел: ").split())
print(user_input)
for num, string in enumerate(user_input, 1):
    print(f"{num}) {string:.10s}")
