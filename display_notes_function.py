def display_notes(notes):
    if not notes:
        print("У вас нет сохранённых заметок.")
        return

    for index, note in enumerate(notes, start=1):
        print(f"Заметка №{index}:")
        print(f"Имя пользователя: {note.get('username', 'Не указано')}")
        print(f"Заголовок: {note.get('title', 'Не указано')}")
        print(f"Описание: {note.get('description', 'Не указано')}")
        print(f"Статус: {note.get('status', 'Не указано')}")
        print(f"Дата создания: {note.get('creation_date', 'Не указано')}")
        print(f"Дедлайн: {note.get('deadline', 'Не указано')}")
        print()  # Пустая строка для лучшей читаемости

# Пример использования функции:
notes = [
    {
        'username': 'Алексей',
        'title': 'Список покупок',
        'description': 'Купить продукты на неделю',
        'status': 'новая',
        'creation_date': '27-11-2024',
        'deadline': '30-11-2024'
    },
    {
        'username': 'Мария',
        'title': 'Задание по математике',
        'description': 'Решить задачи из учебника на странице 45',
        'status': 'в процессе',
        'creation_date': '26-11-2024',
        'deadline': '29-11-2024'
    }
]


def main():# Функция для запуска программы, просмотра заметок и дальнейщих действий по желанию пользователя
    while True:
        print("menu :\n"
          '\t1. посмотреть пример с заметками\n'
          '\t2. посмотреть пример, в случаи отсутсвия заметок\n'
          '\t3. выход'
              )
        print("Выберите операцию:")
        choice = input()

        if choice == '1':
            display_notes(notes)
        elif choice == '2':
            display_notes([])
        elif choice == '3':
            print("До свидания!")
            exit()


if __name__ == "__main__":
    main()