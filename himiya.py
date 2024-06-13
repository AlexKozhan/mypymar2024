"""Напишите программу, которая обрабатывает строку
- формулу молекулы, возвращает атомы из этой
молекулы и их количество в виде словаря.

Примеры:

H2O -> {H: 2, O: 1}
Mg(OH)2 -> {Mg: 1, O: 2, H: 2}
K4[ON(SO3)2]2 -> {K: 4, O: 14, N: 2, S: 4}

Замечания:

Скобки в формулах могут быть круглыми, квадратными
и фигурными. Скобки могут быть вложены друг в друга.
Индекс после скобки означает количество раз, которое
повторяется каждый атом внутри скобок.
Индекс после скобки не обязателен. Если его нет, значит
содержимое скобок повторяется 1 раз."""

from collections import defaultdict
import copy


class Himiya:
    """
    A class to parse a chemical formula
    and count the number of each type of atom.
    """
    def countOfAtoms(self, formula: str) -> dict:
        """
        Parse the given chemical formula and
        return a dictionary with the count of
        each type of atom.
        """
        stk = []  # Stack to hold dictionaries of atom counts at different levels of nesting
        cur = defaultdict(int)  # Current dictionary of atom counts

        i = 0  # Index to iterate over the formula
        while i < len(formula):
            if formula[i] in '([{':  # If opening bracket, push current dictionary to stack and start a new one
                stk.append(copy.deepcopy(cur))
                cur.clear()
                i += 1

            elif formula[i] in ')]}':  # If closing bracket, process the nested formula
                j = i + 1
                while j < len(formula) and formula[j].isdigit():
                    j += 1

                # Multiplier for the nested formula
                num = 1 if j == i + 1 else int(formula[i+1:j])
                for k in cur.keys():
                    cur[k] *= num

                # Merge current dictionary with the top dictionary from the stack
                for k, v in cur.items():
                    stk[-1][k] += v

                cur = stk.pop(-1)  # Pop the top dictionary from the stack
                i = j

            else:
                if formula[i].isupper():  # If it's an atom symbol
                    j = i + 1
                    while j < len(formula) and formula[j].islower():
                        j += 1

                    atom = formula[i:j]  # Extract the atom symbol

                    k = j
                    while k < len(formula) and formula[k].isdigit():
                        k += 1
                    num = 1 if j == k else int(formula[j:k])  # Extract the count
                    cur[atom] += num  # Add the atom count to the current dictionary
                    i = k

        # Merge any remaining dictionaries in the stack
        while stk:
            top = stk.pop()
            for k, v in cur.items():
                top[k] += v
            cur = top

        return dict(sorted(cur.items()))


solution = Himiya()


assert solution.countOfAtoms("H2O") == {'H': 2, 'O': 1}, \
    f"Error: {solution.countOfAtoms('H2O')}"
assert solution.countOfAtoms("Mg(OH)2") == {'Mg': 1, 'O': 2, 'H': 2}, \
    f"Error: {solution.countOfAtoms('Mg(OH)2')}"
assert solution.countOfAtoms("K4[ON(SO3)2]2") == {'K': 4, 'O': 14, 'N': 2, 'S': 4}, \
    f"Error: {solution.countOfAtoms('K4[ON(SO3)2]2')}"
