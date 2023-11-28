def findSum(arr, sumExpected):
    new_dic = dict(zip(arr, arr))
    answer  = False

    for key in new_dic.keys(): 
        if new_dic.get(sumExpected - key) != None and (sumExpected - key) != key:
            answer = True 
        else:
            pass
    

    print(answer)

    """This algorithm is order of O(n)"""

    return answer

arr = [2, 7, 8, 3, 5, 23]
findSum(arr, 9)

arr = [2, 7, 8, 3, 5, 23, 12, 10]
findSum(arr, 20)
    
arr = [2, 7, 8, 13, 17, 18, 12, 10]
findSum(arr, 30)