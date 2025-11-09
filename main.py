
from utils import add_record, delete_record, search_record

dari_aty = "Парацетамол"
price = 850
quantity = 20

try:
    sold = int(input("Сатылған дәрі санын енгізіңіз: "))
except ValueError:
    print("Қате енгізу! Сан енгізу керек.")
    sold = 0

kalgany = quantity - sold
totalprice = sold * price

print(f"\n{dari_aty} дәрісінен {sold} дана сатылды.")
print(f"Қорда қалған дәрі саны: {kalgany}")

if kalgany < 5:
    print("Қор азайып барады, жаңа қор қосу қажет!")
else:
    print("Қор жеткілікті.")

print(f"Жалпы сатылым құны: {totalprice} теңге.\n")

dari = ["Парацетамол", "Аспирин", "Ибупрофен", "Парацетамол", "Цитрамон"]
print("Дәрілер тізімі (қайталанатындармен):", dari)

biregei_med = list(set(dari))
print("Қайталанбайтын дәрілер:", biregei_med)

darihana_info = ("Денсаулық", "Астана", "тәулік бойы жұмыс істейді")
print("Дәріхана туралы мәлімет:", darihana_info, "\n")

search = input("Іздейтін дәрінің атауын енгізіңіз: ").lower()
found = False
for med in biregei_med:
    if search in med.lower():
        print(f"{med} дәріханада бар.")
        found = True

if not found:
    print("Мұндай дәрі базада жоқ.")

example_text = "Парацетамол жоғары температура кезінде қолданылады."
print("\nМысал сөйлем:", example_text)
print("Барлық әріптерді кіші қылып:", example_text.lower())
print("Сөздерге бөлу:", example_text.split())
print("Сөзді ауыстыру:", example_text.replace("Парацетамол", "Ибупрофен"))

dariler = {"Парацетамол": 10, "Аспирин": 5, "Ибупрофен": 12}

print("\nҚазіргі қор жағдайы:")
for med, qty in dariler.items():
    print(f"{med}: {qty} дана")

def show_recursive(data, index=0):
    """Рекурсивті түрде дәрілерді шығару"""
    if index < len(data):
        med = list(data.keys())[index]
        print(f"{med}: {data[med]} дана")
        show_recursive(data, index + 1)

while True:
    print("\n=== Дәріхана мәзірі ===")
    print("1. Дәрі қосу")
    print("2. Дәріні жою")
    print("3. Дәріні іздеу")
    print("4. Қорды көру (рекурсивті)")
    print("5. Деректерді файлға сақтау")
    print("6. Файлдан оқу")
    print("7. Шығу")

    choice = input("Таңдауыңызды енгізіңіз (1-7): ")

    try:
        if choice == "1":
            new_med = input("Қосылатын дәрі атауы: ")
            amount = int(input("Саны: "))
            add_record(dariler, new_med, amount)

        elif choice == "2":
            name = input("Жойылатын дәрі атауы: ")
            delete_record(dariler, name)

        elif choice == "3":
            name = input("Іздейтін дәрі атауы: ")
            search_record(dariler, name)

        elif choice == "4":
            print("\n=== Қордағы дәрілер ===")
            show_recursive(dariler)

        elif choice == "5":
            with open("dariler.txt", "w", encoding="utf-8") as f:
                for med, qty in dariler.items():
                    f.write(f"{med}: {qty}\n")
            print("Мәліметтер 'dariler.txt' файлына сақталды.")

        elif choice == "6":
            try:
                with open("dariler.txt", "r", encoding="utf-8") as f:
                    print("\n=== Файлдан оқылған мәліметтер ===")
                    print(f.read())
            except FileNotFoundError:
                print("Файл табылмады. Алдымен сақтап көріңіз.")

        elif choice == "7":
            print("Бағдарлама аяқталды.")
            break

        else:
            print("Қате таңдау, қайта енгізіңіз.")

    except ValueError:
        print("Қате енгізу! Сан енгізіңіз.")
