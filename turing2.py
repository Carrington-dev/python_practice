def findJudge(N, trust) ->int:
    # print(len(trust))
    keys_c = [] # Returns list of non judges
    value_c = [] # Returns list of possible judges
    the_judge = -1
    list_of_judges = []
    
    """Grouping possible judges and other people separately"""

    for item in trust:
        keys_c.append(item[0])
        value_c.append(item[1])

    # print(keys_c)
    # print(value_c)
    
    # print(keys_c.count(3))
    # print(value_c.count(3))

    """Trying to find out if the possible judge is not in a group of people who trust the judge"""

    for item in value_c:
        if len(keys_c) > 1:
            if value_c.count(item) > 1 and item not in keys_c:
                """Trying to avoid duplicate judges"""
                if item not in list_of_judges:
                    list_of_judges.append(item)
                    the_judge = list_of_judges[0]
        
        elif len(keys_c) == 1:
            if value_c.count(item) >= 1 and item not in keys_c:
                """Trying to avoid duplicate judges"""
                if item not in list_of_judges:
                    list_of_judges.append(item)
                    the_judge = list_of_judges[0]
        
        else:
            pass
                
                
    result = the_judge
    return result

   


print(findJudge(2, [[1, 2]]))
print(findJudge(3, [[1, 3], [2, 3]]))
print(findJudge(3, [[1, 3], [2, 3], [3, 1]]))
print(findJudge(3, [[1, 2], [2, 3]]))    
print(findJudge(4, [[1, 3], [1, 4],[2, 3], [2, 4], [4, 3]]))


