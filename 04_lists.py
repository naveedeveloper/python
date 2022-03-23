items = ["Bread", "Butter", "Fruits"]
Numbers = [1, 2, 3, 4]

print("Numbers List : ", Numbers)
print("Full List : ", items)
print("item at index 1 : ", items[1])
print("items from 0 to 1 index in items list: ", items[0:2])

'''
-> List related function's in python
-> append
-> insert
-> delete
-> item in listName

'''

items.append("Veggies")
print("Appeneded List : ", items)

items.insert(2, "Apples")
print("list after inserting some data : ",items)

print("Bread in the List : ", 'Bread' in items)
print("Burger in the List : ", 'Burger' in items)
