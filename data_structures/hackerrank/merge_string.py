def merge_the_tools(string, k):
    words = []
    for i in range(0, len(string), k):
        vhala = string[i:i+k]
        word = ""
        for char in vhala:
            if char not in word:
                word += str(char)
        
        words.append(word)

    # your code goes here
    # print("\n".join(words))
    return "\n".join(words)

print(merge_the_tools("AABCAAADA", 3))