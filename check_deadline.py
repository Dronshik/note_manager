import datetime
current_date = datetime.datetime.today().date()
formatted_date = current_date.strftime('%d %m %Y')# смена формата даты
print("Текущая дата: ", formatted_date)
print('Введите дату завершения, в формате: 2024-12-01: ')
while True:# цикл на случай некорректности вводимых данных
    try:
        i = input()
        issue_date = datetime.datetime.strptime(i, "%Y-%m-%d").date()# преобразование даны в нужный формат
        current_date = datetime.datetime.today().date()# преобразование даты
        if issue_date < current_date:# если дедлайн истек
            days_passed = abs((issue_date - current_date).days)
            print("Истекло", days_passed, " дня назад.")
            break
        elif issue_date > current_date:# если дедлайн еще впереди
            days_left = (issue_date - current_date).days
            print('Истечет через', days_left, "дней")
            break
        elif issue_date == current_date:#если дедлайн сегодня
            print("Дедлайн сегодня!")
            break
    except ValueError:#если данные  некорректные
        print("Некорректные данные, введите заново:")
























