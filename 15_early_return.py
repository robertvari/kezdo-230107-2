def get_your_age(age):
    if age < 18:
        # early return if condition true
        return "You can't drink alcohol!"

    return "You can drink alcohol!"

print(get_your_age(17))