def search_notes(notes, keyword=None, status=None):
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
            print(f"Пользователь: {note['username']}, Заголовок: {note['title']}, "
                  f"Содержание: {note['content']}, Статус: {note['status']}, "
                  f"Дата создания: {note['created_date']}, Дата завершения: {note['issue_date']}")

# Пример заметки
notes = [
    {'username': 'Алексей', 'title': 'Список покупок', 'content': 'Купить продукты на неделю', 'status': 'новая', 'created_date': '27-11-2024', 'issue_date': '30-11-2024'},
    {'username': 'Мария', 'title': 'Учеба', 'content': 'Подготовиться к экзамену', 'status': 'в процессе', 'created_date': '25-11-2024', 'issue_date': '01-12-2024'},
    {'username': 'Иван', 'title': 'План работы', 'content': 'Завершить проект', 'status': 'выполнено', 'created_date': '20-11-2024', 'issue_date': '26-11-2024'}
]
def main():# Функция для запуска программы, просмотра заметок и дальнейщих действий по желанию пользователя
    while True:
        print("Выберите операцию:\n"
          '\t1. поиск заметки по ключевому слову\n'
          '\t2. поиск заметки по статусу\n'
          '\t3. поиск заметки по ключевому слову и статусу\n'
          '\t4. пустой вызов для демонстрации проверки пустого списка\n'
          '\t5. выход\n'
              )

        choice = input("Выбор: ")
        if choice == '1':
            search_notes(notes, keyword=input("Введите слово для поиска:"))
        elif choice == '2':
            search_notes(notes, status=input("Введите статус заметки для поиска:"))
        elif choice == '3':
            search_notes(notes, keyword=input("Слово:"), status=input("Статус заметки:"))
        elif choice == "4":
            search_notes([])  # Пустой вызов для демонстрации проверки пустого списка
        elif choice == '5':
            print("До свидания!")
            exit()
        else:
            print("Некорректный ввод")
if __name__ == "__main__":
    main()
