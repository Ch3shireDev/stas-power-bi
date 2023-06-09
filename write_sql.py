
import pyodbc

def get_cursor(server, database, username=None, password=None, trusted_connection=True):
    if trusted_connection:
        conn = pyodbc.connect(f'Driver={{SQL Server Native Client 11.0}};Server={server};Database={database};Trusted_Connection=yes;')
    else:
        conn = pyodbc.connect(f'Driver={{SQL Server Native Client 11.0}};Server={server};Database={database};username={username};password={password};')
    return conn.cursor()
 

def clear_tables(cursor, script):
    cursor.execute(script)

def write_future_schools(cursor, future_schools):
    
    for future_school in future_schools:
        cursor.execute("INSERT INTO [FUTURE_SCHOOLS] (FUTURE_SCHOOL_ID, FUTURE_SCHOOL_NAME, FUTURE_SCHOOL_GEO_LATITUDE, FUTURE_SCHOOL_GEO_LONGTITUDE) VALUES (?,?,?,?)", future_school['school_id'], future_school['school_name'], future_school['school_geo_latitude'], future_school['school_geo_longtitude'])

def write_classes(cursor, classes):
        
    for _class in classes:
        cursor.execute("INSERT INTO [CLASSES] (CLASS_ID, CLASS_LETTER, CLASS_NAME, CLASS_YEAR, CLASS_DESCRIPTION) VALUES (?,?,?,?,?)", _class['class_id'], _class['class_letter'], _class['class_name'], _class['class_year'], _class['class_description'])

def write_competitions(cursor, competitions):    
    for competition in competitions:
        cursor.execute("INSERT INTO [COMPETITIONS] (COMPETITION_ID, COMPETITION_NAME) VALUES (?,?)", competition['competition_id'], competition['competition_name'])

def write_students(cursor, students):
    
    for student in students:
        cursor.execute("INSERT INTO [STUDENTS] (STUDENT_ID, STUDENT_FIRST_NAME, STUDENT_LAST_NAME, STUDENT_GENDER, STUDENT_GEO_LATITUDE, STUDENT_GEO_LONGITUDE, STUDENT_TRAVEL_TIME_MINUTES, STUDENT_TRAVEL_DISTANCE_KM, STUDENT_FUTURE_SCHOOL_ID, STUDENT_CLASS_ID) VALUES (?,?,?,?,?,?,?,?,?,?)", student['student_id'], student['student_first_name'], student['student_last_name'], student['student_gender'], student['student_geo_latitude'], student['student_geo_longitude'], student['student_travel_time_minutes'], student['student_travel_distance_km'], student['student_future_school_id'], student['student_class_id'])

def write_student_competitions(cursor, student_competitions):

    for student_competition in student_competitions:
        cursor.execute("INSERT INTO [STUDENT_COMPETITIONS] (STUDENT_ID, COMPETITION_ID, STUDENT_COMPETITION_YEAR) VALUES (?,?,?)", student_competition['student_id'], student_competition['competition_id'], student_competition['student_competition_year'])

def commit(cursor):
    cursor.commit()

def close(cursor):
    cursor.close()