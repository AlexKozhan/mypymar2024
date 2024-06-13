"""Напишите программу, которая создает
текстовый файл(если его нету) "students.txt".
Запишите в файл список студентов, номер группы,
их оценки. Каждый студент на новой строке.
Откройте файл и прочитайте всю информацию из него.
Напечатайте общее количество студентов, количество студентов
для каждой группы и среднюю оценку для каждой группы.
Допишите эту информацию в конец файла. Передусмотрите
возможные ошибки и обработайте их.
"""


def write_students_data(file_name):
    """
    Write students' data to a file.
    """
    students_data = [
        {"name": "Alex", "group": 1, "grades": [8, 9, 7]},
        {"name": "Masha", "group": 2, "grades": [6, 7, 2]},
        {"name": "Ivan", "group": 1, "grades": [9, 8, 9]},
        {"name": "Sasha", "group": 2, "grades": [7, 8, 7]},
        {"name": "Eva", "group": 1, "grades": [8, 8, 8]}
    ]

    try:
        with open(file_name, 'w', encoding='utf-8') as file:
            for student in students_data:
                file.write(f"{student['name']},{student['group']},"
                           f"{','.join(map(str, student['grades']))}\n")
        print(f"Data successfully written to {file_name}")
    except IOError as e:
        print(f"Error writing to {file_name}: {e}")


def read_and_print_statistics(file_name):
    """
    Read student data from a file, calculate statistics, and print them.
    """
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            lines = file.readlines()

            total_students = len(lines)
            group_counts = {}
            group_sums = {}

            for line in lines:
                parts = line.strip().split(',')
                group = int(parts[1])
                grades = list(map(int, parts[2].split(',')))

                if group in group_counts:
                    group_counts[group] += 1
                    group_sums[group] += sum(grades)
                else:
                    group_counts[group] = 1
                    group_sums[group] = sum(grades)

            print(f"Total number of students: {total_students}")
            for group, count in group_counts.items():
                average_grade = group_sums[group] / count
                print(f"Number of students in Group {group}: {count}")
                print(f"Average grade for Group {group}: {average_grade:.2f}")

            # Append statistics to the file
            with open(file_name, 'a', encoding='utf-8') as file:
                file.write("\nStatistics:\n")
                file.write(f"Total number of students: {total_students}\n")
                for group, count in group_counts.items():
                    average_grade = group_sums[group] / count
                    file.write(f"Number of students in Group {group}: {count}\n")
                    file.write(f"Average grade for Group {group}: "
                               f"{average_grade:.2f}\n")

    except IOError as e:
        print(f"Error reading from {file_name}: {e}")


if __name__ == "__main__":
    FILE_NAME = "students.txt"

    write_students_data(FILE_NAME)

    read_and_print_statistics(FILE_NAME)
