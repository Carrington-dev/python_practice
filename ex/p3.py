def solve(s):
    my_list = s.split(" ")

    for i in range(len(my_list)):
        
        word = my_list[i]
        word = word.capitalize()
        my_list[i] = word
    
    s = " ".join(my_list)

    return s

print(solve("alison heck"))
print(solve("1 w 2 r 3g"))