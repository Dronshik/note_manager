from datetime import datetime
created_date = datetime.now().strftime('%Y-%m-%d')
def created_note():# функция для создания заметок
    print("Введите имя пользователя:")
    while True:
        user_name = input()
        if user_name == "":
            print("Введите еоректные данные")
        else:
            break
    print("Введите заголовок заметки:")

    while True:
        title = input()
        if title == "":
            print("Введите еоректные данные")
        else:
            break
    print("Введите описание заметки:")

    while True:
        content = input()
        if content == "":
            print("Введите еоректные данные")
        else:
            break
    print("Ведите статус заметки: новая, в процессе, или отложено :")
    while True:  # для создания статуса
        q = input("Вводите только из предложенных вариантов: ")
        if q == "новая":
            break
        elif q == "в процессе":
            break
        elif q == "отложено":
            break
        else:
            print("Введите корректные данные")
    status = q

    print('Введите дату окончание работы, в формате: 2024-12-01: ')
    while True:# цикл на случай некорректности вводимых данных
        try:
            t = input()
            issue_date = datetime.strptime(t, "%Y-%m-%d").date()# преобразование даны в нужный формат
            if type(issue_date) == str:
                break
            else:
                break
        except ValueError:#если данные  некорректные
            print("Некорректные данные, введите заново:")
    issue_date = t

    print("Ваша заметка успешно создана:")
    notes = []
    note = {'user': user_name, 'title': title, 'content': content, 'status': status, 'created_date': created_date,
            'issue_date': issue_date}
    notes.append(note)
    for note in notes:
        print("Здравствуте,", note['user'])
        print("Ваш заголовок:", note['title'])
        print("Описание:", note['content'])
        print("Статус работы:", note['status'])
        print("Дата начала:", note['created_date'])
        print("Дата окончания:", note['issue_date'])
        print( "----")
    return note

def main():# Функция для запуска программы, просмотра заметок и дальнейщих действий по желанию пользователя
    while True:
        print("Доступные операции:")
        print("1. Создать заметку")

        choice = input("Выберите операцию (1): ")

        if choice == '1':
            created_note()

if __name__ == "__main__":
    main()