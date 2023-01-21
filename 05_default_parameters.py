def say_hello(username, password, email=None, address=None):
    print(f"Hello {username}")
    print(f"Password: {password}")
    print(f"Your email: {email}")
    print(f"Your address:  {address}")

say_hello("robert", "testpas123")
say_hello("robert", "testpas123", "robert@gmail")
say_hello("robert", "testpas123", "robert@gmail", "Budapest")