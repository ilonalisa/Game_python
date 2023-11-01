import sys_exit
users = {
    "ID": 14,
    "прізвище": "Лиса",
    "Ім’я": "Ілона",
    "Група": "ІПЗс-23-2",
    "Курс": 1,
    "Книги (борг)": [],
    "Статистика книг": []
}

while True:
    print("Оберіть опцію:")
    print("1 - Вивести карту читача")
    print("2 - Взяти книгу")
    print("3 - Повернути книгу")
    print("0 - Вихід")
    
    option = input()
    
    if option == "1":
        print("Карта читача:")
        for key, value in users.items():
            print(key + ": " + str(value))
            
    elif option == "2":
        book = input("Введіть назву книги: ")
        users["Книги (борг)"].append(book)
        print("Книга успішно додана у борг.")

    elif option == "3":
        if len(users["Книги (борг)"]) == 0:
            print("Немає книг у боргу.")
        else:
            print("Книги у боргу:")
            for book in reader["Книги (борг)"]:
                print(book)
                
            book = input("Введіть назву книги, яку хочете повернути: ")
            if book in users["Книги (борг)"]:
                users["Книги (борг)"].remove(book)
                users["Статистика книг"].append(book)
                print("Книга успішно повернута.")
            else:
                print("Книга не знайдена у списку боргу.")
                
    elif option == "0":
        sys_exit
        
    else:
        print("Невірна опція. Спробуйте ще раз.")


