def f(n):
    if n <= 1:
        return n
    else:
        return f(n-1) + f(n-2)

print(f(6))

# def fab_list(n):
#     lis = []
#     if n == 0:
#         lis = [0]
#     if n == 1:
#         lis = [0, 1]
#     else:
#         for 