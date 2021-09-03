# a = 15 #int
# c = 3.7 #float
# comp = complex(5,7)
# print(type(comp))
#
# print(2 / 3)
# print(int(2/2))
# c = int(c)
# print(c)
# a = float(a)
# print(a)


# print(bin(a))
# print(oct(a))
# print(hex(a))
# STRINGs
a = 'Привет "Tom"'
b = "Hello 'Tom'"
print(a[1])
print(a[0:10:2])
print(a[::-1])
print(b.lower())
print(b.upper())
print(b.isdigit())
print(b.count('o'))
print(b.index("'"))
a = input("enter a number")
if a.isdigit():
    a = int(a)
else:
    print('wrong type of data')


