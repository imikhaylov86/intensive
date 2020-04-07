original_password = '123123'
user_password = input('Введите пароль: ')

if user_password == original_password:
    print('Авторизация')
else:
    print('Неверный пароль!')