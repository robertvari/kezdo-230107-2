def say_hello(email, name, address):
    print(f"Hello {name}")
    print(f"Your email: {email}")
    print(f"Your address:  {address}")

# keyword arguments
say_hello(address="Budapest", name="Csaba", email="csaba@gmail.com")