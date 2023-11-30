''' This function brings a number from the user and creates
an array with all of the prime numbers in the range from 
the number given'''
def prime_numbers(n):

    # Creates two lists array = list of booleans
    # and prime_numbers = list of prime numbers. 
    array = []
    prime_numbers = []

    # Appends TRUE in all of the elements in the list
    # with the range from 1 to n (the number the user gave us).
    for i in range(n+1):
        array.append(True)

    # p = the first prime number 
    p = 2

    # This loop helps us create the square root of n, this stops because
    # everything above the square root of n is already crossed out 
    while (p * p <= n):
        
        # If the element is true, then we will mark them as false if 
        # we find a multiple of the number and we stop when we reach n 
        if (array[p] == True):

            # p + p is the multiple and we set as false if the element
            # is in the array 
            for multiple in range(p + p, n+1, p):
                array[multiple] = False

        # else we increment p 
        p += 1

    # append all of the true prime numbers starting from 2 
    for p in range (2, n):
        if (array[p] == True):
            prime_numbers.append(p)

    return print(prime_numbers)


def main():


    number = int(input('Enter a number to know what the prime numbers are: ')) 
    prime_numbers(number) 

if __name__ == "__main__":
    main()


   
