def middle_grade(curse):
    if curse in grades:
        mid_grade = sum(grades[f'curse']) / count(grades[f'curse'])
    else:
        mid_grade = 'Ошибка'
        return mid_grade

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_for_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.course and course in lecturer.course:
            if course in lecturer.grades_from_students:
                lecturer.grades_from_students[course] += [grade]
            else:
                lecturer.grades_from_students[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        name = f'Имя: {self.name}'
        surname = f'Фамилия: {self.surname}'
        middle_grade = f'Средняя оценка за домашнее задание: {middle_grade()}'
        courses_in_progress = f'Курсы в процессе изучения: {self.courses_in_progress}'
        finished_courses = f'Завершенные курсы: {self.finished_courses}'
        return name, surname, middle_grade, courses_in_progress, finished_courses

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, grades_from_students, course):
        self.grades_from_students = {}
        self.course = []

    def __str__(self):
        name = f'Имя: {self.name}'
        surname = f'Фамилия: {self.surname}'
        grade = f'Средняя оценка за лекции: {middle_grade()}'
        return name, surname, grade



class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        name = f'Имя: {self.name}'
        surname = 'Фамилия: {self.surname}'
        return name, surname

    def __lt__(self, other):
        self.grade = middle_grade()
        other.grade = middle_grade()
        if isinstance(other, Reviewer):
            print('Ошибка')
            return
        return self.grade > other.grade


 
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
 
cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
 
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
 
print(best_student.grades)