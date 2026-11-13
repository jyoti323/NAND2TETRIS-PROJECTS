
import os

# Folder containing assembly files
INPUT_FOLDER = "input"


# Step 1: Remove comments and blank lines
def clean_file(filename):

    instructions = []

    with open(filename, "r") as file:

        for line_number, line in enumerate(file, start=1):

            # Remove comments
            line = line.split("//")[0].strip()

            # Ignore blank lines
            if line:
                instructions.append((line_number, line))

    return instructions


# Step 2: Create predefined symbols
def create_symbol_table():

    symbols = {
        "SP": 0,
        "LCL": 1,
        "ARG": 2,
        "THIS": 3,
        "THAT": 4,
        "SCREEN": 16384,
        "KBD": 24576
    }

    # Add R0 to R15
    for i in range(16):
        symbols["R" + str(i)] = i

    return symbols


# Step 3: First pass - identify labels
def first_pass(instructions, symbols):

    rom_address = 0

    for line_number, instruction in instructions:

        if instruction.startswith("(") and instruction.endswith(")"):

            # Extract label name
            label = instruction[1:-1]

            # Save label with its ROM address
            if label not in symbols:
                symbols[label] = rom_address

        else:
            rom_address += 1

    return symbols


# Main program
if __name__ == "__main__":

    print("Hack Assembler - Pass 1 Started")

    symbols = create_symbol_table()

    files = ["Add.asm", "Max.asm", "Rect.asm", "Pong.asm"]

    for filename in files:

        filepath = os.path.join(INPUT_FOLDER, filename)

        instructions = clean_file(filepath)

        symbols = first_pass(instructions, symbols)

        print("\nFile:", filename)
        print("Instructions:", len(instructions))

    print("\nFirst Pass Completed!")
