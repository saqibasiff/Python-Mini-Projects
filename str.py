# Ask the user for the number of rows
rows = int(input("Enter the number of rows: "))

# Print the pyramid star pattern
for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * (2 * i - 1))
