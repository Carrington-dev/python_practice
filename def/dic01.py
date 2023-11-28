
def Average(lst):
    return sum(lst) / len(lst)
  
# Driver Code
# lst = [15, 9, 55, 41, 35, 20, 62, 49]
# average = Average(lst)
def floating_decimals(f_val, dec):
    prc = "{:."+str(dec)+"f}" #first cast decimal as str
    # print(prc) #str format output is {:.3f}
    return prc.format(f_val)




if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    my_list = student_marks[f'{query_name.title()}']


    av = Average(my_list)
    print(floating_decimals(av, 2))
    