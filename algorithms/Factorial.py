def factorial(n, depth=0):
    indent = " " * (depth * 4)  # Create indentation for better readability

    if n == 1:
        return 1
    else:
        # Recursive call
        result = factorial(n - 1, depth + 1)
        result = n * result
        return result

# Test the function
