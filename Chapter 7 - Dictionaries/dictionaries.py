# there are 2 ways of making a dictionary

band = {
    "vocals": "Plant",
    "guitar": "Page"
}

band2 = dict(vocals="Plant", guitar="Page")

print(band)
print(band2)

# accessing items in a dictionary
print(band["vocals"])
print(band.get("guitar"))

# list all keys
print(band.keys())

# list all values
print(band.values())

# list of key/value pairs as typles
print(band.items())

# verify if a key exists
print("guitar" in band)
print("triangle" in band)

# change values in a dictionary
band["vocals"] = "Coverdale"
band.update({"bass": "JPJ"})

print(band)

# remove items
print(band.pop("bass"))
print(band)

band["drums"] = "Bonham"
print(band)

print(band.popitem())
print(band)

# delete and clear items
band["drums"] = "Bonham"
del band["drums"]
print(band)

band2.clear()
print(band2)

del band2


# copy dictionary
band2 = band.copy()

# or you can do this
band3 = dict(band)

# nested dictionaries
member1 = {
    "name": "Plant",
    "instrument": "vocals"
}
member2 = {
    "name": "Page",
    "instrument": "guitar"
}
band = {
    "member1": member1,
    "member2": member2
}

print(band)
print(band["member2"]["name"])

# Sets
nums = {1,2,3,4}
nums2 = set((1,2,3,4))

# no duplicates allowed in a set - it will remove duplicates
nums = {1,2,2,3}
print(nums)

# it will also treat True as 1 and False as 0

# you can check if a value is in a set
print(2 in nums)

# but you cannot refer to an elemt in the set with an index position or a key

# add a new element to a set
nums.add(8)

# add elements from one set to another
morenums = {5,6,7,8}

nums.update(morenums)
print(nums)

# merging two sets and creating a new one
nums4 = {1,2,3}
nums5 = {4,5,6}

new_set = nums4.union(nums5)
print(new_set)