import json


def write_classes(classes, file_name='classes.json'):
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(json.dumps(classes, indent=4, ensure_ascii=False))
        f.close()


def write_future_schools(future_schools, file_name='schools.json'):
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(json.dumps(future_schools, indent=4, ensure_ascii=False))
        f.close()


def write_students(students, file_name='students.json'):
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(json.dumps(students, indent=4, ensure_ascii=False))
        f.close()


def write_competitions(competitions, file_name='competitions.json'):
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(json.dumps(competitions, indent=4, ensure_ascii=False))
        f.close()


def write_student_competitions(student_competitions, file_name='student_competitions.json'):
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(json.dumps(student_competitions, indent=4, ensure_ascii=False))
        f.close()
