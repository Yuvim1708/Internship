#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Q11: Python Program to Find the Factorial of a Number

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Example usage
num = int(input("Enter a number: "))
print(f"The factorial of {num} is {factorial(num)}")


# In[3]:


# Q12: Python Program to Find Whether a Number is Prime or Composite

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Example usage
num = int(input("Enter a number: "))
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is a composite number.")


# In[5]:


# Q13: Python Program to Check Whether a Given String is Palindrome or Not

def is_palindrome(s):
    return s == s[::-1]

# Example usage
string = input("Enter a string: ")
if is_palindrome(string):
    print(f"'{string}' is a palindrome.")
else:
    print(f"'{string}' is not a palindrome.")


# In[7]:


# Q14: Python Program to Get the Third Side of a Right-Angled Triangle from Two Given Sides

import math

def third_side_of_right_triangle(a, b):
    # Hypotenuse calculation
    hypotenuse = math.sqrt(a**2 + b**2)
    return hypotenuse

# Example usage
side1 = float(input("Enter the length of the first side: "))
side2 = float(input("Enter the length of the second side: "))
print(f"The length of the hypotenuse is {third_side_of_right_triangle(side1, side2)}")


# In[9]:


# Q15: Python Program to Print the Frequency of Each of the Characters Present in a Given String

from collections import Counter

def char_frequency(s):
    return Counter(s)

# Example usage
string = input("Enter a string: ")
frequency = char_frequency(string)
print("Character frequencies:")
for char, freq in frequency.items():
    print(f"{char}: {freq}")

