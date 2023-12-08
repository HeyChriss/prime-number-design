# Prime Number Algorithm  
A prime number is a number that is only divisible by itself and 1. Thus, 2 is a prime number (the factors are 1 and 2) but 4 is not (the factors are 1, 2, and 4). We are to find all the prime numbers at or below a certain number. For example, the prime numbers at or below 20 are:

                        `{ 2, 3, 5, 7, 11, 13, 17, 19 }`

Prime Number Algorithm
To find all the prime numbers below a certain value n, we will start with an array containing n elements. Each element in the array will correspond to a number. We will start by ruling out all the multiples of two greater than 2. Thus, we will cross out the values 4, 6, 8, 10, 12, ... n. We know these values are not prime because they have 2 as a factor (as well as 1 and the number itself).

We will then rule out all the multiples of three greater than 3. Thus we will "cross out" the values 6, 9, 12, 15, 18, ... n. Note that 6, 12, 18 were already crossed out. This shouldn't matter; crossing out a value twice keeps it crossed out.

Next we will rule out all the multiples of four. Notice that 4 is already crossed out! We did that when we went through all the multiples of 2. Thus we can be assured that 4 is not a prime (its factors are 1, 2, and 4).

Next, we will rule out the multiples of five. Since 5 is not crossed out already, we will iterate through all the multiples of five greater than 5: 10, 15, 20, 25, ... n.

This process continues until we attempt to rule out the square root of n. We can stop here because everything above the square root of n is already crossed out.

Every number in our array that is not crossed out is prime!

Pseudo code and program trace might be found in the pdf attached to this repository 

## Pseudo Code 
```
PROMPT number 
GET number 
     FOR I in range of number
        Array  True
P  2 
WHILE ( p * p <= number )
    IF array[p]  True
        FOR I in range (p+p, number, p) 
            Array[i]  False
        ELSE
            P += 1 
FOR p in range (2, number)
    IF array[p] == True
        Prime numbers  p 
PRINT Prime numbers

```

## Algorithmic Efficiency

The time complexity for this algorithm is O(n log n) because we are using many loops in this algorithm. The first one in line 3 because we are appending everything as True and that is O(n). There is another loop in line 6 and an inner loop in line 8 which makes it O (n log n) because we take the first loop and then we loop again until we break the first loop. There is another loop to append all of the true numbers in the new list prime numbers and that is O(n), This might be a good algorithm because it is fast for smaller numbers but might take a little bit longer if we have a long number because then the data increases. 

