from collections import defaultdict


class Gradebook:
    def __init__(self):
        self._grades = {}

    def add_student(self, name):
        self._grades[name] = defaultdict(list)

    def report_grade(self, name, subject, score, weight):
        by_subject = self._grades[name]
        grade_list = by_subject[subject]
        grade_list.append((score, weight))

    def average_grade(self, name):
        by_subject = self._grades[name]

        score_sum, score_count = 0, 0
        for subject, scores in by_subject.items():
            subject_avg, total_weight = 0, 0
            for score, weight in scores:
                subject_avg += score * weight
                total_weight += weight

        score_sum += subject_avg / total_weight
        score_count += 1
        return score_sum / score_count


book = Gradebook()
book.add_student('Tomasz Kaniecki')
book.report_grade('Tomasz Kaniecki', 'informatyka', 90, 0.05)
book.report_grade('Tomasz Kaniecki', 'WF', 95, 0.15)
book.report_grade('Tomasz Kaniecki', 'angielski', 75, 0.60)

print(book.average_grade('Tomasz Kaniecki'))
