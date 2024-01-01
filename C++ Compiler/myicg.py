def generate_intermediate_code(parse_tree):
    intermediate_code = []
    for node in parse_tree:
        if node[0] == 'subexpression':
            intermediate_code.append(generate_intermediate_code(node[1]))
        elif node[0] == 'operator':
            if node[1] == '<<':
                # Replace cout<< with print(
                intermediate_code.append('')
            else:
                intermediate_code.append(node[1])
        elif node[0] == 'identifier':
            if node[1] == 'cout':
                # Replace cout with print(
                intermediate_code.append('print(')
            elif node[1] == 'endl':
                intermediate_code.append('')
            else:
                intermediate_code.append(node[1])
        elif node[0] == 'integer':
            intermediate_code.append(str(node[1]))
        elif node[0] == 'float':
            intermediate_code.append(str(node[1]))
        elif node[0] == 'string':
            intermediate_code.append(node[1])
        elif node[0] == 'keyword':
            intermediate_code.append(node[1])
        else:
            raise ValueError(f'Unknown node type: {node[0]}')
    code = ' '.join(intermediate_code)
    # Replace <<endl with )
    code = code.replace('<<endl', ')')
    return code
