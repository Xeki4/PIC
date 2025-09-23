groupmates = [
    {"name": "Андрей", "surname": "Сафонов", "exams": ["БД", "ПИС", "АиГ"], "marks": [4, 5, 2]},
    {"name": "Дамир", "surname": "Гайфуллин", "exams": ["СИИ", "Основы Маркетинга", "Math"], "marks": [3, 4, 4]},
    {"name": "Александр", "surname": "Блинов", "exams": ["C++", "Физ. Культура", "1C"], "marks": [5, 5, 5]},
    {"name": "Константин", "surname": "Кабанов", "exams": ["C++", "Физ. Культура", "СИИ"], "marks": [2, 2, 2]}
]

def print_students(students):
    while True:
        try:
            threshold = float(input("Введите минимальный средний балл: ").replace(',', '.'))
            break
        except ValueError:
            print("Ошибка! Введите число.")

    # Заголовок таблицы
    print(f"{'Имя':<15}{'Фамилия':<10}{'Экзамены':<30}{'Оценки':<20}{'Средний балл':<15}")
    print("-" * 90)

    # Фильтрация и вывод по порогу
    for student in students:
        avg_score = sum(student["marks"]) / len(student["marks"])
        if avg_score >= threshold:
            exams_str = ", ".join(student["exams"])
            marks_str = ", ".join(map(str, student["marks"]))
            print(f"{student['name']:<15}{student['surname']:<10}{exams_str:<30}{marks_str:<20}{avg_score:.1f}")

print_students(groupmates)
3