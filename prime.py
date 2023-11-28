def prime_numbers(user_number):
    array = []

    for i in range(1, user_number + 1):
        array.append(i)

    return print(array)   



number = int(input('Enter a number to know what the prime numbers are: ')) 
prime_numbers(number)      
