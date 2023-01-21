NAME = "pythonsuli.hu"

def change_name(name):
    # pull NAME from global space
    global NAME

    # override NAME with new name
    NAME = name

change_name("Csaba")
print(NAME)