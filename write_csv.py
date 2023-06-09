import csv

def write_classes(classes, file_name='classes.csv'):
    with open(file_name, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=classes[0].keys())
        writer.writeheader()
        writer.writerows(classes)
        f.close()

def write_future_schools(future_schools, file_name='schools.csv'):
    with open(file_name, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=future_schools[0].keys())
        writer.writeheader()
        writer.writerows(future_schools)
        f.close()

def write_students(students, file_name='students.csv'):
    with open(file_name, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=students[0].keys())
        writer.writeheader()
        writer.writerows(students)
        f.close()

def write_competitions(competitions, file_name='competitions.csv'):
    with open(file_name, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=competitions[0].keys())
        writer.writeheader()
        writer.writerows(competitions)
        f.close()

def write_student_competitions(student_competitions, file_name='student_competitions.csv'):
    with open(file_name, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=student_competitions[0].keys())
        writer.writeheader()
        writer.writerows(student_competitions)
        f.close()
