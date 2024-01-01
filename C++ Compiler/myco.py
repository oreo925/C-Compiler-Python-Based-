import re
def optimize_code(code, keywords):
    # Remove all comments
    code = re.sub('//.*', '', code)
    # Remove all header files
    code = re.sub('#include\s*<\w+(\.\w+)*>\n', '', code)
    # Remove all escape sequences
    code = re.sub('\\\\\w', '', code)
    # Remove int main() and using namespace std;
    code = re.sub('int main\s*\(\s*\)\s*{|using namespace std\s*;', '', code)
    # Replace cout<< with print
    code = code.replace('cout<<', 'print(')
    code = code.replace('cout <<', 'print(')
    code = code.replace('cout<< ', 'print(')
    code = code.replace('cout << ', 'print(')
    code = code.replace('<<', ')')
    # Replace cout<< with print
    code = code.replace('<<endl', '')
    code = code.replace(' <<endl', '')
    code = code.replace('<< endl', '')
    code = code.replace(' << endl', '')
    code = code.replace('<<endl ', '')
    code = code.replace(' <<endl ', '')
    code = code.replace('<< endl ', '')
    code = code.replace(' << endl ', '')
    code = code.replace('endl', '')
    code = code.replace(' endl', '')
    code = code.replace('endl ', '')
    code = code.replace(' endl ', '')
    # Remove all occurrences of keywords
    for keyword in keywords:
        code = re.sub('\\b' + keyword + '\\b', '', code)
    # Remove all unnecessary whitespace
    # code = re.sub('\s+', ' ', code)
    # Remove all unnecessary brackets
    code = re.sub('[{}]', '', code)
    # Remove all semicolons
    code = re.sub(';', '', code)
    return code.strip()
