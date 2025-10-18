dari_aty = "Парацетамол"
price = 850
quantity = 20

sold = int(input("Сатылған дәрі санын енгізіңіз: "))

kalgany = quantity - sold
totalprice = sold * price

print(f"\n{dari_aty} дәрісінен {sold} дана сатылды.")
print(f"Қорда қалған дәрі саны: {kalgany}")

if kalgany < 5:
    print(" Қор азайып барады, жаңа қор қосу қажет!")
else:
    print(" Қор жеткілікті.")

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
    print(" Мұндай дәрі базада жоқ.")

example_text = "Парацетамол жоғары температура кезінде қолданылады."
print("\nМысал сөйлем:", example_text)
print("Барлық әріптерді кіші қылып:", example_text.lower())
print("Сөздерге бөлу:", example_text.split())
print("Сөзді ауыстыру:", example_text.replace("Парацетамол", "Ибупрофен"))


dariler = {"Парацетамол": 10, "Аспирин": 5, "Ибупрофен": 12}

print("\n Қазіргі қор жағдайы:")
for med, qty in dariler.items():
    print(f"{med}: {qty} дана")

while True:
    print("\n=== Дәріхана мәзірі ===")
    print("1. Дәрі қосу")
    print("2. Қорды көру")
    print("3. Шығу")

    choice = input("Таңдауыңызды енгізіңіз (1/2/3): ")

    if choice == "1":
        new_med = input("Қосылатын дәрі атауы: ")
        amount = int(input("Саны: "))
        dariler[new_med] = amount
        print(f"{new_med} дәрісі {amount} данамен қосылды.")
    elif choice == "2":
        print("\nҚордағы дәрілер:")
        for med, qty in dariler.items():
            print(f"{med}: {qty} дана")
    elif choice == "3":
        print("Бағдарлама аяқталды.")
        break
    else:
        print("Қате таңдау, қайта енгізіңіз.")
