# code...
a = 1
b = 2
c = 3
s = a+b+c
r = s/3
print(r)
# code...

'''
def average():
    a = 1
    b = 2
    c = 3
    s = a+b+c
    r = s/3
    print(r)


average()
'''

'''
#input
#parameter
#argument
def average(a,b,c):
    s = a+b+c
    r = s/3
    print(r)

average(10,20,30)
'''


def average(a, b, c):
    s = a+b+c
    r = s/3
    return r


print(average(10, 20, 30))
