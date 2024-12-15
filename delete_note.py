
notes = [
    {"username": "Алексей", "title": "Список покупок", "content": "Купить продукты на неделю"},
    {"username": "Мария", "title": "Учеба", "content": "Подготовиться к экзамену"},
    {"username": "Ильнар", "title": "Работа", "content": "Заработать"},
]

def delete_notes_by_username(username):# функция для удаления заметки по пользователю
    global notes
    notes_before = len(notes)
    notes = [note for note in notes if note["username"] != username]
    notes_after = len(notes)
    if notes_before == notes_after:
        print(f"Заметки для пользователя '{username}' не найдены.")
    else:
        print(f"Заметки для пользователя '{username}' были удалены.")

def delete_notes_by_title(title):# Функция для удаления заметки по загаловкам
    global notes
    notes_before = len(notes)
    notes = [note for note in notes if note["title"] != title]
    notes_after = len(notes)
    if notes_before == notes_after:
        print(f"Заметки с заголовком '{title}' не найдены.")
    else:
        print(f"Заметки с заголовком '{title}' были удалены.")

def main():# Функция для запуска программы, просмотра заметок и дальнейщих действий по желанию пользователя
    while True:
        print("Доступные операции:")
        print("1. Удалить заметки по имени пользователя")
        print("2. Удалить заметки по заголовку")
        print("3. Вывести оставшиеся заметки")
        print("4. Выйти")

        choice = input("Выберите операцию (1-4): ")

        if choice == '1':
            username = input("Введите имя пользователя: ")
            delete_notes_by_username(username)
        elif choice == '2':
            title = input("Введите заголовок заметки: ")
            delete_notes_by_title(title)
        elif choice == '3':
            print("Текущий список ваших заметок:")
            for note in notes:
                print("Имя пользователя", note['username'])
                print("Ваш заголовок:", note['title'])
                print("Описание:", note['content'])
                print("--------")
        elif choice == '4':
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите правильный вариант.")

if __name__ == "__main__":
    main()