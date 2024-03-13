def average(a=9, b=1):
    print("the ayerage of two numebr is -->", int((a + b) / 2))


#  it can take the default arguments


average()  # it can give only the
# use the keyword argument dont worry about for order maintain

average(b=9, a=91)  # this keyword arrgument


def sum(a, b=1):
    return a + b


#  it can b is default but a i required to push the task make


print(sum(a=9))


#  variable lenght of arguments
def number(*number):
    sum = 0
    print(type(number))
    for i in number:
        sum = sum + i
    print(f"the average of {len(number)} number is -->", int(sum / len(number)))


number(
    4, 4, 4, 5, 3, 3, 3, 3, 3, 3, 3, 3, 5, 3, 3, 3, 3, 3, 3
)  # it depends on the lenght of arrgument it can passed in for in tuple and finthe averaeg of totoal number arrgument passed



# it use the dictonry type of data is store 
def greet(**kwargs):
    print(type(kwargs))
    print("Hello,", kwargs['sname'], kwargs['last_name'])

greet(sname="Mukul", last_name="Vats")
