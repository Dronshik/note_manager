user_name = input("Введите имя пользователя: ")
title1 = input("Заголовок 1: ")
title2 = input("Заголовок 2: ")
title3 = input("Заголовок 2: ")
content = input("Описание: ")
status = input("Статус работы: ")
created_date = input("Начало работы (дд.мм.гг.): ")
issue_date = input("Окончание работы (дд.мм.гг.): ")
list = [user_name, title1, title2, title3, content, status, created_date, issue_date]
print ("Здравствуйте,", list[0], '!', "Ваша тема:", (list[1]), ',', (list[2]), 'и', (list[3]), '.', "Описание:", list[4], '.',  "Статус работы:", list[5],"Дата выполнения с", list[6], "по", list[7], '.')
