
import os
import re

INPUT_FOLDER = "input"
OUTPUT_FOLDER = "output"

# Create predefined symbol table
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

    # Add registers R0 to R15
    for i in range(16):
        symbols["R" + str(i)] = i

    return symbols


def is_valid_symbol(name):
    return re.fullmatch(r"[A-Za-z_.$:][A-Za-z0-9_.$:]*", name) is not None
    symbols = {
        "SP": 0,
        "LCL": 1,
        "ARG": 2,
        "THIS": 3,
        "THAT": 4,
        "SCREEN": 16384,
        "KBD": 24576
    }

    for i in range(16):
        symbols["R" + str(i)] = i

    return symbols


# Remove comments and blank lines
def clean_file(filename):
    instructions = []

    with open(filename, "r") as file:
        for line_number, line in enumerate(file, start=1):
            line = line.split("//")[0].strip()

            if line:
                instructions.append((line_number, line))

    return instructions


# First pass: identify labels and report errors
def first_pass(instructions, symbols):

    rom_address = 0

    for line_number, instruction in instructions:

        if instruction.startswith("(") or instruction.endswith(")"):

            if not (instruction.startswith("(") and instruction.endswith(")")):
                raise ValueError(
                    f"Line {line_number}: Invalid label format: {instruction}"
                )

            label = instruction[1:-1]

            if not is_valid_symbol(label):
                raise ValueError(
                    f"Line {line_number}: Invalid label name: {label}"
                )

            if label in symbols:
                raise ValueError(
                    f"Line {line_number}: Duplicate or reserved label: {label}"
                )

            symbols[label] = rom_address

        else:
            rom_address += 1

    return symbols

# Binary codes for computations
COMP = {
    "0": "0101010",
    "1": "0111111",
    "-1": "0111010",
    "D": "0001100",
    "A": "0110000",
    "M": "1110000",
    "!D": "0001101",
    "!A": "0110001",
    "!M": "1110001",
    "-D": "0001111",
    "-A": "0110011",
    "-M": "1110011",
    "D+1": "0011111",
    "A+1": "0110111",
    "M+1": "1110111",
    "D-1": "0001110",
    "A-1": "0110010",
    "M-1": "1110010",
    "D+A": "0000010",
    "D+M": "1000010",
    "D-A": "0010011",
    "D-M": "1010011",
    "A-D": "0000111",
    "M-D": "1000111",
    "D&A": "0000000",
    "D&M": "1000000",
    "D|A": "0010101",
    "D|M": "1010101"
}


# Destination codes
DEST = {
    "": "000",
    "M": "001",
    "D": "010",
    "MD": "011",
    "A": "100",
    "AM": "101",
    "AD": "110",
    "AMD": "111"
}


# Jump codes
JUMP = {
    "": "000",
    "JGT": "001",
    "JEQ": "010",
    "JGE": "011",
    "JLT": "100",
    "JNE": "101",
    "JLE": "110",
    "JMP": "111"
}

# Convert A-instruction and validate its symbol
def assemble_a_instruction(instruction, symbols, next_variable):

    value = instruction[1:]

    if not value:
        raise ValueError("Missing address after @")

    if value.isdigit():
        address = int(value)

    else:
        if not is_valid_symbol(value):
            raise ValueError("Invalid symbol: " + value)

        if value not in symbols:
            symbols[value] = next_variable[0]
            next_variable[0] += 1

        address = symbols[value]

    if address < 0 or address > 32767:
        raise ValueError("Address must be between 0 and 32767")

    return format(address, "016b")


# Convert C-instruction
def assemble_c_instruction(instruction):
    dest = ""
    jump = ""

    if "=" in instruction:
        dest, instruction = instruction.split("=", 1)

    if ";" in instruction:
        instruction, jump = instruction.split(";", 1)

    comp = instruction

    if comp not in COMP:
        raise ValueError("Invalid computation: " + comp)

    if any(char not in "ADM" for char in dest) or len(set(dest)) != len(dest):
        raise ValueError("Invalid destination: " + dest)

    dest_bits = format(
        (4 if "A" in dest else 0) +
        (2 if "D" in dest else 0) +
        (1 if "M" in dest else 0),
         "03b"
    )

    if jump not in JUMP:
        raise ValueError("Invalid jump: " + jump)

    return "111" + COMP[comp] + dest_bits + JUMP[jump]


# Second pass: convert instructions into binary
def second_pass(instructions, symbols):
    machine_code = []
    next_variable = [16]

    for line_number, instruction in instructions:

        if instruction.startswith("(") and instruction.endswith(")"):
            continue

        try:
            if instruction.startswith("@"):
                binary = assemble_a_instruction(
                    instruction, symbols, next_variable
                )
            else:
                binary = assemble_c_instruction(instruction)

            machine_code.append(binary)

        except (ValueError, IndexError) as error:
            raise ValueError(f"Line {line_number}: {error}")

    return machine_code


# Assemble one ASM file
def assemble_file(filename):

    input_path = os.path.join(INPUT_FOLDER, filename)
    output_name = filename.replace(".asm", ".hack")
    output_path = os.path.join(OUTPUT_FOLDER, output_name)

    instructions = clean_file(input_path)

    # Use a separate symbol table for each program
    symbols = create_symbol_table()

    # Pass 1
    first_pass(instructions, symbols)

    # Pass 2
    machine_code = second_pass(instructions, symbols)

    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    with open(output_path, "w") as file:
        for binary in machine_code:
            file.write(binary + "\n")

    print(filename, "->", output_name, "completed")
    print("Machine instructions:", len(machine_code))


# Main programzos
if __name__ == "__main__":

    print("Hack Assembler Started!")

    files = ["Add.asm", "Max.asm", "Rect.asm", "Pong.asm"]

    for filename in files:
        try:
            assemble_file(filename)
        except Exception as error:
            print("Error in", filename, ":", error)

    print("\nAssembly process finished!")
