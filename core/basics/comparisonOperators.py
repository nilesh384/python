# temp = 31

# if(temp == 30):
#     print ("it is 30")

# if(temp != 30):
#     print ("it is not 30")

name = input("what is your name? ")
if(len(name) < 3):
    print("name must be at least 3 characters")
elif(len(name) > 50):
    print("name must be less than 50 characters")
else:
    print("name looks good")