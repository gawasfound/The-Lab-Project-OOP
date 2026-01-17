class Teacher:
    def __init__(self, teacher_id, name):
        self.__teacher_id = teacher_id
        self.__name = name

class Subject:
    def __init__(self, subject_code, subject_name, credit_hours):
        self.__subject_code = subject_code
        self.__subject_name = subject_name
        self.__credit_hours = credit_hours
        self.__teacher = None

    def assign_teacher(self, teacher):
        self.__teacher = teacher

    def get__credit_hours(self):
        return self.__credit_hours
    
    def get_teacher(self):
        return self.__teacher

    
class Enrollment:
    def __init__(self, student, subject, grade=None):
        self.__student = student
        self.__subject = subject
        self.__grade = grade

    def set_grade(self, grade):
        self.__grade = grade

    def get_student(self):
        return self.__student

    def get_subject(self):
        return self.__subject

    def get_grade(self):
        return self.__grade
