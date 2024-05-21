# Мы можем визуализировать художественную
# пирамиду ASCII с N уровнями,
# напечатав N рядов звездочек, где верхний ряд
# имеет одну звездочку
# в центре, а каждый последующий ряд имеет две
# дополнительные звездочки с каждой стороны.

# Вот как это выглядит, когда N равно 3.

#   *
#  ***
# *****
# Вот как это выглядит, когда N равно 5.

#     *
#    ***
#   *****
#  *******
# *********
# Необходимо написать программу, которая
# генерирует такую пирамиду
# со значением N, равным 10

N = 10
for i in range(N):
    """Adding stars and white spaces for piramida"""
    stars = 2*i+1
    probeli = N-i-1
    piramida = ' ' * probeli + '*' * stars
    print(piramida)
