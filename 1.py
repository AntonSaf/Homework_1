# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# 6 -> да
# 7 -> да
# 1 -> нет


number = int(input('Введите день недели (число от 1 до 7): '))
if number > 5 and number <= 7:
    print('Да, это выходной день')
elif number > 0 and number <= 5:
    print('Нет, это рабочий день')
else:
    print('Такого дня недели нет')