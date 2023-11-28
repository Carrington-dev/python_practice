class Student:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        a = self.a + other.a
        b = self.b + other.b

        return Student(a, b)


    def __mul__(self, other):
        a = self.a * other.a
        b = self.b * other.b

        return Student(a, b)

    def __sub__(self, other):
        a = self.a - other.a
        b = self.b - other.b

        return Student(a, b)

    def __div__(self, other):
        a = self.a / other.a
        b = self.b / other.b

        return Student(a, b)


s1 = Student(23, 56)
s2 = Student(34, 67)

s3 = s1 + s2
print(s3.a, s3.b)

s3 = s1 * s2
print(s3.a, s3.b)


s3 = s1 / s2
print(s3.a, s3.b)

s3 = s1 - s2
print(s3.a, s3.b)


    
