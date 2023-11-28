def reverse(s):
    if len(s) == 0:
        return s
    else:
        return reverse(s[1:]) + s[0]



a= reverse("I am Carrington")
print(a)


def reverse_by_slice(s):
    return s[::-1]

b = reverse_by_slice("I am Carrington")
print(b)


def reversed(s):
    if len(s) == 0:
        return s
    else:
        return reverse(s[1:]) + s[0]
