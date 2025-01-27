def load_notes_from_file(filename):
    notes = []
    with open('notes.txt', 'r', encoding='utf-8') as file:
        lines = file.read().split('---\n')

    for note in lines:
        if not note.strip():
            continue
        note_dict = {}
        for line in note.strip().split('\n'):
            if ': ' in line:
                key, value = line.split(': ', 1)
                key = key.lower().replace(' ', '_')
                if key == 'дата_создания':
                    key = 'created_date'
                elif key == 'дедлайн':
                    key = 'issue_date'
                note_dict[key] = value
        notes.append(note_dict)

    return notes




notes = load_notes_from_file('notes.txt')
print(notes)