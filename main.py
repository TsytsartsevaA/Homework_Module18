# Домашняя работа по Модулю 18

kolvo_biletov = int(input("Укажите сколько билетов Вы хотите приобрести:"))
if kolvo_biletov <=0:
    print("Вы не верно указали количество билетов")
age = []
for i in range(0, kolvo_biletov):
    input_value = int(input(f"Введите возраст участника конференции №{i + 1}:"))
    age.append(input_value)
    def prise(age):
        if age < 18:
            return 0
        elif 18 <= age < 25:
            return 990
        else:
            return 1390
full_prise = sum(map(prise, age))
discount_prise = int(full_prise * 0.9)
if kolvo_biletov > 3:
    print('Стоимость всех билетов со скидкой: ', discount_prise, "руб.")
else:
    print('Стоимость всех билетов: ', full_prise, "руб.")
