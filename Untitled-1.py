class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, reviews):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.finished_courses: # proverit chto lector i student zakrepleny za kursom
            if course in lecturer.reviews:
                lecturer.reviews[course] += [reviews]
            else:
                lecturer.reviews[course] = [reviews]
        else:
            return 'Ошибка'

    def gpa(self):
        
        for k, n in self.grades.items():
            result = 0
            result = result + sum(n)/ float(len(n))
            return result

    def __str__(self):
        return f'Name: {self.name}\n Surname: {self.surname}\n Courses in progress: {", ".join(self.courses_in_progress)}\n Courses completed: {", ".join(self.finished_courses)}\n GPA: {self.gpa()}' 

    def __lt__(self, student):
        return self.gpa() < student.gpa()

        
class Mentor:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.courses_attached = []

class Reviewer(Mentor):
    def __init__(self, name, surname, gender):
        super().__init__(name, surname, gender)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Name: {self.name}\n Surname: {self.surname}' 

class Lecturer(Mentor):
    def __init__(self, name, surname, gender):
        super().__init__(name, surname, gender)
        self.reviews = {}

    def aver(self):
        result = 0
        for k, n in self.reviews.items():
            result = result + sum(n)/ float(len(n))
            return result

    def __str__(self):
            return f'Name: {self.name}\n Surname: {self.surname}\n GPA: {self.aver()}' 


    def __lt__(self, lector):
        return self.aver() < lector.aver()

best_student1 = Student('Ruoy', 'Eman', 'your_gender')
best_student2 = Student('Frank', 'Ford', 'male')
best_student1.courses_in_progress += ['Python']
best_student1.finished_courses += ['Git']
best_student2.courses_in_progress += ['Java']
best_student2.finished_courses += ['Git']
best_student1.finished_courses += ['Python']
best_student2.finished_courses += ['Python']


cool_reviewer = Reviewer('Some', 'Buddy', 'somegender')
cool_reviewer = Reviewer('Some', 'Buddy', 'somegender')
cool_reviewer.courses_attached += ['Python']

 
cool_reviewer.rate_hw(best_student1, 'Python', 10)
cool_reviewer.rate_hw(best_student2, 'Python', 10)
cool_reviewer.rate_hw(best_student1, 'Python', 8)

cool_lecturer = Lecturer ('Vasiliy', 'Pupkin', 'Male')
cool_lecturer.courses_attached += ['Python']
cool_lecturer2 = Lecturer ('Ben', 'Big', 'Male')
cool_lecturer2.courses_attached += ['Python']

best_student1.rate_lecturer(cool_lecturer, "Python", 9)
best_student2.rate_lecturer(cool_lecturer, "Python", 8)
best_student1.rate_lecturer(cool_lecturer2, "Python", 3)
best_student2.rate_lecturer(cool_lecturer2, "Python", 4)

print(best_student1)
print(cool_reviewer)
print(cool_lecturer)

print(cool_lecturer < cool_lecturer2)

