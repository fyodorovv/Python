import function

def start_menu():
    print("Посмотеть все контакты [1]: ")
    print("Найти контакт [2]: ")
    print("Добавить контакт [3]: ")
    print("Импорт контактов [4]: ")
    print("Экспорт контактов [5]: ")
    choice = int(input("Выберете действие: "))
    print("---------------------------------------")


    if choice == 1:
        function.read()

    elif choice == 2:
        data_request = str(input("Введите данные: ")).title()
        function.find_contact(data_request)

    elif choice == 3:
        family = input("Введите фамилию: ")
        name = input("Введите имя: ")
        number = input("Введите номер: ")
        description = input("Введите описание: ")
        function.create_contart(family, name, number, description)

    elif choice == 4:
        filename = input("Введите название файла csv: ")
        function.import_contacts(filename)

    elif choice == 5:
        expt = input("Введите названия файла для экспорта: ")
        function.export_contact(expt)
