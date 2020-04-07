full_salary = int(input('Введите зарплату за месяц: '))
taxyn = input('Налог на доход уже вычтен? (Да/Нет): ')

if taxyn == 'Да':
    print('Ок, дополнительно ничего не считаем')
    tax = 0
elif taxyn == 'да':
    print('Ок, дополнительно ничего не считаем')
    tax = 0
elif taxyn == 'Нет':
    print('Хорошо, произведем расчет согласно ставке налога')
    custom_tax = int(input('Введите ставку налога на доход: '))
    tax = full_salary * custom_tax / 100
elif taxyn == 'нет':
    print('Хорошо, произведем расчет согласно ставке налога')
    custom_tax = int(input('Введите ставку налога на доход: '))
    tax = full_salary * custom_tax / 100

workdays = int(input('Введите количество отработанных дней: '))

day_cost = (full_salary - tax) / workdays
hour_cost = day_cost / 8

print('Вы зарабатываете в день: ', day_cost)
print('Вы зарабатываете в час: ', hour_cost)

if taxyn == 'Нет':
    print('Уплаченный налог на доход: ', tax)
elif taxyn == 'нет':
    print('Уплаченный налог на доход: ', tax)