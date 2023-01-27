"""
I can say that,
functions can make a program easier to read and to clear.
In addition, it can make useful with debugging on code because,
we can easily solved the problems on the codes with dividing a function.

Then, having return programming in the function is a significant act.

"""
def square(a):
    return a**2

square(7)
>> 49

def oper(x,y):
    return x**y

oper(4,3)
>> 64

def math(a,b,c,):
    m1 = a**b
    m2 = a**c
    result = (m1, m2)
    return result
math(3,4,5)
>> (81,243)

def multi(*args):           # when have use flexible arguments
    result = 1
    for number in args:
        result = result * number

    print(result) 

multi(2,3,4,5)
>> 120



x = [3, 5, 6, 7, 8, 9, 12, 15, 20]

def average(list):
    piece = 0
    total = 0

    for t in list:
        piece += 1
        total += t

    result = total/piece
    return result

average(x)
>> 9.4444


def query():
    z = int(input("Please, enter a number: "))

    if z % 2 == 0:
        print("{} is an even number.".format(z))
    else:
        print("{} is an odd number. ".format(z))

query()
>> Please, enter a number: 18
   18 is an even number.
# or
>> Please, enter a number : 7
   7 is an odd number. 
