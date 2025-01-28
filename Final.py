#Спрашиваем у пользывателя данные для заметки

name = input('Введите Ваше имя: ')
surname = input('Введите Вашу фамилию: ')
print ('Здраствуйте,', name.title(), surname.title(), sep=' ')
title = input('Введите заголовок заметки: ')
content = input('Напишите описание заметки: ')
status = input('В каком статусе замтка "В Работе" или "Закрыта": ')
data_created = input('Укажите дату создания заметки в формате ЧЧ-ММ-ГГГГ: ')
data_issue = input('Укажите дедлайн заметки в фомате ЧЧ-ММ-ГГГГ: ')

#Объединяем введёные данные ползывателя в список
list_info = [name.title(),
             surname.title(),
             title.title(),
             content.title(),
             status.title(),
             data_created.title(),
             data_issue.title()]

#Запрашиваем у юзера 2 доп заголовка
title1 = input('Введите дополнительный заголовок:')
title2 = input('Введите ещё один заголовок: ')

#Создаем доп список для 2 доп заголовках
list_info2 = [title1.title(), title2.title()]

#Добавляем доп список в конец первого списка
list_info.append(list_info2)

#Выврдим всю собраную инфу на экран
print(list_info)


