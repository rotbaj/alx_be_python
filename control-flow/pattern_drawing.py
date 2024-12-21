# Prompt the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Validate the input to ensure it's a positive integer
if size <= 0:
    print("Please enter a positive integer.")
else:
    # Use a while loop for rows
    row = 0
    while row < size:
        # Use a for loop to draw the asterisks in each row
        for col in range(size):
            print("*", end="")
        print()  # Print a newline after each row
        row += 1
