# first problem from Problem Solving Challenge
# 🔹 Problem 1: Reverse a String

message="Hello"

print(message[4::-1]) 

 # this slicing reversly it starts from index 4 which is o stop at begining beacuse we are not mentioning ending index , -1 shows reversing order

 # alternatively it can be done like this

reverse_message=message[4::-1]
print(reverse_message)

# we can make the function of it also

def reversed_string(s):
    return s[::-1]
print(reversed_string("hello"))