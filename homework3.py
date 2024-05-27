"""Ваша задача написать программу,
принимающее число - номер кредитной карты
(число может быть четным или не четным).
И проверяющей может ли такая карта существовать.
Предусмотреть защиту от ввода букв, пустой
строки и т.д. Примечания Алгоритм Луна

Примеры
validate(4561261212345464) #=> False
validate(4561261212345467) #=> True"""


def validator(card_number):
    """Cheking string for not being empty and with letters"""
    if not isinstance(card_number, str) or not card_number.isdigit():
        return False

    reversed_list = [int(d) for d in card_number][::-1]
    temp_sum = 0
    for i, digit in enumerate(reversed_list):
        if i % 2 == 1:
            doubled = digit * 2
            if doubled > 9:
                doubled -= 9
            temp_sum += doubled
        else:
            temp_sum += digit

    return temp_sum % 10 == 0


print(validator("4561261212345464"))
print(validator("4561261212345467"))
