def merge_the_tools(string, k):
    
    for i in range(0, len(string)+1, k):
        word = string[i:i+k]
        unique_string = ''
        for char in word:
            if char in unique_string:
                pass
            else: unique_string += char
    
    
        print(unique_string)

    

    
# def merge_the_tools(string, k):
#     for i in range(0, len(string), k):
#         uniq = ''
#         for c in string[i : i+k]:
#             if (c not in uniq):
#                 uniq+=c
#         print(uniq)

merge_the_tools("AAABCADDE", 3)
merge_the_tools("AABCAAADA", 3)
