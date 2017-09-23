class StudentList(list):
    def __init__(self, name, age, classmates=None):
        if classmates is None:
            classmates = []
        self.name = name
        self.age = age
        list.__init__([])
        self.extend(classmates)

    def oldest3classmate(self):
        return sorted([stu.age for stu in self], reverse=True)[0:3], True


student = StudentList('a', 5, [StudentList('b', 6), StudentList('b', 10), StudentList('c', 8), StudentList('d', 9)])
oldest_classmate, flag = student.oldest3classmate()
print oldest_classmate
print flag
