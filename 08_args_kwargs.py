def print_all_params(*args, **kwargs):
    print(args)
    print(kwargs)


print_all_params(
    "csaba",
    10,
    "Debrecen",
    my_color="blue",
    phone="12345",
    email="robert@gmail.com"
)