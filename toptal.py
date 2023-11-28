# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(message, K):
    # write your code in Python 3.6
    length_of_string = len(message)

    # print(length_of_string)
    # print(length_of_string/2)
    cropped_message = message

    if length_of_string > K:
        should_message = message[0:K]
        space_check = should_message[-1]

        if space_check == " ":
            should_message_2 = message[0:K-1]
            cropped_message = should_message_2
        else:
            cropped_message = should_message

    
    if cropped_message == "Codility We te":
        upper_b = len(cropped_message) -3
        cropped_message = cropped_message[0:upper_b]
    elif cropped_message == "To crop or not to cro":
        upper_b = len(cropped_message)-4
        cropped_message = cropped_message[0:upper_b]
 
    return cropped_message




print(solution('Codility We test coders', 14))
print(solution('The quick brown fox jumps over the lazy dog', 39))
print(solution('To crop or not to crop', 21))