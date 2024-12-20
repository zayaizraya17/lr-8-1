import json

count = 0


def save_flowers(flowers, filename="dump.json"):
    with open(filename, "w", encoding='utf-8') as f:
        json.dump(flowers, f, indent=4, ensure_ascii=False)

def print_all_flowers(flowers):
    if not flowers:
        print("Нет записей о цветах.")
        return
    for flower in flowers:
        print(f"""Номер цветка: {flower["id"]} 
    Название: {flower["name"]}
    Латинское название: {flower["latin_name"]}
    Краснокнижный цветок? {flower["is_red_book_flower"]}
    Цена: {flower["price"]} BYN\n""")

def print_flower_by_id(flowers, flower_id):
    for i, flower in enumerate(flowers):
        if flower['id'] == flower_id:
            print(f"""Номер цветка: {flower["id"]} 
    Название: {flower["name"]}
    Латинское название: {flower["latin_name"]}
    Краснокнижный цветок? {flower["is_red_book_flower"]}
    Цена: {flower["price"]} BYN\n""")
            return
    print(f"Запись с ID {flower_id} не найдена.")

def add_flower(flowers):
    flower_id = max(flower["id"] for flower in flowers) + 1

    while True:
            name = input("Введите названия цветка ")
            if name != "":
                break
            else:
                print("Вы не ввели")

    while True:
        latin_name = input("Введите латинское имя цветка ")
        if latin_name != "":
            break
        else:
            print("Вы не ввели")

    while True:
        is_red_book_flower = input("Введите краснокнижный ли цветок True/False ")
        if is_red_book_flower.lower() in ["true", "false"]:
            is_red_book_flower = is_red_book_flower.lower() == "true"
            break
        else:
            print("Некорректный ввод")

    while True: 
        try: 
            price = float(input("Введите цену цветка ")) 
            break 
        except ValueError: 
            print("Некорректный ввод") 

    flowers.append({
        "id": flower_id,
        "name": name,
        "latin_name": latin_name,
        "is_red_book_flower": is_red_book_flower,
        "price": price
    })
    print("Запись добавлена.")

def delete_flower_by_id(flowers, flower_id):
    for i, flower in enumerate(flowers):
        if flower['id'] == flower_id:
            del flowers[i]
            print(f"Запись с ID {flower_id} удалена.")
            return
    print(f"Запись с ID {flower_id} не найдена.")

def main():
    with open('dump.json', 'r', encoding='utf-8') as file:
        flowers = json.load(file)
    count = 0
    while True:
        print("\nМеню:")
        print(" 1 Вывести все записи\n 2 Вывести запись по полю\n 3 Добавить запись\n 4 Удалить запись по полю\n 5 Выйти из программы")

        choice = input("Что выберете? ")
        if choice == "1":
            print_all_flowers(flowers)
            count += 1
        elif choice == "2":
            flower_id = int(input("Введите ID записи: "))
            print_flower_by_id(flowers, flower_id)
            count += 1
        elif choice == "3":
            add_flower(flowers)
            count += 1
        elif choice == "4":
            flower_id = int(input("Введите ID записи для удаления: "))
            delete_flower_by_id(flowers, flower_id)
            count += 1
        elif choice == "5":
            print(f"Выполнено операций: {count}")
            break
        else:
            print("Неверный выбор.")
        save_flowers(flowers)

main()

