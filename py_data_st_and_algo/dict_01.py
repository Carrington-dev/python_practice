a = [2, 5, 7, 9]
b = ["man", "children", "teachers", "women"]

context = zip(b, a)
print(context)
context = dict(context)
print(context)


# x = ('key1', 'key2', 'key3')
# y = 0

# thisdict = dict.fromkeys(x, y)


# print(thisdict)

va = context.get("man")
print(va)
va = context.get("men")
print(va)
