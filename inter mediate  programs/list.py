# grocerry store list
fruit = list(("Apple=", "Mango", "Banana", "Kiwi", "Pineapple"))
new_fruit = [" Avocado", "Lemon", "Apricot", "Blueberry", " Papaya"]
vegetable = ["Potatao", "Cabage", "Ladyfinger", "Sweet potato", "onion", "Ginger"]
cleaning_items = [
    "polish",
    "Dish towel",
    "Brush",
    "soap",
    "bathroom cleaner",
    "Trash can",
    "Mop",
    "Hose",
]
kitchen_item = [
    "wash basin",
    "Spice box",
    "Jar",
    "Tray",
    "Ice Tray",
    "Spoon ",
    "Cutting tray",
    "Match box",
    "Fry pan",
]
store = [fruit, vegetable, cleaning_items, kitchen_item]

# call individualy list  using index value
print(store[0])
print(store[1])
print(store[2])
print(store[3])


# call by using list -> index number
print(store[0][2])
print(store[1][2])
print(store[2][2])
print(store[3][2])


#  lenght of all list's
print("This lenght of Fruits Items->", {len(store[0])})

print("This lenght of vegetable Items->", {len(store[1])})

print("This lenght of Cleaning Items->", {len(store[2])})

print("This lenght of Kitchen Items->", {len(store[3])})


# using of range function (start here and end here - 1)
print(kitchen_item[1:7])
#  in other function you can using [:end any where but still-1]
print(kitchen_item[:7])


#  check by customer is it avaiable  or not !


if "Kiwi" in fruit:
    print("-------yes is aviable sir you can buy or not")
else:
    print("Sorry sir isn't avaiable in store")

# store owner can change the item or update a store then is using the index

# list can allow the to change the item

fruit[2] = "Dragon fruit"
print(fruit)


#  uisng the index start here : end here the value can change

fruit[1 + 1 : 3] = ["Blueberry", "Cherry"]
print(fruit)


#  Index value insert uisng insert function()

fruit.insert(3, "Plum")
print(fruit)


#  append using to add the items in list but at the end the side
print("Previous list", len(fruit))
fruit.append("Orange")
print("after append ", len(fruit))


# List comprehension
seperate_fruit=[]
for i in fruit:
    if "a" in i:
        seperate_fruit.append(i)
        
print(seperate_fruit)


#  you can convert any list in single for some funn (:->)>

your_love_thing= ["Salon" for x in fruit]
print(your_love_thing)


#  thank you 
