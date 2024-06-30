pattern_size = int(input("Enter the size of the pattern: "))

# Validate input to ensure it is a positive integer
if pattern_size <= 0:
    print("Please enter a positive integer.")
else:
    row = 0

    # Use a while loop to iterate through each row
    while row < pattern_size:
        for column in range(pattern_size):
            print("*", end="")
            row += 1
