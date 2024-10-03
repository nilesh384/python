customer = {
    "name": "Nilesh",
    "age": 27,
    "is_verified": True}

print(customer["age"])    #throws keyError if key is absent so we use get function

print(customer.get("Name"))    #returns None if key is absent

print(customer.get("Name", "Not Found"))      #returns default value if key is absent

customer["name"] = "Manish"
customer["college"] = "IIT Patna"

print(customer)