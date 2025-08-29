# File Read & Write Challenge with Error Handling

def modify_content(line):
    """
    Example modification function.
    Here we simply convert each line to uppercase.
    You can customize this as needed.
    """
    return line.upper()


# Ask the user for a filename
filename = input("Enter the filename to read: ")

try:
    # Try to open and read the file
    with open(filename, "r") as infile:
        lines = infile.readlines()

    # Modify the content
    modified_lines = [modify_content(line) for line in lines]

    # Write modified content to a new file
    new_filename = "modified_" + filename
    with open(new_filename, "w") as outfile:
        outfile.writelines(modified_lines)

    print(f"Modified content written to '{new_filename}' successfully!")

except FileNotFoundError:
    print(f"Error: The file '{filename}' does not exist.")
except IOError:
    print(f"Error: The file '{filename}' could not be read or written.")