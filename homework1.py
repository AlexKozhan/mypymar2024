"""Напишите программу, которая бы работала
следующим образом - находила символ "#" и если
этот символ найден - удаляла предыдущий символ
из строки. Ваша задача обработать строки с "#" символом.

Примеры:

"a#bc#d" ==>  "bd"
"abc#d##c"      ==>  "ac"
"abc##d######"  ==>  ""
"#######"       ==>  ""
""              ==>  ""
"""


def sortirovka(a):
    """Deleting element 'i-1' when we face i=#
    and puting other elements of string in 'masiv'"""
    masiv = []
    for i in a:
        if i == '#':
            if masiv:
                masiv.pop()
        else:
            masiv.append(i)
    return ''.join(masiv)


print(sortirovka("a#bc#d"))
print(sortirovka("abc#d##c"))
print(sortirovka("abc##d######"))
print(sortirovka("#######"))
print(sortirovka(""))
