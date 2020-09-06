print('Задание №2')


def print_user_info(first_name, second_name, birth_date, mail, mobile_number):
    print(f'{first_name} {second_name}, дата рождения: {birth_date}, контакты: {mail} {mobile_number}')


f_name = input('Введите имя: ')
s_name = input('Введите фамилию: ')
b_date = input('Введите дату рождения: ')
e_mail = input('Введите почту: ')
m_number = input('Введите номер телефона: ')

user_info = dict(first_name=f_name, second_name=s_name, birth_date=b_date, mobile_number=m_number, mail=e_mail)
print_user_info(**user_info)
