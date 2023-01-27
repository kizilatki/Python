"""
It doesn't make sense to repeat the same work over and over.

We can automate a repeated actions and call it when we need.

Function provides this exactly.

"""

def read(x):

"""
a function is define with "def" as above. For the example, function name is "read"
and the expression in parantheses is called the argument. At the end,
you can "call" the function by the name.

"""
def say_hi():
    print("Hello World")

say_hi():               # if we call
>> Hello World

def book_list():
    print("We\nA Brief History of Time\nThe Invisible Man")

book_list()
>> We
   A Brief History of Time
   The Invisible Man

# or

def book_list():
    print ("We")
    print ("A Brief Hisroty of Time")
    print ("The Invisible Man")

>> # output is same

def favourite_list():
    book_list()

favourite_list()
>> We
   A Brief History of Time
   The Invisible Man
 
