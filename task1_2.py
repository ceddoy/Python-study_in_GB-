seconds = int(input("Введите желаемое количество секунд: "))
hh = seconds // 3600
print(hh)
mm = (seconds // 60) % 60
print(mm)
ss = seconds % 60
print(ss)
if hh < 10:
    hh = (f"0{hh}")
if mm < 10:
    mm = (f"0{mm}")
if ss < 10:
    ss = (f"0{ss}")

print(f"{hh}:{mm}:{ss}")
