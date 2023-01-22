name_list = ["Vári Róbert", "Kiss Elemér", "Nagy Adrienn", "Tóth Barna", "Kiss Elemér Aladár"]

def split_name(name):
    return name.split()[-1]

# using key with a function
print(sorted(name_list, key= split_name))

# using key with a lambda
print(sorted(name_list, key= lambda name: name.split()[-1]))