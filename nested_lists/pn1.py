Number = int(input())
marksheet = []



def inputTaker(N=Number):
    for i in range(N):
        for _ in range(0,Number):
            marksheet.append([input(''), 
                float(input(''))])
    
        print(marksheet)
        


inputTaker(Number)