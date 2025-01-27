
try:
    with open("ret.exe", 'r') as file:
        print(file.read())
except FileNotFoundError:
    print('Файл "ret.txt" не найден. Создан новый файл.')
except UnicodeDecodeError:
    print('Ошибка при чтении файла "ret.exe". Проверьте его содержимое')
except PermissionError:
    print('Ошибка доступа')
except Exception as e:
    print(f"Ошибка: {e}")
