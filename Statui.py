"""Вы получили в подарок на день рождения статуи
разных размеров, каждая статуя имеет неотрицательный
целочисленный размер. Поскольку Вам нравится доводить
вещи до совершенства, то необходимо расположить их от
меньшего к большему, чтобы каждая статуя была больше
предыдущей ровно на 1. Для этого Вам могут понадобиться
дополнительные статуи. Определите количество
отсутствующих статуй.

Пример Для статуй = [6, 2, 3, 8] результат должен быть = 3.
Иными словами, у Вас отсутствуют статуи размеров 4, 5 и 7."""

Statui_List = [6, 2, 3, 8]
Min_Statuya = min(Statui_List)
Max_Statuya = max(Statui_List)
Missing_Statui = []
"""Finding elements not in Statui_List"""
for i in range(Min_Statuya, Max_Statuya + 1):
    if i not in Statui_List:
        Missing_Statui.append(i)
Missing_Statui_String=', '.join(map(str, Missing_Statui))
print(f"Не хватает {len(Missing_Statui_String)} статуй")
print(f"У вас отсутсвуют статуи размеров {Missing_Statui_String}")
