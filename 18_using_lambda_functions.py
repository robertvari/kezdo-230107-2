name_list = ["Vári Róbert", "Kiss Elemér", "Nagy Adrienn", "Tóth Barna", "Kiss Elemér Aladár"]

def split_name(name):
    return name.split()[-1]

print(sorted(name_list, key=split_name))