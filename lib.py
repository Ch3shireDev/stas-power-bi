from data import class_descriptions, school_names, competition_names
from random import randrange, choice, randint, gauss
from faker import Faker
fake = Faker('pl-PL')


def get_person():

    person = {
        'first_name': 'Jan',
        'last_name': 'Kowalski',
        'gender': 'M'
    }

    while True:
        name = fake.name()
        parts = name.split(' ')
        if len(parts) == 3:
            continue
        first_name = parts[0]
        last_name = parts[1]
        gender = 'F' if first_name[-1] == 'a' else 'M'

        person = {
            'first_name': first_name,
            'last_name': last_name,
            'gender': gender
        }

        return person

def get_future_schools():
    future_schools = []
    school_id = 1
    for school_name in school_names:
        school = {
            'school_id': school_id,
            'school_name': school_name,
            'school_geo_latitude': round(gauss(52.2, 0.1), 3),
            'school_geo_longtitude': round(gauss(21.0, 0.1), 3),
        }
        school_id += 1
        future_schools.append(school)
    return future_schools

def get_classes():
    classes = []
    class_id = 1
    class_index = 0
    for year in range(2009, 2017):
        for class_letter in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']:
            class_description_name = class_descriptions[class_index]
            class_index += 1

            class_name, class_description = class_description_name.split(': ')

            _class = {
                'class_id': class_id,
                'class_letter': class_letter,
                'class_name': class_name,
                'class_description': class_description,
                'class_year': year,
            }

            class_id += 1

            classes.append(_class)
    return classes



school_latitude_min = 51.8
school_latitude_max = 52.6

school_longitude_min = 20.3
school_longitude_max = 21.7

school_latitude = 52.2
school_longitude = 21.0

def get_students(future_schools, classes):

    students = []

    student_id = 1

    for _class in classes:
        for i in range(1, 31):
            person = get_person()

            geo_longtitude = gauss(school_longitude, 0.2)

            geo_latitude = gauss(school_latitude, 0.1)

            long_dist = abs(geo_longtitude - school_longitude) * 20
            lat_dist = abs(geo_latitude - school_latitude) * 20

            travel_time = round((long_dist + lat_dist) / 60) + randint(20, 40)

            travel_distance = round((long_dist + lat_dist) *2.5, 2)

            student = {
                'student_id': student_id,
                'student_first_name': person['first_name'],
                'student_last_name': person['last_name'],
                'student_gender': person['gender'],
                'student_geo_latitude':  round(geo_latitude, 3),
                'student_geo_longitude': round(geo_longtitude, 3),
                'student_travel_time_minutes': travel_time,
                'student_travel_distance_km': travel_distance,
                'student_future_school_id': randint(1, len(future_schools)),
                'student_class_id': _class['class_id'],
            }

            student_id += 1

            students.append(student)

    return students

def get_competitions():
    competitions = []
    competition_id = 1
    for competition_name in competition_names:
        competition = {
            'competition_name': competition_name,
            'competition_id': competition_id,
        }
        competition_id += 1

        competitions.append(competition)
    return competitions

def get_student_competitions(students,competitions, classes):
    student_competitions = []
    used_students_competitions = []

    for i in range(1, 1000):

        student = choice(students)
        competition = choice(competitions)

        _class = classes[student['student_class_id'] - 1]
        class_year = _class['class_year']

        year = randint(class_year, 2016)

        student_competition = {
            'student_id': student['student_id'],
            'competition_id': competition['competition_id'],
            'student_competition_score': randint(0, 100),
            'student_competition_year': year,
        }

        if (student['student_id'], competition['competition_id']) in used_students_competitions:
            continue

        used_students_competitions.append((student['student_id'], competition['competition_id']))

        student_competitions.append(student_competition)
    return student_competitions