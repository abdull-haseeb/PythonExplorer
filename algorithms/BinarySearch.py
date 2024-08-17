def binary_search(my_list, item):
    low = 0  # Start of the list
    high = len(my_list) - 1  # End of the list
    
    while low <= high:
        mid = (low + high) // 2 # Calculate the middle index
        print("low =", low, ", high =", high, ", mid =", mid)  # Debug print
        
        guess = my_list[mid]  # Get the middle element
        print("guess =", guess)  # Debug print
        
        # If the guess is correct, return the index
        if guess == item:
            return mid
        # If the guess is too high, reduce the search space to the left half
        if guess > item:
            high = mid - 1
        # If the guess is too low, reduce the search space to the right half
        else:
            low = mid + 1
    
    # If the item is not found, return None
    return None

# Example usage
my_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
print("RESULT:", binary_search(my_list, 4))  # Searching for the number 4
