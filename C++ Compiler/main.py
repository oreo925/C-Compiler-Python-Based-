from mylexer import tokenize
from myparser import parse, generate_parse_tree
from myass import convert_to_assembly
import myicg
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
tokens, keywords, identifier, integer_literal, floating_literal, string_literal = tokenize(code)
stack, remaining_tokens = parse(tokens, keywords, identifier, integer_literal, floating_literal, string_literal)
if remaining_tokens:
    error_line = len(tokens) - len(remaining_tokens) + 1
    print(f"Parsing error at line {error_line}")
else:
    parse_tree = generate_parse_tree(stack)
    for element in parse_tree:
        print(element)
    print("No parsing errors\n")
    intermediate_code = myicg.generate_intermediate_code(parse_tree)
    # Print the intermediate code
    print("Intermediate Code:")
    print(intermediate_code)
    # Optimize the code
    optimized_code = myco.optimize_code(intermediate_code, keywords)
    # Print the optimized code
    print("\nOptimized Code:")
    print(optimized_code)
    # Execute the optimized code
    print("Output:")
    exec(optimized_code)
    # Show the assembly code
    assembly_code = convert_to_assembly(code)
    print(assembly_code)
    
    
    