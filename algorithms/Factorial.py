def factorial(n, depth=0):
    indent = " " * (depth * 4)  
    if n == 1:
        return 1
    else:
        result = factorial(n - 1, depth + 1)
        result = n * result
        return result