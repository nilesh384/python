try:
    age = int(input("Enter age:  "))
    print ("age is : ",age)

    risk = 2000/age
    print("risk is: ",risk)


except ValueError:
    print("correct your code")

except ZeroDivisionError:
    print("cant give 0 as age ")