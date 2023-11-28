


#
# Complete the 'stringAnagram' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY dictionary
#  2. STRING_ARRAY query
#

def stringAnagram(dictionary, query):
    # Write your code here
    count_list = []
    
    for i in dictionary:
        index = dictionary.index(i)
        sorted_chars = sorted(i)
        i = "".join(sorted_chars)
        dictionary[index] = i
    
    for j in query:
        
        index = query.index(j)
        sorted_char = sorted(j)
        j = "".join(sorted_char)
        query[index] = j
    
    for j in query:        
        count_list.append(dictionary.count(j))
    
    
            
    print(dictionary)      
    
    return count_list


cat = ['cat', 'cta', 'atc', 'act', 'tac', 'tca', "acg", "cag", "cga"]
cat2 = ['cat', "cag"]
print(stringAnagram(cat, cat2))

