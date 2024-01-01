import re
def parse(tokens, keywords, identifier, integer_literal, floating_literal, string_literal):
    stack = []
    while tokens:
        token = tokens.pop(0)
        if token in keywords:
            stack.append(('keyword', token))
        elif re.match(identifier, token):
            stack.append(('identifier', token))
        elif re.match(integer_literal, token):
            stack.append(('integer', int(token)))
        elif re.match(floating_literal, token):
            stack.append(('float', float(token)))
        elif re.match(string_literal, token):
            stack.append(('string', token))
        else:
            if token == '(':
                subexpression, tokens = parse(tokens, keywords, identifier, integer_literal, floating_literal, string_literal)
                stack.append(('subexpression', subexpression))
            elif token == ')':
                return stack, tokens
            else:
                stack.append(('operator', token))
    return stack, []
def generate_parse_tree(stack):
    parse_tree = []
    while stack:
        item = stack.pop(0)
        if item[0] == 'subexpression':
            parse_tree.append(('subexpression', generate_parse_tree(item[1])))
        else:
            parse_tree.append(item)
    return parse_tree

