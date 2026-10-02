# Базовий словник: Ключ - № багажу, Значення - словник {"count": кількість_речей, "weight": вага}
luggage_db = {
    "P1": {"count": 3, "weight": 45.0},
    "P2": {"count": 1, "weight": 18.5},
    "P3": {"count": 2, "weight": 22.0},
    "P4": {"count": 4, "weight": 50.0},
    "P5": {"count": 1, "weight": 30.0},
    "P6": {"count": 3, "weight": 36.0},
    "P7": {"count": 2, "weight": 15.0},
    "P8": {"count": 5, "weight": 60.0},
    "P9": {"count": 1, "weight": 12.0},
    "P10": {"count": 2, "weight": 28.0}
}

def print_all(db):
    """Виведення усіх значень словника"""
    if not db:
        print("Словник порожній.")
        return
    print("\n--- Вміст словника багажу ---")
    for key, data in db.items():
        print(f"Пасажир (№ багажу): {key:5} | Кількість речей: {data['count']:2} | Загальна вага: {data['weight']:5.1f} кг")

def add_entry(db):
    """Додавання нового запису"""
    key = input("Введіть номер багажу (ключ): ").strip()
    if key in db:
        print("Помилка: Запис із таким ключем вже існує!")
        return
    try:
        count = int(input("Введіть кількість речей: "))
        weight = float(input("Введіть загальну вагу (кг): "))
        if count <= 0 or weight <= 0:
            raise ValueError("Кількість речей та вага повинні бути додатними числами!")
        db[key] = {"count": count, "weight": weight}
        print(f"Запис '{key}' успішно додано.")
    except ValueError as e:
        print(f"Помилка введення даних: {e}")

def delete_entry(db):
    """Видалення запису зі словника з обробкою винятків"""
    key = input("Введіть номер багажу для видалення: ").strip()
    try:
        del db[key]
        print(f"Запис '{key}' успішно видалено.")
    except KeyError:
        print(f"Помилка: Багаж із номером '{key}' не знайдено у словнику!")

def print_sorted(db):
    """Перегляд вмісту за відсортованими ключами"""
    if not db:
        print("Словник порожній.")
        return
    print("\n--- Словник, відсортований за ключами ---")
    for key in sorted(db.keys()):
        data = db[key]
        print(f"Пасажир (№ багажу): {key:5} | Кількість речей: {data['count']:2} | Загальна вага: {data['weight']:5.1f} кг")

def task_a(db):
    """а) Кількість пасажирів, які мають більше двох речей"""
    count = sum(1 for data in db.values() if data['count'] > 2)
    print(f"\n[а] Кількість пасажирів, які мають більше 2 речей: {count}")

def task_b(db):
    """б) Чи є хоч один пасажир, багаж якого складається з однієї речі вагою менше 25 кг"""
    found = any(data['count'] == 1 and data['weight'] < 25.0 for data in db.values())
    if found:
        print("\n[б] ТАК, є принаймні один пасажир з 1 річчю вагою менше 25 кг.")
    else:
        print("\n[б] НІ, таких пасажирів немає.")

def task_c(db):
    """в) Номер багажу, в якому вага однієї речі відрізняється від загальної середньої ваги однієї речі не більше ніж на 0.5 кг"""
    total_items = sum(data['count'] for data in db.values())
    total_weight = sum(data['weight'] for data in db.values())
    
    if total_items == 0:
        print("\n[в] Словник порожній або загальна кількість речей дорівнює 0.")
        return

    avg_item_weight = total_weight / total_items
    print(f"\nЗагальна середня вага однієї речі по всіх пасажирах: {avg_item_weight:.2f} кг")
    
    matching_keys = []
    for key, data in db.items():
        passenger_avg = data['weight'] / data['count']
        if abs(passenger_avg - avg_item_weight) <= 0.5:
            matching_keys.append((key, passenger_avg))

    if matching_keys:
        print("[в] Номери багажу, де середня вага однієї речі відрізняється від загальної не більше ніж на 0.5 кг:")
        for k, val in matching_keys:
            print(f"    - Номер: {k} (Середня вага речі пасажира: {val:.2f} кг)")
    else:
        print("[в] Пасажирів, що відповідають умові в), не знайдено.")

def menu():
    while True:
        print("\n" + "="*50)
        print(" МЕНЮ КЕРУВАННЯ БАГАЖНОЮ СИСТЕМОЮ")
        print("="*50)
        print("1 - Вивести всі записи словника")
        print("2 - Додати новий запис")
        print("3 - Видалити запис за ключем")
        print("4 - Переглянути словник за відсортованими ключами")
        print("5 - [Завдання А] Пасажири з понад 2 речами")
        print("6 - [Завдання Б] Перевірка пасажирів (1 річ < 25 кг)")
        print("7 - [Завдання В] Номери багажу із середньою вагою речі ≈ загальній (±0.5 кг)")
        print("0 - Вийти з програми")
        
        choice = input("Оберіть пункт меню: ").strip()
        
        if choice == '1':
            print_all(luggage_db)
        elif choice == '2':
            add_entry(luggage_db)
        elif choice == '3':
            delete_entry(luggage_db)
        elif choice == '4':
            print_sorted(luggage_db)
        elif choice == '5':
            task_a(luggage_db)
        elif choice == '6':
            task_b(luggage_db)
        elif choice == '7':
            task_c(luggage_db)
        elif choice == '0':
            print("Завершення роботи програми.")
            break
        else:
            print("Некоректний вибір. Спробуйте ще раз!")

if __name__ == "__main__":
    menu()
