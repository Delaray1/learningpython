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
# EXAMPLE
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("Even")
else:
    print("Odd")
2. Cycle Through Values
# EXAMPLE
for i in range(10):
    print(i % 3) 
# Outputs: 0, 1, 2, 0, 1, 2...
3. Check Divisibility
# EXAMPLE
if 15 % 5 == 0:
    print("15 is divisible by 5")
else:
    print("15 is not divisible by 5")
4. Wrap Around an Index (e.g., Rotating Through a List)
# EXAMPLE
items = ["A", "B", "C"]
for i in range(10):
    print(items[i % len(items)])
# Outputs: A, B, C, A, B, C...
5. Get the Last Digit of a Number
# EXAMPLE
number = 12345
print(number % 10)
# Outputs: 5
6. Find if a Year is a Leap Year
# EXAMPLE
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap year")
else:
    print("Not a leap year")
7. Partition Numbers
# EXAMPLE
for i in range(10):
    if i % 3 == 0:
        print(f"{i} is divisible by 3")

## FOR LOOP
The for loop
is used for iterating over a sequence (list, tuple, string) or other iterable objects.
## Examples
1. Looping Through a List
# EXAMPLE
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
2. Using range()
Example: Loop from 0 to 9
# EXAMPLE
for i in range(10):
    print(i)
## Example: Loop with a Step
# EXAMPLE
for i in range(0, 20, 5):
    print(i)
## Example: Loop in Reverse
# EXAMPLE
for i in range(10, 0, -1):
    print(i)
3. Looping Through a String
# EXAMPLE
word = "Python"
for letter in word:
    print(letter)
4. Looping Through a Dictionary
# EXAMPLE
grades = {"Alice": "A", "Bob": "B", "Charlie": "C"}
for student, grade in grades.items():
    print(f"{student} scored {grade}")
5. Nested for Loops
# EXAMPLE
for i in range(3):
    for j in range(2):
        print(f"i = {i}, j = {j}")
6. for Loop with else
The else block in a for loop runs after the loop completes, unless the loop is terminated by a break.
# EXAMPLE
for i in range(5):
    print(i)
else:
    print("Loop completed!")
7. Breaking Out of a Loop
# EXAMPLE
for i in range(10):
    if i == 5:
        break
    print(i)
8. Skipping an Iteration with continue
# EXAMPLE
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
9. Using pass in a Loop
The pass statement is a placeholder that does nothing.
# EXAMPLE
for i in range(5):
    if i == 3:
        pass
    else:
        print(i)
10. Looping Through a List with enumerate()
# EXAMPLE
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")
11. Looping Through Multiple Sequences with zip()
# EXAMPLE
names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 78]
for name, score in zip(names, scores):
    print(f"{name} scored {score}")

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
