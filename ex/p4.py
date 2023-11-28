def minion_game(s):
    # your code goes here
    # Enter your code here. Read input from STDIN. Print output to STDOUT
    vowels = ['A', 'E', 'I', 'O', 'U']
    
    
    a = 0
    b = 0
    for i, c in enumerate(s):
        if c in vowels:
            b += len(s) - i
        else:
            a += len(s) - i
            
    if a == b:
        print("Draw") 
    elif a > b:
        print ('Stuart {}'.format(a))
    else:
        print ('Kevin {}'.format(b))


s = input()

minion_game(s)