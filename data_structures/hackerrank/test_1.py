def transformSentence(sentence):
    # Write your code here
    sent_arr = sentence.split(" ")
    for i in range(len(sent_arr)):
        word = sent_arr[i]
        # print(word)
        # first_letter = word[0]
        # second_letter = word[1]
        # if first_letter > second_letter:
        for j in range(len(word)-1):
            print(word[j], word[j+1])
            if word[0]:
                pass
            if word[j] > word[j+1]:
                word.replace(word[j], word[j].lower())
                # word[j] = word[j].lower()
            elif word[j] == word[j+1]:
                pass
            else:
                word.replace(word[j], word[j].upper())
                # word[j] = word[j].upper()
        
        sent_arr[i] = word
    
    sentence = " ".join(sent_arr)
    print(sentence)


transformSentence("a Blue MOON")
transformSentence("a Hole World")