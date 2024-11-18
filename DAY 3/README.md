## Modulus Operator (%) in Python
The modulus operator (%) in Python is used to compute the remainder when one number is divided by another. This operator is widely used in programming for various tasks like determining parity, cycling values, and handling modular arithmetic.

## Syntax
python
Copy code
remainder = a % b
a: Dividend (the number to be divided).
b: Divisor (the number dividing).
Returns the remainder of a ÷ b.
## Use Cases
1. Determine if a Number is Even or Odd
python
Copy code
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("Even")
else:
    print("Odd")
2. Cycle Through Values
python
Copy code
for i in range(10):
    print(i % 3)  # Outputs: 0, 1, 2, 0, 1, 2...
3. Check Divisibility
python
Copy code
if 15 % 5 == 0:
    print("15 is divisible by 5")
else:
    print("15 is not divisible by 5")
4. Wrap Around an Index (e.g., Rotating Through a List)
python
Copy code
items = ["A", "B", "C"]
for i in range(10):
    print(items[i % len(items)])  # Outputs: A, B, C, A, B, C...
5. Get the Last Digit of a Number
python
Copy code
number = 12345
print(number % 10)  # Outputs: 5
6. Find if a Year is a Leap Year
python
Copy code
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap year")
else:
    print("Not a leap year")
7. Partition Numbers
python
Copy code
for i in range(10):
    if i % 3 == 0:
        print(f"{i} is divisible by 3")

## FOR LOOP
The for loop
is used for iterating over a sequence (list, tuple, string) or other iterable objects.
## SYNTAX
for variable in sequence:
    # code to be executed
    ## EXAMPLE
    ts = ["apple", "banana", "cherry"]
    for fruit in fruits:
    print(fruit)
    ## OUTPUT
    apple
    banana
    cherry
    ## EXAMPLE
    for i in range(10):
    print(i)
    ## OUTPUT
    0
    1
    2
    3
    4
    5
    6
    7
    8
    9
    ##
    ## EXAMPLE
    for i in range(1, 10, 2):
    print(i)
    ## OUTPUT
    1
    3
    5
    7
    9
    ## EXAMPLE
    for i
    in range(10, 0, -1):
    print(i)
    ## OUTPUT
    10
    9
    8
    7
    6
    5
    4
    3
    2
    1
    ##
    ## EXAMPLE
    for i in range(1, 10):
    if i % 2 == 0:
    print(i)
    ## OUTPUT
    2
    4
    6
    8
    ##
    ## EXAMPLE
    for i in range(1, 10):
    if i % 2 != 0:
    print(i)
    ## OUTPUT
    1
    3
    5
    7
    9
    ##
    ## EXAMPLE
    for i in range(1, 10):
    if
    i % 2 == 0:
    print(i)
    else:
    print("odd")
    ## OUTPUT
    2
    odd
    4
    odd
    6
    odd
    5
    odd
    8
    odd
    10
    odd
    ##
    ## EXAMPLE
    for i in range(1, 10):
    if i % 2 == 0:
    print(i)
    else:
    print("odd")
    ## OUTPUT
    2
    odd
    4
    odd
    6
    odd
    5
    odd
    8
    odd
    10
    odd
    ##

## lists
A list is a collection which is ordered and changeable. Allows duplicate members.
## SYNTAX
list = ["apple", "banana", "cherry"]
## EXAMPLE
fruits = ["apple", "banana", "cherry"]
print(fruits[0])
## OUTPUT
apple
## EXAMPLE
fruits = ["apple", "banana", "cherry"]
print(fruits[-1])
## OUTPUT
cherry
## EXAMPLE
fruits = ["apple", "banana", "cherry"]
print(fruits[1:3])
## OUTPUT
['banana', 'cherry']

## dictionary
A dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
## SYNTAX
dictionary = { "key": "value" }
## EXAMPLE
person = { "name": "John", "age": 36 }
print(person["name"])
## OUTPUT
John
## EXAMPLE
person = { "name": "John", "age": 36 }
print(person.get("age"))
## OUTPUT
36
## EXAMPLE
person = { "name ": "John", "age": 36 }
print(person.keys())
## OUTPUT
dict_keys(['name', 'age'])
