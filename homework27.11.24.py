def send_email(message, recipient, sender = "university.help@gmail.com"):
    if "@" not in sender or "@"  not in recipient:
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
    elif (".com" not in sender and ".ru" not in sender and ".net" not in sender) or (".com" not in recipient and ".ru" not in recipient and ".net" not in recipient):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
    elif sender ==  recipient:
        print("Нельзя отправить письмо самому себе!")
    elif sender  == "university.help@gmail.com" :
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    elif sender != "university.help@gmail.com":
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")
send_email('Здарова', 'vasyok1337@gmail.com')
send_email('Как дела?', 'urban.fan@mail.ru', 'urban.info@gmail.com')
send_email('Что делаешь?',  'urban.student@mail.ru','urban.teacher@mail.uk')
send_email('Пошли гулять', 'urban.teacher@mail.ru', 'urban.teacher@mail.ru')