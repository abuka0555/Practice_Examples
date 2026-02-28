def multiply(x, y):
    """A regular function to multiply two numbers."""
    result = x * y
    return result

# Calling the regular function
output = multiply(5, 3)
print(f"Regular function output: {output}")


# An anonymous function (lambda) to multiply two numbers
# lambda parameters: expression
multiply_lambda = lambda x, y: x * y

# Calling the anonymous function
output_lambda = multiply_lambda(5, 3)
print(f"Anonymous function output: {output_lambda}")
