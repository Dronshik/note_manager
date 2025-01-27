import json
from fileinput import close

notes = [
    {
        "username": "Алексей",
        "title": "Список покупок",
        "content": "Купить продукты",
        "status": "новая",
        "created_date": "27-11-2024",
        "issue_date": "30-11-2024"
    }
]
def save_notes_json(notes, filename):

    # Запись JSON-данных в файл
    with open("notes.json", "w", encoding="utf-8") as file:# Сериализация данных в JSON с отступами для удобства чтения
        note = json.dump(notes, file, indent=4, ensure_ascii=False)
    print("Заметки успешно сохранены в файл notes.json")

save_notes_json(notes, 'notes.json')