list = {1:"выполнено", 2:"в процессе",3:"отложено"}
print('Ваш статус заметки:', list.get(2))
print("Выберите статус заметки: 1 = выполнено, 2 = в процессе, 3 = отложено")
while True:
    status = input("Вводите только цифрами: ")
    if status == "1":
        print('Статус заметки успешно обновлён на:', (list.get(1)))
        break
    elif status == "2":
        print('Статус заметки успешно обновлён на: ', (list.get(2)))
        break
    elif status == "3":
        print('Статус заметки успешно обновлён на: ', (list.get(3)))
        break
    else:
        print("Введите корректные данные")
print('Если хотите придумать свой статус напишите ниже: ')
list2 = []
status1 = input()
list2.append(status1)
print('Статус заметки успешно обновлён на:', *list2)