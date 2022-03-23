def Sum(a, b):
    total = a + b
    return total


ans = Sum(2, 5)
print("Answer : ", ans)


list1 = [123, 546, 2324, 531, 1]
list2 = [12, 435, 645, 645, 43]

def Total(arg):
    total  = 0
    for i in arg:
        total = total + i
    return total

print("List1 Total : ", Total(list1))
print("List2 Total : ", Total(list2))

