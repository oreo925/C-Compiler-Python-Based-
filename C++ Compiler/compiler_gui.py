import tkinter as tk
from tkinter import messagebox
from mylexer import tokenize
from myparser import parse, generate_parse_tree
import myass
import myco
code = """
#include <iostream>
using namespace std;
int main() {
    int x = 42;
    if (x > 0) {
        cout << "x is positive" << endl;
    } else {
        cout << "x is non-positive" << endl;
    }
    return 0;
}
"""
def parse_code():
    # Tokenize the code
    tokens, keywords, identifier, integer_literal, floating_literal, string_literal = tokenize(code)
    # Parse the tokens
    stack, remaining_tokens = parse(tokens, keywords, identifier, integer_literal, floating_literal, string_literal)

    if remaining_tokens:
        error_line = len(tokens) - len(remaining_tokens) + 1
        messagebox.showerror("Parsing Error", f"Parsing error at line {error_line}")
    else:
        parse_tree = generate_parse_tree(stack)
        messagebox.showinfo("Parsing Result", f"No parsing errors\n\nParse Tree:\n{parse_tree}")
def tokenize_code():
    # Tokenize the code
    tokens, keywords, identifier, integer_literal, floating_literal, string_literal = tokenize(code)
    messagebox.showinfo("Tokenization Result", f"Tokens:\n{tokens}")
def optimize_code():
    # Optimize the code
    optimized_code = myco.optimize_code(code, [])
    messagebox.showinfo("Code Optimization Result", f"Optimized Code:\n{optimized_code}")
def generate_assembly_code():
    # Convert to assembly code
    assembly_code = myass.convert_to_assembly(code)
    messagebox.showinfo("Assembly Code Result", f"Assembly Code:\n{assembly_code}")
# Create the GUI window
window = tk.Tk()
window.title("C++ Compiler")
# Set the window size and position
window.geometry("600x400")
window.resizable(False, False)
window.configure(bg="white")
# Add a title label
title_label = tk.Label(window, text="C++ Compiler", font=("Helvetica", 20, "bold"), bg="white")
title_label.pack(pady=20)
# Add a Text widget to display the code
code_text = tk.Text(window, height=10, width=60, font=("Courier", 12))
code_text.insert(tk.END, code)
code_text.pack(pady=10)
# Create a frame to hold the buttons
button_frame = tk.Frame(window, bg="white")
button_frame.pack(pady=20)
# Function to create a separator line
def create_separator():
    separator = tk.Frame(window, height=2, width=400, bg="gray70")
    separator.pack(pady=10)
# Add buttons for each option
parse_button = tk.Button(button_frame, text="Parsing", command=parse_code, padx=10, pady=5, font=("Helvetica", 12))
parse_button.grid(row=0, column=0, padx=10)
tokenize_button = tk.Button(button_frame, text="Lexer", command=tokenize_code, padx=10, pady=5, font=("Helvetica", 12))
tokenize_button.grid(row=0, column=1, padx=10)
optimize_button = tk.Button(button_frame, text="Code Optimization", command=optimize_code, padx=10, pady=5, font=("Helvetica", 12))
optimize_button.grid(row=0, column=2, padx=10)
assembly_button = tk.Button(button_frame, text="Assembly Code", command=generate_assembly_code, padx=10, pady=5, font=("Helvetica", 12))
assembly_button.grid(row=0, column=3, padx=10)
# Add separator lines
create_separator()
create_separator()
# Start the GUI event loop
window.mainloop()


