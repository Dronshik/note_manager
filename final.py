user_name = input("Введите имя пользователя: ")
title1 = input("Заголовок 1: ")
title2 = input("Заголовок 2: ")
title3 = input("Заголовок 2: ")
content = input("Описание: ")
status = input("Статус работы: ")
created_date = input("Начало работы (дд.мм.гг.): ")
issue_date = input("Окончание работы (дд.мм.гг.): ")
list = [title1, title2, title3]
book = {1:user_name, 2:(list[0]), 3:(list[1]), 4:(list[2]), 5:content, 6:status, 7:created_date, 8:issue_date }
print("Здравствуйте,", book[1], '!', "Ваша тема:", book[2], ',', book[3], 'и', book[4], '.',  "Описание:",book[3], '.',  "Статус работы:", book[6], "Дата выполнения с", book[7], "по", book[8])
