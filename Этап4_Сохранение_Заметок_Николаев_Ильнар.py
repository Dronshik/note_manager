def save_notes_to_file(notes, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        for i, note in enumerate(notes, start=1):
            file.write(f"Заметка № {i}\n")
            file.write(f"Имя пользователя: {note['username']}\n")
            file.write(f"Заголовок: {note['title']}\n")
            file.write(f"Описание: {note['content']}\n")
            file.write(f"Статус: {note['status']}\n")
            file.write(f"Дата создания: {note['created_date']}\n")
            file.write(f"Дедлайн: {note['issue_date']}\n")
            file.write("---\n")

# Пример использования:
notes = [
    {
        "username": "user1",
        "title": "Заметка 1",
        "content": "Описание заметки 1",
        "status": "В процессе",
        "created_date": "2023-10-01",
        "issue_date": "2023-10-10"
    },
    {
        "username": "user2",
        "title": "Заметка 2",
        "content": "Описание заметки 2",
        "status": "Завершено",
        "created_date": "2023-10-02",
        "issue_date": "2023-10-12"
    }
]

save_notes_to_file(notes, "notes.txt")