# Specify the path to your file
file_path = "your_log_file.txt"

# Read the data from the file
with open(file_path, 'r') as file:
    data = file.readlines()

# Remove leading and trailing whitespaces from each line
data = [line.strip() for line in data]

# Create a Python list
stocks = data

# Print the list of stocks
print(stocks)
