from datetime import datetime
from random import choice

created_date = datetime.now().strftime('%Y-%m-%d')
notes = []
def created_note():# функция для создания заметок
    print("Введите имя пользователя:")
    while True:
        user_name = input()
        if user_name == "":
            print("Введите корректные данные")
        else:
            break
    print("Введите заголовок заметки:")

    while True:
        title = input()
        if title == "":
            print("Введите корректные данные")
        else:
            break
    print("Введите описание заметки:")

    while True:
        content = input()
        if content == "":
            print("Введите корректные данные")
        else:
            break

    print("Введите статус заметки: новая, в процессе, или отложено:")

    while True:
        status = input("Вводите только из предложенных вариантов: ")
        if status in ["новая", "в процессе", "отложено"]:
            break
        else:
            print("Введите корректные данные")

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
    note = {'user_name': user_name, 'title': title, 'content': content, 'status': status, 'created_date': created_date,
            'issue_date': issue_date}
    notes.append(note)

    return notes
def display_notes(notes):#функция для вывода заметок
    if not notes:
        print("У вас нет сохранённых заметок.")
        return

    for index, note in enumerate(notes, start=1):
        print(f"Заметка №{index}:")
        print(f"Имя пользователя: {note.get('user_name', 'Не указано')}")
        print(f"Заголовок: {note.get('title', 'Не указано')}")
        print(f"Описание: {note.get('content', 'Не указано')}")
        print(f"Статус: {note.get('status', 'Не указано')}")
        print(f"Дата создания: {note.get('created_date', 'Не указано')}")
        print(f"Дедлайн: {note.get('issue_date', 'Не указано')}")
        print()  # Пустая строка для лучшей читаемости

def search_notes(notes, keyword=None, status=None):# Функция для поиска по данным
    if not notes:
        print("Список заметок пуст.")
        return

    filtered_notes = notes

    if keyword:
        keyword = keyword.lower()  # Приводим к нижнему регистру для нечувствительного поиска
        filtered_notes = [note for note in filtered_notes if
                          keyword in note['title'].lower() or
                          keyword in note['content'].lower() or
                          keyword in note['username'].lower()]

    if status:
        filtered_notes = [note for note in filtered_notes if note['status'] == status]
# Если в словаре такого нет:
    if not filtered_notes:
        print("Заметки, соответствующие запросу, не найдены.")
    else:# Вывод найденной заметки
        for note in filtered_notes:
            print(f"Пользователь: {note['user_name']}, Заголовок: {note['title']}, "
                  f"Содержание: {note['content']}, Статус: {note['status']}, "
                  f"Дата создания: {note['created_date']}, Дата завершения: {note['issue_date']}")

def update_note():# Для обновления любого пункта, которое имеется
    #на мой взгляд есть баг, который обновляет поле во всех заметках, а не просто в выбранном
    if not notes:
        print("У вас нет сохранённых заметок.")
        return
    try:
        index = int(input("Введите номер заметки для обновления: ")) - 1# Находим заметку по номеру и работаем данными этой заметк
        if 0 <= index < len(notes):

            print("Выберите поле, которое хотите обновить:\n"
                      '\t1. Имя полбзователя\n'
                      '\t2. Заголовок\n'
                      '\t3. Описание\n'
                      '\t4. Статус\n'
                      '\t5. Дата окончания'
                      )
            choice = input()
            if choice == '1':
                    changes_username()
            elif choice == '2':
                    change_title()
            elif choice == '3':
                    change_content()
            elif choice == "4":
                    change_status()
            elif choice == "5":
                    change_issue_date()
            print("Заметка обновлена!")
        else:
            print("Некорректный номер заметки.")
    except ValueError:
        print("Введите корректный номер.")
def changes_username():# функция для изменения имени пользователя
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
def delete_note():
    if not notes:
        print("Список заметок пуст.")
        return
    try:
        index = int(input("Введите номер заметки для удаления: ")) - 1
        if 0 <= index < len(notes):
            deleted_note = notes.pop(index)
            print(f"Заметка '{deleted_note}' удалена!")
        else:
            print("Некорректный номер заметки.")
    except ValueError:
        print("Введите корректный номер.")

def main():# Функция для запуска программы, просмотра заметок и дальнейщих действий по желанию пользователя
    while True:
        print("Меню:\n"
          '\t1. Создать новую заметку\n'
          '\t2. Показать все заметки\n'
          '\t3. Обновить заметку\n'
          '\t4. Удалить заметку\n'
          '\t5. Найти заметки\n'
          '\t6. Выход из программы\n'
              )

        choice = input("Выбор: ")

        if choice == '1':
            created_note()
        elif choice == '2':
            display_notes(notes)
        elif choice == '3':
            update_note()
        elif choice == "4":
            delete_note()
        elif choice == "5":
            print("Осуществить поиск по:\n"
                  '\t1. Имени пользователя, заголовку, описанию\n'
                  '\t2. Статусу\n'
                  '\t3. Слову(имя пользователя/заголовок/описание) и статусу')
            i = input()
            if i == '1':
                search_notes(notes, keyword=input("Введите слово для поиска:"))
            elif i == '2':
                search_notes(notes, status=input("Введите статус заметки для поиска:"))
            elif choice == '3':
                search_notes(notes, keyword=input("Слово:"), status=input("Статус заметки:"))
        elif choice == '6':
            print("До свидания!")
            exit()
        else:
            print("Некорректный ввод")

if __name__ == "__main__":
    main()