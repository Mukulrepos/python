
# this is operator to use to basic to complex tesk in the python
# 1. arthemetic operator
# 2. conditional and relation operator
# 3. logical operator
# 4. bitwise
# 5.Assignment operator 
# 6.identity
# 7.membership operator 

# Arthemetic operator 
# +, - , / for float division, * , %, // for integer value  , ** power
 

# print(34//6)
# print(34-6)
# print(34/6)
# print(34%6)
# print(34*6)
# print(34**6)

# operator precedence

print(5+5*5)

# ()
#  **
#  *,/,//,%
#  +,-
#==========================================================================================
#Assignment and comparision 
# a=5 the value 5 asign in a varaiable
# this is comparsion is >,<,>=,<=, ==, != 



#==============================================================
#logical operator 
#and ,or, not


a , b = 7, 8 
if a==7 and b !=8:
    print("true ")
else:
    print("false")
    
    # work on and operator of logical type
    #if any one is not true is not exicuted 
    # a  b ans  
    # |1 |1  |true
    # |1 |0  |false
    # |0 |0  |false
    # |0 |1  |false
    
    
    
a , b = 7, 8 
if a==7 or b !=8:
    print("true ")
else:
    print("false")
    
    # work on or gate in logical operator 
    #if any one true it can exicuted
    # a b  ans
    # |1 |1  |true
    # |1 |0  |true
    # |0 |0  |false
    # |0 |1  |true
    
    
    