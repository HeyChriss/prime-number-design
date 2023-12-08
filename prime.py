# 1. Name:
#      Christian Mijangos.
# 2. Assignment Name:
#      Lab 13: Prime Numbers.
# 3. Assignment Description:
#      The purpose of this program is to create a list with all of 
#      the possible prime numbers from an specific number. 
#      We do this by summing and finding factorization from the 
#      number given. 
# 4. What was the hardest part? Be as specific as possible.
#      Finding a way to use a sentinel controlled for loop 
#      was a challenge at the beginning and looking for asserts
#      was also a challenge because I did not know how to create
#      them nor the location where I needed to put them. 
# 5. How long did it take for you to complete the assignment?
#      This assignment took me approximately 3 hours 

'''
This functions takes a number and makes a list of 
prime numbers 
'''
def prime_numbers(n):

    array = [] # List of booleans [True, True...]
    prime_numbers = [] #List of prime numbers [2, 3 ...]

    # Appends (n) elements as True 
    for i in range(n+1):
        array.append(True)
    
        # Assert if the list is empty
    assert len(array) > 0,"The list is empty, there are no" \
                                "prime numbers"    

    # There are two loops in this part. 
    # The outer loop is an sentinel-controlled loop and this is 
    # indicating it starts from number 2 and stops in the square root
    # of the number 
    for p in range(2, int(n**0.5) + 1):
        if array[p]:

            # This is where we check the factorization summing the 
            # numbers and putting them as false 
            # for i in range(start, stop, step):
            for i in range(p + p, n + 1, p):
                array[i] = False

    # Appends all of the booleans that are left as True in the
    # new list prime_numbers
    for p in range (2, n+1):
        if (array[p] == True):
            prime_numbers.append(p)

    # Assert if the list is empty
    assert len(prime_numbers) > 0,"The list is empty, there are no" \
                                "prime numbers"        

    return prime_numbers

# Error Handling
try: 
    # Asks for a new number 
    number = int(input('Enter a number to know what the '
                        'prime numbers are: ')) 

    # Assertion if a number is negative
    assert number >= 0, "The number is negative" 

    # User Error Correction if number is less than 2 
    if number < 2:
        print ("Please use another number")
    else:   
        result = prime_numbers(number)
        print("Prime numbers:", result)

except ValueError:
    # Handle the case where the input is not a valid integer
    print("Error: Please enter a valid integer.")
except AssertionError as e:
    print(f"Assertion Error: {e}")

   
