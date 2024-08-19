def factorial(n, depth=0):
    indent = " " * (depth * 4)  # Create indentation for better readability
    print(f"{indent}factorial({n}) called")  # Print the value of n at the start of each call

    if n == 1:
        print(f"{indent}Returning 1 because n is {n}")
        return 1
    else:
        # Recursive call
        result = factorial(n - 1, depth + 1)
        result = n * result
        print(f"{indent}Returning {result} because {n} * factorial({n-1}) = {result}")
        return result

# Test the function
print(f"Final Result: {factorial(5)}")
