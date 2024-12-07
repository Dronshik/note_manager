user_name = input("Введите имя пользователя: ")
title1 = input("Заголовок 1: ")
title2 = input("Заголовок 2: ")
title3 = input("Заголовок 2: ")
content = input("Описание: ")
status = input("Статус работы: ")
created_date = input("Начало работы (дд.мм.гг.): ")
issue_date = input("Окончание работы (дд.мм.гг.): ")
list = [title1, title2, title3]
print ("Здравствуйте,",(user_name),'Ваши темы:',(list[0]), ',', (list[1]), 'и', (list[2]), "Описание:", (content),'статус работы:', (status), 'Дата начала:',(created_date), 'Дата окончани:',(issue_date))

