# 💡Problem 2-Count Vowels in a string
# since there are many ways to solve this problem but we have to use loop as directed in problem

string="Apple"
vowels="a,e,i,o,u"
count=0

for char in string.lower():
    if char in vowels:
        count +=1

print("vowels in",string,count)

print("\n*************\n")

# we can make function of it also

def  count_vowels(s:str):
    
    vowels = {"a","e","i","o","u"}   # we creat set of vowels to check
    count=0                          # initialize the counter at 0

    for char in s.lower():          # make all characters in our variable s in lower case
        if char in vowels:
            count +=1             # this will increas the value of count as long as char found in vowels

    return count                   # will return the final value in counter

print("vowels in given string are",count_vowels("acknowlegement")) # call the function in print function and pass the any required argument

print("\n~~~~~~~~~~~~~~~~~\n")

# we can make it user input given program also

def  count_vowels(s:str):
    
    vowels = {"a","e","i","o","u"}   # we creat set of vowels to check
    count=0                          # initialize the counter at 0

    for char in s.lower():          # make all characters in our variable s in lower case
        if char in vowels:
            count +=1             # this will increas the value of count as long as char found in vowels

    return count                   # will return the final value in counter

# now take use input
s=input("Enter word for counting vowels :")
print(f"vowels in {s} are",count_vowels(s))
