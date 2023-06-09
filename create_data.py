from lib import get_future_schools, get_classes, get_students, get_competitions, get_student_competitions
import write_json
import write_sql
import write_csv

future_schools = get_future_schools()
classes = get_classes()
students = get_students(future_schools, classes)
competitions = get_competitions()
student_competitions = get_student_competitions(students, competitions, classes)


write_json.write_classes(classes)
write_json.write_future_schools(future_schools)
write_json.write_students(students)
write_json.write_competitions(competitions)
write_json.write_student_competitions(student_competitions)

 
cursor = write_sql.get_cursor('localhost', 'school_db', trusted_connection=True)
write_sql.clear_tables(cursor, open('clear_tables.sql', 'r').read())
write_sql.write_future_schools(cursor, future_schools)
write_sql.write_classes(cursor, classes)
write_sql.write_students(cursor, students)
write_sql.write_competitions(cursor, competitions)
write_sql.write_student_competitions(cursor, student_competitions)
write_sql.commit(cursor)
write_sql.close(cursor)

write_csv.write_classes(classes)
write_csv.write_future_schools(future_schools)
write_csv.write_students(students)
write_csv.write_competitions(competitions)
write_csv.write_student_competitions(student_competitions)