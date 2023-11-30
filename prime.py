def prime_numbers(n):
    array = []
    prime_numbers = []
    for i in range(n+1):
        array.append(True)

    p = 2

    while (p * p <= n):

        if (array[p] == True):
            for i in range(p * p, n+1, p):
                array[i] = False

        p += 1

    for p in range (2, n):
        if (array[p] == True):
            prime_numbers.append(p)

    return print(prime_numbers)



number = int(input('Enter a number to know what the prime numbers are: ')) 
prime_numbers(number) 
   
