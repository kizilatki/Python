"""
List comprehension helps us to create a new list from another or old list.
By the list comprehension, we can generate a new list in just a line.

First of all, list are able to create by using the "for" too. Yes, can do.

For example:

"""
list1 = [2, 3, 5, 7, 10, 15]
list2 = []

for i in list1:
    list2.append(i**2)
print(list2)

>> [4, 9, 25, 49, 100, 225]


cube_list = []
for i in range(2,7):
    cube_list.append(i**3)

print(cube_list)

>> [8, 27, 64, 125, 216]



# with List Comprehension:
1)

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday' ]

short_days = [day[0:3] for day in days]
print(short_days)

>> ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

2)

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday' ]
brief_days = [day[0:3] for day in days if day[0] == "S"]

print(brief_days)

>> ['Sat', 'Sun']

# List Comprehension witf if + else

loop = [i**23 if i % 2 == 1 else i**3 for i in range(2,9)]
print(loop)

>> [8, 9, 64, 25, 216, 49, 512]

