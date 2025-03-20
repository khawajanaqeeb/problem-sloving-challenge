# problem 3- sum of digit
# this can also be done in many ways 
# simple approach modulus and division

n=1234       # taken non-negative integer
total=0

while n > 0:        # its a loop , which run untill n become 0
    total +=n % 10  # it get the last digit and add it total, %  gives the remainder after division
    n //=10         # it remove the last digit, // gives quotient and ingnore decimal part

print(total)    

print("\n-------------\n")

# now make fucntions for both integer and string

def sum_of_digits(n:int):               # setup function for digits
    return sum(int(digit) for digit in str(n)) # Convert each digit to int and sum them

print(sum_of_digits(1234))      # call function in side print() and pass argument

print("\n-------------\n")

# now function for sum of number

def sum_of_digits(m:int):
    totals=0
    while m > 0:
        totals += m % 10   # get last digit and add total
        m //=10           # remove the last digit and store in n
    return totals

print(sum_of_digits(1234))

print("\n#########################\n")

# now make it for user input

def sum_of_digits(mn:int):
    totals=0
    while mn > 0:
        totals += mn % 10   # get last digit and add total
        mn //=10           # remove the last digit and store in n
    return totals
mn=int(input("Enter the number to get its sum :"))    # since input()return a string we first convert it to integer
print(sum_of_digits(mn))

print("\n_____________________\n")
# use input () for interger also

def sum_of_digits(n:int):               
    return sum(int(digit) for digit in str(n)) # convert each digit to intiger and sum

n=input("enter number to get its sum :")
print(sum_of_digits(n))      # call function in side print() and pass argument
    
        