"""
if you need to traverse the elements of a sequence and
their indices, we should use the built-in function enumerate:
"""

list = ['X', 'Y', 'K', 'L']
for index, value in enumerate(list):
    print(index,value)

>> 0 X
   1 Y
   2 K
   3 L

for index,element in enumerate("FREEDOM"):
    print index,element

>> 0 F
   1 R
   2 E
   3 E
   4 D
   5 O
   6 M

# The zip function, zip(), takes one or more iterable objects as arguments and produces an array of tuple objects.

countries = ['Canada', 'Indonesia', 'Czechia', 'Italy']
capitals = ['Ottava', 'Jakarta', 'Prague', 'Rome']

for country, capital in zip(countries, capitals):
    print(country, "," ,capital)

>> Canada , Ottava
   Indonesia , Jakarta
   Czechia , Prague
   Italy , Rome