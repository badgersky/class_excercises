import csv


class Student:

    def __init__(self, name, surname, school_class, birth_year, grade_avg):
        self.name = name
        self.surname = surname
        self.school_class = school_class
        self.birth_year = int(birth_year)
        self.grade_avg = float(grade_avg)

    @classmethod
    def from_file(cls, file, class_name=None):
        students = []
        with open(file, 'r') as f:
            for row in csv.reader(f):
                if class_name is None or class_name == row[2]:
                    students.append(cls(row[0], row[1], row[2], row[3], row[4]))
        return students

                    
