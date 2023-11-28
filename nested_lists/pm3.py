from operator import itemgetter

n = int(input())
students = []
for n in range(n):
    students.append([input(), float(input())])

lowest = sorted(set(map(itemgetter(1), students)))[1]
for student in sorted(filter(lambda l: l[1] == lowest, students)):
    print(student[0])