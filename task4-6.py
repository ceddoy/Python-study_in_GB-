class Warehouse:
    warehouse = []
    divisions_lawyers = []
    accounting_department = []
    divisions_HR = []

    @staticmethod
    def show_warehouse():
        for i, goods in enumerate(Warehouse.warehouse):
            print(f"{i + 1}) {goods}")


class OfficeEquipment:
    office_equipment = []
    def __init__(self, name, model, price, count):
        self.name = name
        self.model = model
        self.price = price
        self.count = count

    @staticmethod
    def move_warehouse():
        Warehouse.warehouse.extend(OfficeEquipment.office_equipment)

    @staticmethod
    def del_goods():
       OfficeEquipment.office_equipment.remove()

class Printer(OfficeEquipment):
    def __init__(self, name, model, price, count, printing_technology):
        super().__init__(name, model, price, count)
        self.printing_technology = printing_technology
        OfficeEquipment.office_equipment.append({"Наименование": self.name,
                        "Модель": self.model,
                        "Цена": self.price,
                        "Количество": self.count,
                        "Технология печати": self.printing_technology})


class Scanner(OfficeEquipment):
    def __init__(self, name, model, price, count, type_scanner):
        super().__init__(name, model, price, count)
        self.type_scanner = type_scanner
        OfficeEquipment.office_equipment.append({"Наименование": self.name,
                                    "Модель": self.model,
                                    "Цена": self.price,
                                    "Количество": self.count,
                                    "Тип сканера": self.type_scanner})


class Xerox(OfficeEquipment):
    def __init__(self, name, model, price, count, type_xerox):
        super().__init__(name, model, price, count)
        self.type_xerox = type_xerox
        OfficeEquipment.office_equipment.append({"Наименование": self.name,
                                    "Модель": self.model,
                                    "Цена": self.price,
                                    "Количество": self.count,
                                    "Тип ксерокса": self.type_xerox})


procurement_1 = Xerox("Conen", "STRONG2000", 15999, 15, "МФЦ")
procurement_2 = Printer("Ph", "HD-4k", 24799, 20, "Лазерный")
OfficeEquipment.move_warehouse()
Warehouse.show_warehouse()



