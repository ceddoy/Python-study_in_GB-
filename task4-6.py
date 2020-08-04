class Divisions:
    pass

class HR(Divisions):
    divisions_HR = []
    @staticmethod
    def show_org():
        for i, goods in enumerate(HR.divisions_HR):
            print(f"{i + 1}) {goods}")
    def in_warehouse(self):
        pass

class Warehouse:
    warehouse = []
    @staticmethod
    def in_division(name, count):
        for el in Warehouse.warehouse:
            for key, val in el.items():
                if name == val:
                    if count <= el["Количество"]:
                        el["Количество"] = count
                        HR.divisions_HR.append(el)
                        Warehouse.del_count_goods(name, count)
                        return print(f'Позиция: {name}, кол-во: {count} перемещена в подзразделение')
                    else:
                        return print('Такого количества нет на складе')
                return print('Такого товара нет на складе')

    @staticmethod
    def del_count_goods(name, count):
        for el in Warehouse.warehouse:
            for key, val in el.items():
                if name == val:
                    el["Количество"] -= count
                    if el["Количество"] == 0:
                        Warehouse.warehouse.remove(el)

    @staticmethod
    def show_warehouse():
        for i, goods in enumerate(Warehouse.warehouse):
            print(f"{i + 1}) {goods}")

    @staticmethod
    def show_about_goods(good):
        for i, goods in enumerate(good.out_inf().values()):
            print(f"{i + 1}) {goods}")


class OfficeEquipment:
    office_equipment = []
    def __init__(self, name, model, price, count):
        self.name = name
        self.model = model
        self.price = price
        self.count = count

    @staticmethod
    def move_warehouse(org):
        Warehouse.warehouse.append(org)


class Printer(OfficeEquipment):
    def __init__(self, name, model, price, count, printing_technology):
        super().__init__(name, model, price, count)
        self.printing_technology = printing_technology

    def out_inf(self):
        return dict({"Наименование": self.name,
                     "Модель": self.model,
                     "Цена": self.price,
                     "Количество": self.count,
                     "Технология печати": self.printing_technology})


class Scanner(OfficeEquipment):
    def __init__(self, name, model, price, count, type_scanner):
        super().__init__(name, model, price, count)
        self.type_scanner = type_scanner

    def out_inf(self):
        return dict({"Наименование": self.name,
                     "Модель": self.model,
                     "Цена": self.price,
                     "Количество": self.count,
                     "Тип сканера": self.type_scanner})


class Xerox(OfficeEquipment):
    def __init__(self, name, model, price, count, type_xerox):
        super().__init__(name, model, price, count)
        self.type_xerox = type_xerox

    def out_inf(self):
        return dict({"Наименование": self.name,
                     "Модель": self.model,
                     "Цена": self.price,
                     "Количество": self.count,
                     "Тип ксерокса": self.type_xerox})


procurement_1 = Xerox("Conen", "STRONG2000", 15999, 15, "МФЦ")
procurement_2 = Printer("Ph", "HD-4k", 24799, 20, "Лазерный")
OfficeEquipment.move_warehouse(procurement_1.out_inf())
Warehouse.show_warehouse()
hr = HR()
Warehouse.in_division("Conen", 5)
hr.show_org()
Warehouse.show_warehouse()



