def closestNumbers(numbers):
    # Write your code here
    differences  = {
        
    }
    difference_list = []
    for i in numbers:
        for j in numbers:
            difference = abs(i - j)
            if difference != 0:
                difference_list.append(difference)
                if difference in differences:
                    if i < j:
                        differences[difference].append((i, j))
                else:
                    if i < j:
                        differences[difference] = [(i, j)]
    
    minimum_dif = min(difference_list)
    
    print(minimum_dif)
    
    pairs = differences[minimum_dif]
    pairs = sorted(pairs)
    
    # print((pair for pair in pairs))
    # print(pairs)
    for pair in pairs:
        # if pair 
        print(pair[0], pair[1])



def closestNumbers(numbers):
    numbers = sorted(numbers)
    difference = 0
    context = {}
    diffs = []
   
    for i in range(len(numbers)-1):
        d = abs(numbers[i] - numbers[i+1])
        diffs.append(d)
        if d in context:
            context[d].append([numbers[i], numbers[i+1]])
        else:
            context[d] = [[numbers[i], numbers[i+1]]]
    
    pre = min(diffs)
    
    pref = context[pre]
    
    for i in pref:
        print(i[0], i[1])

"""
HRW
HERHRWS
"""

def getSubsequenceCount(s1, s2):
    # Write your code here
    count = 0
    for i in range(len(s2)):
        if s2[i:].startswith(s1):
            count += 1
        elif s2.index(s1[0]) < s2.index(s1[1]) and s2.index(s1[1]) < s2.index(s1[2]):
            count += 1
        else:
            pass
    
    return count

def getSubsequenceCount(s1, s2):
    # Write your code here
    count = 0
    context = {
        
    }
    for i in s1:
        for j in range(len(s2)):
            word = s2[j:]
            if i in context:
                context[i].append(word.index(i)+ j)
            else:
                context[i] = [word.index(i) + j]
    
    print(context)
    
    return count

# ecommerce
# clinic 
# word 