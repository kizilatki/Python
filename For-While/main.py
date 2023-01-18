"""
We can guess the meaning of "for" and "while" from the English Grammar lessons.
Actually, these are same in the Python programming language too.

Easy level example:

list = [["a","b"], ["p","21"], ["17","27"], ["U","Y"], ["13","8"]]
for x,y in list:
   print(y)

>>  b
    21
    27
    Y
    8


x = 0
while x<6:
   print ("{} is lower than 6" .format(x))
   x += 1

>  0 is lower than 6
1 is lower than 6
2 is lower than 6
3 is lower than 6
4 is lower than 6
5 is lower than 6

Medium level example:

for number in range(1,6):
    if number%2==0:
        continue
    print(number)

 > 1
   3
   5
