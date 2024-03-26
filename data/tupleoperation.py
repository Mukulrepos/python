# find the lenght


def leng(tup):
    return len(tup)


grade = (23, 34, 45, 56,1,1, 67, 34, 45, 56, 67, 34, 45, 56, 67, 78, 89, 90, 0, 12)
lenght = leng(grade)
print(lenght)


#  Concatenate two tuples.
def joint(block1, block2):
    return block1 + block2


name = ("muku", "suresh", "saloni", "divya", "kansh")
family = joint(grade, name)
print(family)


#  Access the element in tuple using the index number manunal


def access(tup, index):
    return tup[index]


#  Second index have a saloni name
acess = access(name, 2)
print(acess)


# Count the elements in the tuple


def counter_strike(tup, value):
    return tup.count(value)


#  count the elements how many times is present in the tuple
counter_attack = counter_strike(grade, 67)
print(counter_attack)
#  output 3 times it can present


# exist function or not
def exist(tuples, function):
    return function in tuples


names = exist(name, "muku")
print(names)


#  convert the tuple in string s


def converter(tup):
    return str(tup)


nams = converter(name)
print(nams)


#   cnvert the list


def lists(tup):
    return list(tup)


print(lists(grade))


#  iterate the number using the for lopps


def iterate(tup):
    for iterator in tup:
        print(iterator, end="||")


print(iterate(grade))


# find the max and nin
def checker(tup):
    return max(tup), min(tup)


print(checker(grade))


# joint the albhabet to  make the sentence


def jointer(joins):
    return "".join(joins)


VISION = (" V", "I", "S", "I", "O", "N")
print(jointer(VISION))


#  remover the elements


def remover(tup, value):
    return tuple(x for x in tup if x !=value)

print(remover(name,"muku"))


#  find the common elements

def phone(samrt_phones_in_area, previous_area_phone_locate):
    return tuple(x for x in samrt_phones_in_area if x in previous_area_phone_locate)

signal_sensor= ("Samsung M13", "iphone12", "lenovo ")
signal_sensor_previous = ("iphone12", " lenovo")
common = phone(signal_sensor, signal_sensor_previous)
print(common)


#  sort algos

def sorter(items):
    return tuple(sorted(items))


print(sorter(grade))



# find the all sum of elements

def sums(tup):
    return sum(tup)

print(sums(grade))
