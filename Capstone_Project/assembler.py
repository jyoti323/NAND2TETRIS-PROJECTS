
import os

# Remove comments and blank lines
def clean_file(filename):

    instructions = []

    with open(filename, "r") as file:

        for line in file:

            # Remove comments
            line = line.split("//")[0].strip()

            # Ignore empty lines
            if line:
                instructions.append(line)

    return instructions


# Test the cleaning function
if __name__ == "__main__":

    print("Hack Assembler Started!")

    print("Python environment is ready.")
