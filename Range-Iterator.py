"""
the range function ,range(), creates the number series between first number and (last number-1).

"""
for x in range(1,6):
    print(x**2)

>> 1
   4
   9
   16
   25

for a in range(10,20,2)              # from 10 to 20 in increase of 2 each.
    print(a)

>> 10
   12
   14
   16
   18

"""
Iterator, arrays of ordered elements that can be applied to their elements
sequentially and one at a time are called iterable structures.

list = ['A', 'B', 'C', 'D' ] -----> [iterator] -- [A]
                                               -- [B]
                                               -- [C]
                                               -- [D]
                                               
and main methods: 

iter()
next()

In addition, to use "*" is a more pratical way for iterator in Python like SQL.
"""
city = "Edinburgh"
t = iter(city)
print(*t)

>> E d i n b u r g h


shopping = ["Books", "Puzzle", "Coffee"]

iter_shop = iter(shopping)
print(next(iter_shop))

while True:
    try:
        element = next(iter_shop)
        print(element)

    except: StopIteration             # if element ended, iterator stopped and, break.
    break

>> Books
   Puzzle
   Coffee




