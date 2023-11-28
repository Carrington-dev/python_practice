from collections import deque

arr = deque()
arr.append(23)
arr.append(34)
arr.append(42)
arr.append(35)
arr.append(24)
print(arr)
arr.rotate(2)
print(arr)

str_arr = deque("I am legit")

# str_arr.append()
print(str_arr)


str_arr.rotate(4)
print(str_arr)