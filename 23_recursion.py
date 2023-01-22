def call_myself(n):
    print(f"The value of n is: {n}")

    if n >= 10:
        return

    call_myself(n+1)


call_myself(0)