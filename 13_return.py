def add_numbers(a: int, b: int):
    return a + b

def multiply_numbers(a: int, b: int):
    "Multipy two numbers"
    return a * b

def divide_numbers(a: int, b:int):
    "Divide two numbers"
    return a / b

add_result = add_numbers(10, 3)
multipy_result = multiply_numbers(add_result, 10)
final_result = divide_numbers(multipy_result, 450)
print(final_result)