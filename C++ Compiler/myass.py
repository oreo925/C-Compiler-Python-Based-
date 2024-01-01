import subprocess
def convert_to_assembly(cpp_code):
    # Create a temporary C++ file
    cpp_filename = "temp.cpp"
    with open(cpp_filename, "w") as file:
        file.write(cpp_code)
    # Use gcc to compile the C++ code and generate assembly code
    asm_filename = "temp.s"
    command = ["gcc", "-S", cpp_filename, "-o", asm_filename]
    subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # Read the assembly code from the file
    with open(asm_filename, "r") as file:
        assembly_code = file.read()
    # Remove temporary files
    subprocess.run(["rm", cpp_filename, asm_filename])
    return assembly_code
