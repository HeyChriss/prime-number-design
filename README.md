# Pseudo Code 
A prime number is a number that is only divisible by itself and 1. Thus, 2 is a prime number (the factors are 1 and 2) but 4 is not (the factors are 1, 2, and 4). We are to find all the prime numbers at or below a certain number. For example, the prime numbers at or below 20 are:

{ 2, 3, 5, 7, 11, 13, 17, 19 }

Prime Number Algorithm
To find all the prime numbers below a certain value n, we will start with an array containing n elements. Each element in the array will correspond to a number. We will start by ruling out all the multiples of two greater than 2. Thus, we will cross out the values 4, 6, 8, 10, 12, ... n. We know these values are not prime because they have 2 as a factor (as well as 1 and the number itself).

We will then rule out all the multiples of three greater than 3. Thus we will "cross out" the values 6, 9, 12, 15, 18, ... n. Note that 6, 12, 18 were already crossed out. This shouldn't matter; crossing out a value twice keeps it crossed out.

Next we will rule out all the multiples of four. Notice that 4 is already crossed out! We did that when we went through all the multiples of 2. Thus we can be assured that 4 is not a prime (its factors are 1, 2, and 4).

Next, we will rule out the multiples of five. Since 5 is not crossed out already, we will iterate through all the multiples of five greater than 5: 10, 15, 20, 25, ... n.

This process continues until we attempt to rule out the square root of n. We can stop here because everything above the square root of n is already crossed out. Why is that? See if you can figure it out.

Every number in our array that is not crossed out is prime!
