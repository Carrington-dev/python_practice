# # t1 = [1, 2 ,4]
# # t2 = [5, 7, 9, 34]

# # t3 = t1 + t2
# # print(t3)

# Y = [2, 5j, 6]
# Y.sort()
# print(Y)

f = None
for i in range(5):
    with open("app.log", "w") as f:
        if i > 2:
            break

print(f.closed)

# # data = [ 1, 2, 3]
# # def incr(x):
# #     return x + 1

# # print(list(map(incr, data)))

# # skills = ['NodeJs', "Python","ReactJs", "VueJs"]

# # skills.add(3,'java')
# # print(skills)

# class Foo():
    
#     def __init__(self, *args, **kwargs):
#         super(Foo, self).__init__(*args, **kwargs)

# A = Foo()
# B = Foo()
# print(A + B)

# import  re
# result = re.findall("Welcome to Turing", 'Welcome',1)
# print(result)


# al = 'abcd'

# for i in range(len(al)):
#     al[i].upper()

# print(al)