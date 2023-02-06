import csv


def start():
    phone_book_list = []
    with open('phone_book.csv', newline='') as f:
        reader = csv.reader(f, delimiter=";")
        for line in reader:
            phone_book_list.append(line)
    return phone_book_list


def read():
    phone_book_list = start()
    for row in phone_book_list:
        print(" ".join(row))


def create_contart(family, name, number, description):
    data_cont = [family, name, number, description]
    with open('phone_book.csv', 'a', newline='') as f:
        phone_book = csv.writer(f, delimiter=";")
        phone_book.writerow(data_cont)
    print('Контакт добавлен!')
    read()


def find_contact(data_request):
    find = " "
    phone_book_list = start()
    for i in range(len(phone_book_list)):
        for j in range(len(phone_book_list[i])):
            if data_request in phone_book_list[i][j]:
                find = phone_book_list[i]
    if find == " ":
        print("Не найденно")
    else:
        print(" ".join(find))


def import_contacts(filename):
    import_list = []
    filename += '.csv'
    with open(filename, newline='') as f:
        reader = csv.reader(f, delimiter=";")
        for line in reader:
            import_list.append(line)

    for item in import_list:
        with open('phone_book.csv', 'a', newline='') as f:
            phone_book = csv.writer(f, delimiter=";")
            phone_book.writerow(item)
    print("Импорт успешно выполнен!")
    print("---------------------------------------")
    read()


def export_contact(expt):
    expt += ".csv"
    export_list = start()
    with open(expt, 'w', newline='') as f:
        writer = csv.writer(f, delimiter=";")
        for row in export_list:
            writer.writerow(row)
    print("Экспорт успешно выполнен!")
