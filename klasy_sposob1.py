class Gradebook:
    def __init__(self):
        self._grades = {}

    def add_student(self, name):
        self._grades[name] = []

    def report_grade(self, name, score):
        self._grades[name].append(score)

    def average_grade(self, name):
        grades = self._grades[name]
        return sum(grades) / len(grades)


book = Gradebook()
book.add_student('Tomasz Kaniecki')
book.report_grade('Tomasz Kaniecki', 90)
book.report_grade('Tomasz Kaniecki', 95)
book.report_grade('Tomasz Kaniecki', 75)

print(book.average_grade('Tomasz Kaniecki'))
