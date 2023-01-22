def calculate_result(a, b):
    def add_numbers(x, y):
        return x+y

    def multiply_numbers(x, y):
        return x*y

    def divide_numbers(x, y):
        return x/y

    add_result = add_numbers(a, b)
    multiply_result = multiply_numbers(add_result, b)
    divide_result = divide_numbers(multiply_result, b)

    return divide_result

result = calculate_result(45, 3)
print(result)