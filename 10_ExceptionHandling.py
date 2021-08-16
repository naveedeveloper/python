
# Example 1
num1 = input("Enter a number : ")
num2 = input("Enter a number : ")

try:
    ans = int(num1) / int(num2)
    print("Ans : ", ans)
except Exception as e:
    print("Exception occured : ", e)



# Example 2

num1 = input("Enter a number : ")
num2 = input("Enter a number : ")

try:
    ans = num1 / int(num2)
    print("Ans : ", ans)
except Exception as e:
    print("Exception occured : ", e)