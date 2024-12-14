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
            print("Истекло", abs(issue_date.day - current_date.day), " дня назад.")
            break
        elif issue_date > current_date:# если дедлайн еще впереди
            print('Истечет через', issue_date.day - current_date.day, "дней")
            break
        elif issue_date == current_date:#если дедлайн сегодня
            print("Дедлайн сегодня!")
            break
    except ValueError:#
        print("Некорректные данные, введите заново")
























