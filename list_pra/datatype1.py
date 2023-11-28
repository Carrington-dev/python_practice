def listMaxFinder(list):
    scores = (list)
    max_score = 0
    for i in scores:
        if i > max_score:
            max_score = i
    print(scores[-3])
    print(max(list))
    
    # scores.remove(max(list))

score_list = [ 1, 3 ,4 , 6, 7, 8, 11, 11]
listMaxFinder(score_list)