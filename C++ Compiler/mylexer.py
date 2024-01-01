import re
def tokenize(code):
    keywords = ['auto', 'break', 'case', 'char', 'const', 'continue', 'default',
                'do', 'double', 'else', 'enum', 'extern', 'float', 'for', 'goto',
                'if', 'int', 'long', 'register', 'return', 'short', 'signed',
                'sizeof', 'static', 'struct', 'switch', 'typedef', 'union',
                'unsigned', 'void', 'volatile', 'while']
    identifier = r'[a-zA-Z_]\w*'
    integer_literal = r'\d+'
    floating_literal = r'\d+\.\d+f?'
    string_literal = r'".*"'
    punctuators = r'\{|\}|\[|\]|\(|\)|\.|->|\+\+|--|&|\*|\+|-|~|!|/|%|<<|>>|<|<=|>|>=|==|!=|^|&amp;|\||&&|\|\||\?|:|;|\.+|,|#|##|\.\.\.'
    pattern = '|'.join([floating_literal, integer_literal, identifier, string_literal, punctuators] + keywords)
    tokens = re.findall(pattern, code)
    return tokens, keywords, identifier, integer_literal, floating_literal, string_literal


