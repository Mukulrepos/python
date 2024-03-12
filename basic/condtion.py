# condition it can use the decsion
# what is descioson
# descision is concept of a life to check if u can drive a car to travel one city to anotehr city then you chck the insfastructure is good ot nto the frist city or better or not
# if u have a 100 gb same for this new upadtae the u can update robot dirver or not

storage = int(input("Enter the total available space for the 100 GB update in GB: "))

if storage >= 120:
    print("You can update the driver and install it.")
elif storage >= 100:
    print("You can update the driver, but don't run it yet.")
elif storage >= 50:
    print("You can take more space, but not enough for updating the driver.")
else:
    print("You don't have enough space to update the driver.")

