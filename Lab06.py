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

 class Student:
    def __init__(self, student_id, name):
        self.__student_id = student_id
        self.__name = name
        self.__enrollments = []

    def enroll(self, subject):
        if isinstance(subject, str):
            return 
Error
        for e in self.__enrollments:
            if e.get_subject() == subject:
                return Already
Enrolled
        self.__enrollments.append(Enrollment(self, subject))
        return Done        

    def get_enrolled_subjects(self):
        return [e.get_subject() for e in self.__enrollments]

    def assign_grade(self, subject, grade):
        for e in self.__enrollments:
            if e.get_subject() == subject:
                e.set_grade(grade)
                return Done
        return Not
Found

    def get_gps(self):
        total_points = 0
        total_credits = 0
        for e in self.__enrollments:
            grade = e.get_grade()
            if grade:
                if grade == A:
                    grade_points = 4
                elif grade == B:
                    grade_points = 3
                elif grade == C:
                    grade_points = 2
                elif grade == D:
                    grade_points = 1
                elif grade == F:
                    grade_points = 0
                else:
                    grade_points = 0
                credit_hours = e.get_subject().get__credit_hours()
                total_points += grade_points * credit_hours
                total_credits += credit_hours
        if total_credits == 0:
            return 0.0
        return total_points / total_credits
    
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
