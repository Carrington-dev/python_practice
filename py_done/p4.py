def squareList(number):
    an_list = []
    a_list = list(range(0, number))
    for i in a_list:
        i_square = i**2
        an_list.append(i_square)
    
    for j in an_list:
        print(j)
    # pr2int(an_list) 

if __name__ == '__main__':
    n = int(input())
    squareList(n)
