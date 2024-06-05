"""
На вход подается строка, например, "cccbba" результат
работы программы - строка “c3b2a"

Примеры для проверки работоспособности:

"cccbba" == "c3b2a"
"abeehhhhhccced" == "abe2h5c3ed"
"aaabbceedd" == "a3b2ce2d2"
"abcde" == "abcde"
"aaabbdefffff" == "a3b2def5"
"""


def count_letters(s):
    """Function allows to count same letters"""
    if not s:
        return ""

    result = []
    current_char = s[0]
    count = 1

    for char in s[1:]:
        if char == current_char:
            count += 1
        else:
            result.append(current_char)
            if count > 1:
                result.append(str(count))
            current_char = char
            count = 1

    result.append(current_char)
    if count > 1:
        result.append(str(count))

    return ''.join(result)


print(count_letters("cccbba"))
print(count_letters("abeehhhhhccced"))
print(count_letters("aaabbceedd"))
print(count_letters("abcde"))
print(count_letters("aaabbdefffff"))
