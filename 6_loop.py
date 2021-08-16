num = 5

for i in range(1, 11):
    print(num, " * ",i, " = ",num * i)


items = ["Apple", "Orange", "Mango", "Banana"]

for item in items:
    print(item)

numbers = [21, 43, 56, 3, 54]

for i in numbers:
    if i == 3:
        print("3 is found!!")
        break
    else:
        print("3 not found")
