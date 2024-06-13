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

    def __init__(self):
        pass

    def count_of_atoms(self, formula: str) -> dict:
        """
        Parse the given chemical formula and
        return a dictionary with the count of
        each type of atom.
        """
        stack = []  # Stack to hold dictionaries of atom
        # counts at different levels of nesting
        current = defaultdict(int)  # Current dictionary of atom counts

        i = 0  # Index to iterate over the formula
        while i < len(formula):
            if formula[i] in '([{':  # If opening bracket, push current
                # dictionary to stack and start a new one
                stack.append(copy.deepcopy(current))
                current.clear()
                i += 1

            elif formula[i] in ')]}':  # If closing bracket, process
                # the nested formula
                j = i + 1
                while j < len(formula) and formula[j].isdigit():
                    j += 1

                # Multiplier for the nested formula
                num = 1 if j == i + 1 else int(formula[i + 1:j])
                for key in current.keys():
                    current[key] *= num

                # Merge current dictionary with the top
                # dictionary from the stack
                for key, value in current.items():
                    stack[-1][key] += value

                current = stack.pop(-1)  # Pop the top dictionary
                # from the stack
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
                    num = 1 if j == k else int(formula[j:k])
                    # Extract the count
                    current[atom] += num  # Add the atom count
                    # to the current dictionary
                    i = k

        # Merge any remaining dictionaries in the stack
        while stack:
            top = stack.pop()
            for key, value in current.items():
                top[key] += value
            current = top

        return dict(sorted(current.items()))

    def get_sorted_atom_counts(self, formula: str) -> dict:
        """
        Returns a dictionary with sorted counts of each type of atom
        in the given chemical formula.
        """
        atom_counts = self.count_of_atoms(formula)
        return dict(sorted(atom_counts.items()))

    def validate_formula(self) -> bool:
        """
        Validates if the given formula is a valid chemical formula.
        """
        # Implement validation logic here (example: check
        # for balanced parentheses)
        # For simplicity, assuming parentheses are always
        # balanced in this case
        return True  # Placeholder for validation logic

    def get_supported_elements(self) -> list:
        """
        Returns a list of supported element symbols.
        """
        # Placeholder for actual supported elements
        return ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne']


if __name__ == "__main__":
    solution = Himiya()

    expected_result = {'H': 2, 'O': 1}
    assert solution.count_of_atoms("H2O") == expected_result, (
        f"Error: {solution.count_of_atoms('H2O')}"
    )

    expected_result = {'Mg': 1, 'O': 2, 'H': 2}
    assert solution.count_of_atoms("Mg(OH)2") == expected_result, (
        f"Error: {solution.count_of_atoms('Mg(OH)2')}"
    )

    expected_result = {'K': 4, 'O': 14, 'N': 2, 'S': 4}
    assert solution.count_of_atoms("K4[ON(SO3)2]2") == expected_result, (
        f"Error: {solution.count_of_atoms('K4[ON(SO3)2]2')}"
    )

    # Additional method usage example:
    sorted_counts = solution.get_sorted_atom_counts("K4[ON(SO3)2]2")
    print("Sorted Atom Counts:", sorted_counts)

    # Validation example:
    FORMULA_TO_VALIDATE = "H2O"
    IS_VALID = solution.validate_formula()
    print(f"Is '{FORMULA_TO_VALIDATE}' a valid formula?: {IS_VALID}")

    # Supported elements example:
    supported_elements = solution.get_supported_elements()
    print("Supported Elements:", supported_elements)
