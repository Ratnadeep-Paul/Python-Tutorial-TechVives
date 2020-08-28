dc = {"Car":"BMW", "Bike":"Kawasaki"}
# This is a simple Dictionary.

# Default Dictionary = {"Key":"Value"}

print(dc)
# Printing a Dictionary is also same.

ls_in_dict = {"iOS":"iPhone", "Android":["Samsung", "OnePlus", "Xiaomi", "Vivo", "Oppo", "Realme"]}
dict_in_dict = {"iOS":"iPhone", "Android":{"Samsung":"Note 20", "OnePlus":"OnePlus 8", "Vivo":"X50 Pro"}}

# We can print this--
print(ls_in_dict)
print(ls_in_dict["Android"])
print(dict_in_dict)
print(dict_in_dict["Android"])
print(dict_in_dict["Android"]["OnePlus"])


# Basic Methods==
dc = {"Car":"BMW", "Bike":"Kawasaki"}
print(dc["Bike"])

# Change Key Value Of A Python Dictionary
dc = {"Car":"BMW", "Bike":"Kawasaki"}

dc["Bike"] = "Suzuki"

# Now if we print the Dictionary(dc). Then we will get the new value.
print(dc)
print(dc["Bike"])

# Add Key Value Of A Python Dictionary
dc = {"Car":"BMW", "Bike":"Kawasaki"}

dc["Ship"] = "Titanic"

# Now if we print the Dictionary(dc). Then we will get the new key and value.
print(dc)
print(dc["Ship"])

# Copy() Function
dc = {"Car":"BMW", "Bike":"Kawasaki"}
dc1 = dc.copy()
print(dc1)

# Get() Function
dc = {"Car":"BMW", "Bike":"Kawasaki"}
print(dc.get("Car"))

# keys() and values() function
dc = {"Car":"BMW", "Bike":"Kawasaki"}
print(dc.keys())
print(dc.values())

# update() Functions
dc = {"Car":"BMW", "Bike":"Kawasaki"}
dc.update({"Bicycle":"Hero"})
# The new key and value will be add added.
print(dc)
print(dc.get("Bicycle"))
