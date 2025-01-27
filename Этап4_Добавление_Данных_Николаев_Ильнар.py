import json
def  append_notes_to_file(notes, filename):
     with open(filename, 'a', encoding='utf-8') as file:
         for note in notes:
             file.write(f"Имя пользователя: {note['username']}\n")
             file.write(f"Заголовок: {note['title']}\n")
             file.write(f"Описание: {note['content']}\n")
             file.write(f"Статус: {note['status']}\n")
             file.write(f"Дата создания: {note['created_date']}\n")
             file.write(f"Дедлайн: {note['issue_date']}\n")
             file.write("---\n")
new_notes = [
         {
             "username": "Мария",
             "title": "План работы",
             "content": "Подготовить отчёт",
             "status": "в процессе",
             "created_date": "27-11-2024",
             "issue_date": "28-11-2024"
        }
     ]

append_notes_to_file(new_notes, "notes.txt")