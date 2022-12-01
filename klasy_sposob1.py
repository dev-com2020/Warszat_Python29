from collections import defaultdict


class Gradebook:
    def __init__(self):
        self._grades = {}

    def add_student(self, name):
        self._grades[name] = defaultdict(list)

    def report_grade(self, name, subject, grade):
        by_subject = self._grades[name]
        grade_list = by_subject[subject]
        grade_list.append(grade)

    def average_grade(self, name):
        by_subject = self._grades[name]
        total, count = 0, 0
        for grades in by_subject.values():
            total += sum(grades)
            count += len(grades)
        return total / count


book = Gradebook()
book.add_student('Tomasz Kaniecki')
book.report_grade('Tomasz Kaniecki', 'informatyka', 90)
book.report_grade('Tomasz Kaniecki', 'WF', 95)
book.report_grade('Tomasz Kaniecki', 'angielski', 75)

print(book.average_grade('Tomasz Kaniecki'))
