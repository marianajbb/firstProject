
import random
from datetime import datetime
import random

#write a script which can ceil and floor ...
x = 3.4
def floor(x):
    if isinstance(x, int):
        return x
    else:
     return int(x)
print(floor(x))

def ceil(x):
    if isinstance(x, int):
        return x
    else:
        return int(x)+1
print(ceil(x))


# Python script to swat to integers in single line

a, b = 2, 3
a, b = b, a
print(a, b)


#write a program that asks the user their name ...

print("what is your name ")
name = input()

message = "great, nice to meet you" if name == "John Cleese" or name == "Michael Palin" \
    else "That is a nice name" if name == "Mariana Bastardo"\
        else "you have a nice name"

print(message)

# A particular retailer is having a 60% off ...

prices = [4.95, 9.95, 14.95, 19.95, 24.95]
discount = 0.60
print("Original Price | Discount Amount | New Price")
for price in prices:
    discountAmount = round(price * discount, 2)
    newPrice = round(price - discountAmount, 2)

    print(f"${price: 7.2f} | ${discountAmount: 7.2f} | ${newPrice: 7.2f}")

# print a table, write a program that displays the following table ...

def power(a , b):
    result = 1
    for _ in range(b):
        result *= a
    return result

print("a b pow(a,b)")
data = [(1,2),(2,3),(3,4),(4,5),(5,6)]
for a, b in data:
    powerResult = power(a, b)
    print(f"{a} {b} {powerResult}")

# game Lottery

def lottery() :
    lotteryNumber = random.randint(100,999)
    print("Please enter a number between 100 and 999")
    number = int(input())

    if number == lotteryNumber:
        print("The award is 10.000")
    else:
        sortedLottery = sorted(str(lotteryNumber))
        sortedNumber = sorted(str(number))

        if sortedNumber == sortedLottery:
            print("The award is 3000")
        else:
            lotteryStr = str(lotteryNumber)
            numberStr = str(number)
            match = False
            for digit in numberStr:
                if digit in lotteryStr:
                    match = True
                    break
            if match:
                print("The award is 1000")
            else:
                print("The award is 0")

lottery()

#ocurrence of max numbers

def occurence():
    numbers =[]
    while True :
        print("Please enter a number between 1 to 9, press 0 to stop")
        number = int(input())
        if number == 0:
            break
        numbers.append(number)

    if not numbers:
        return

    maxNumber = max(numbers)
    count = numbers.count(maxNumber)

    print(f"The largest number is: {maxNumber}")
    print(f"The occurrence count of the largest number is: {count}")

occurence()

#write a program to display the following series

def displayAsterisks(rows):
    for i in range (1, rows + 1):
        spaces = " " * (rows - i)
        asterisks = "* " * i
        print(spaces + asterisks)

displayAsterisks(5)

# write a program that display the following series
def generate_series(n):

    for i in range(0, n):
        for j in range(i + 1, n + 1):
            print(j, end="")
        print()

    for i in range(n, 0, -1):
        for j in range(i, n + 1):
            print(j, end="")
        print()


generate_series(7)


# The international standard letter...

def translate_phone_number(phone_number):

    translation = str.maketrans({
        'A': '2', 'B': '2', 'C': '2',
        'D': '3', 'E': '3', 'F': '3',
        'G': '4', 'H': '4', 'I': '4',
        'J': '5', 'K': '5', 'L': '5',
        'M': '6', 'N': '6', 'O': '6',
        'P': '7', 'Q': '7', 'R': '7', 'S': '7',
        'T': '8', 'U': '8', 'V': '8',
        'W': '9', 'X': '9', 'Y': '9', 'Z': '9',
        'a': '2', 'b': '2', 'c': '2',
        'd': '3', 'e': '3', 'f': '3',
        'g': '4', 'h': '4', 'i': '4',
        'j': '5', 'k': '5', 'l': '5',
        'm': '6', 'n': '6', 'o': '6',
        'p': '7', 'q': '7', 'r': '7', 's': '7',
        't': '8', 'u': '8', 'v': '8',
        'w': '9', 'x': '9', 'y': '9', 'z': '9'
    })

    translated_number = phone_number.translate(translation)
    return translated_number

phone_number = input("Enter a string: ")

translated_number = translate_phone_number(phone_number)
print(translated_number)

#find all the prime numbers in a range
def is_prime(num):

    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_primes_in_range(start, end):
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes


start_range = int(input("enter the starting number"))
end_range = int(input("enter the ending number"))

prime_numbers = find_primes_in_range(start_range, end_range)

print(f"Prime numbers within the range {start_range} to {end_range}:")
print(prime_numbers)

#Reverse of a given integer number

def reverse_integer(num):

    reversed_num = 0
    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10
    return reversed_num

num = int(input("Enter an integer number with more than 2 digits: "))

reversed_num = reverse_integer(num)
print("Reverse of the number:", reversed_num)

# total number of days between two dates

def days_between_dates(date_one, date_two):
    date_format = "%Y-%m-%d"
    date1 = datetime.strptime(date_one, date_format).date()
    date2 = datetime.strptime(date_two, date_format).date()
    days_difference = abs((date2 - date1).days)
    return days_difference


date1 = input("Enter the first date (YYYY-MM-DD): ")
date2 = input("Enter the second date (YYYY-MM-DD): ")

days_difference = days_between_dates(date1, date2)
print("Total number of days between the dates:", days_difference)


#generate 2 random numbers

import random

def generate_product_of_random_numbers():

    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)

    product = num1 * num2
    return product

product = generate_product_of_random_numbers()
print("The product of two random numbers is:", product)