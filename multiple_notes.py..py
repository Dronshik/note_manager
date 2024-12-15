import datetime
print("Добро пожаловать в Менеджер заметок! Вы можете добавить новую заметку")
notes = []# список, куда добавляются все заметки в виде словарей

while True:
    user_name = input("Введите имя пользователя: ")
    title = input("Введите заголовок : ")
    content = input("Введите описание: ")
    list = {1:"выполнено", 2:"в процессе",3:"отложено"}
    print("ВВедите статус заметки: выполнено, в процессе, или отложено :")
    while True:# для создания статуса
        q = input("Вводите только из предложенных вариантов: ")
        if q == "выполнено":
            print('Статус заметки успешно обновлён на:', (list.get(1)))
            break
        elif q == "в процессе":
            print('Статус заметки успешно обновлён на: ', (list.get(2)))
            break
        elif q == "отложено":
            print('Статус заметки успешно обновлён на: ', (list.get(3)))
            break
        else:
            print("Введите корректные данные")
    status = q
    current_date = datetime.datetime.today().date()
    print('Введите дату начала, в формате: 2024-12-01: ')
    while True:# цикл на случай некорректности вводимых данных
        try:
            i = input()
            created_date = datetime.datetime.strptime(i, "%Y-%m-%d").date()# преобразование даны в нужный формат
            if type(created_date) == str:
                break
            else:
                break
        except ValueError:#если данные  некорректные
            print("Некорректные данные, введите заново:")
    created_date = i
    print('Введите дату окончание работы, в формате: 2024-12-01: ')
    while True:# цикл на случай некорректности вводимых данных
        try:
            t = input()
            issue_date = datetime.datetime.strptime(t, "%Y-%m-%d").date()# преобразование даны в нужный формат
            if type(issue_date) == str:
                break
            else:
                break
        except ValueError:#если данные  некорректные
            print("Некорректные данные, введите заново:")
    issue_date = t
    print("Желаете добавить еще одну заметку? да/нет")
    while True:# для продолжения добавления заметок или же прекращения работы
        с = input()
        if с == "нет":
            break
        elif с == "да" or "Да":
            print("Создайте новую заметку")
            break
        else:
            print("Введите только да или нет")
    note = {'user': user_name, 'title': title, 'content': content, 'status': status, 'created_date': created_date, 'issue_date': issue_date}
    notes.append(note)
    if с == "нет":
        break
def hello(notes):  # достает элементы из списка и словаря + выводит данные заметок
    for note in notes:
        print("Здравствуте,", note['user'])
        print("Ваш заголовок:", note['title'])
        print("Описание:", note['content'])
        print("Статус работы:", note['status'])
        print("Дата начала:", note['created_date'])
        print("Дата окончания:", note['issue_date'])
        print("----")

hello(notes)  # вызываем функцию hello с параметром notes
