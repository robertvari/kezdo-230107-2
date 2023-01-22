def check_result(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result < 10:
            print(f"Result is too low: {result}")
            
        return result
    return wrapper


@check_result
def add_numbers(a, b):
    return a+b


result = add_numbers(3, 3)
print(result)