def transformSentence(sentence):
    words = sentence.split()
    a = ""
    for word in words:
        a += word[0]
        # print(sentence[i], sentence[i+1])
        for j in range(1, len(word)):
           
            
            if word[j-1].lower() > word[j].lower():
                a += word[j].lower()
            elif word[j-1].lower() < word[j].lower():
                a += word[j].upper()
            else:
                a += word[j]

        a += " "
                
    print(a[:-1:])

    return a[:-1:]


transformSentence("a Hole World")