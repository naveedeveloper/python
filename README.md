# Python

Python is a high-level, interpreted programming language that is widely used for web development, data analysis, artificial intelligence, and scientific computing. Its simple syntax and dynamic nature make it a great choice for beginners and experienced programmers alike.

In this repo I covered all the basics of Python language.

## Variables
- In Python, variables are used to store and manipulate data.
- Variables are declared by giving them a name and assigning a value to them.

### Example:

x = 5

y = "Hello, World!"

## Data Types
Python has several built-in data types, including:

- <b>int:</b> used for whole numbers
- <b>float:</b> used for decimal numbers
- <b>str:</b> used for strings of characters
- <b>bool:</b> used for True/False values
- <b>list:</b> used for lists of items
- <b>dict:</b> used for key-value pairs

## Operators
Python has several operators that can be used to perform mathematical and logical operations on variables.

- <b>+:</b> used for addition
- <b>-:</b> used for subtraction
- <b>*:</b> used for multiplication
- <b>/:</b> used for division
- <b>%:</b> used for modulus (remainder)
- <b>==:</b> used for equality comparison
- <b>!=:</b> used for inequality comparison
- <b><:</b> used for less than comparison
- <b>>:</b> used for greater than comparison

## Control Flow
Python provides several control flow statements that can be used to control the flow of execution in a program.

- <b>if:</b> used for conditional execution
- <b>for:</b> used for looping through a sequence of items
- <b>while:</b> used for looping while a condition is true


## Functions
Functions are a way to organize and reuse code. In Python, functions are defined using the def keyword, followed by the function name and a set of parentheses that contain any parameters the function takes.

```
def greet(name):
    print("Hello, " + name + "!")

greet("John") # Outputs "Hello, John!"
```
    
## Classes
Classes are a way to create objects that have their own methods and properties. In Python, classes are defined using the class keyword, followed by the class name and a set of parentheses that contain the parent class, if any.

```
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print("Woof!")

dog = Dog("Fido", "Golden Retriever")
print(dog.name) # Outputs "Fido"
dog.bark() # Outputs "Woof!"
```
This should give a basic understanding on python concepts. Happy Coding!
