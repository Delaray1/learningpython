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
