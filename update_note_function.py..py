from datetime import datetime
notes = []
note = {"user_name": "Алексей", "title": "Список дел", "content": "Купить продукты на неделю", "status": "новая", "created_date": "27-11-2024", "issue_date": "30-11-2024"}
notes.append(note)

def changes_username():# функция для изменения имени пользователя
    global notes
    global note
    print("Введите новое имя пользователя:")
    for note in notes:
        while True:
            note["user_name"] = input()
            if note["user_name"]  == "":
                print("Введите новое имя пользователя")
            else:
                break

    print("Имя пользователя был успешно изменен на:", note["user_name"])

def change_title():# Функция для изменения загаловка
    global notes
    global note
    print("Введите новое имя пользователя:")
    for note in notes:
        while True:
            note["title"] = input()
            if note["title"] == "":
                print("Введите новый заголовок")
            else:
                break
    print("Заголовое был успешно изменен на:", note["title"])
def change_content(): # Функция для изменения описания
    global notes
    global note
    print("Введите новое описание:")
    for note in notes:
        while True:
            note["content"] = input()
            if note["content"] == "":
                print("Введите новое описание")
            else:
                break
    print("Описание было успешно изменено на:", note["content"])
def change_status(): # Функция для изменения статуса
    global notes
    global note
    print("Введите новый статус: новая, в процессе, отложено.")
    for note in notes:
        while True:
            note["status"] = input("Вводите только из предложенных вариантов: ")
            if note["status"] == "новая":
                print('Статус заметки успешно обновлён на:', note["status"])
                break
            elif note["status"] == "в процессе":
                print('Статус заметки успешно обновлён на:', note["status"])
                break
            elif note["status"] == "отложено":
                print('Статус заметки успешно обновлён на:', note["status"])
                break
            else:
                print("Введите корректные данные")
def change_issue_date():# Функция для изменения времени
    global notes
    global note
    print('Введите дату окончание работы, в формате: 01-12-2024: ')
    for note in notes:
        while True:# цикл на случай некорректности вводимых данных
            try:
                note["issue_date"] = input()
                issue_date = datetime.strptime(note["issue_date"], "%d-%m-%Y").date()# преобразование даны в нужный формат
                if type(issue_date) == str:
                    break
                else:
                    break
            except ValueError:#если данные  некорректные
                print("Некорректные данные, введите заново:")
    print("Дата окончание работы был успешно изменен на", note["issue_date"])


def main():# Функция для запуска программы, просмотра заметок и дальнейщих действий по желанию пользователя
    while True:
        print("Ваша заметка:")
        for note in notes:
            print("Имя пользователя", note['user_name'])
            print("Ваш заголовок:", note['title'])
            print("Описание:", note['content'])
            print("Статус работы:", note['status'])
            print("Дата начала:", note['created_date'])
            print("Дата окончания:", note['issue_date'])

        print("Доступные операции:")
        print("1. Изменить имя пользователя")
        print("2. Изменить название заголовка")
        print("3. Изменить описание заметки")
        print("4. Изменить статус заметки")
        print("5. Изменить время окончания заметки")
        print("6. Выйти")
        print("Выберите операцию (1-7): ")

        choice = input()

        if choice == '1':
            print("Вы уверены, что хотите обновить поле? (да/нет):")
            while True:
                t = input()
                if t == "да":
                    changes_username()
                    break
                elif t == "нет":
                    break
                else:
                    print("Введите только да или нет")
        elif choice == '2':
            print("Вы уверены, что хотите обновить поле? (да/нет):")
            while True:
                t = input()
                if t == "да":
                    change_title()
                    break
                elif t == "нет":
                    break
                else:
                    print("Введите только да или нет")
        elif choice == '3':
            print("Вы уверены, что хотите обновить поле? (да/нет):")
            while True:
                t = input()
                if t == "да":
                    change_content()
                    break
                elif t == "нет":
                    break
                else:
                    print("Введите только да или нет")
        elif choice == '4':
            print("Вы уверены, что хотите обновить поле? (да/нет):")
            while True:
                t = input()
                if t == "да":
                    change_status()
                    break
                elif t == "нет":
                    break
                else:
                    print("Введите только да или нет")
        elif choice == '5':
            print("Вы уверены, что хотите обновить поле? (да/нет):")
            while True:
                t = input()
                if t == "да":
                    change_issue_date()
                    break
                elif t == "нет":
                    break
                else:
                    print("Введите только да или нет")
        elif choice == '6':
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите правильный вариант.")

if __name__ == "__main__":
    main()