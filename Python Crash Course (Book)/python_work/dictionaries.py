# 6.1
personal_details = {
    'first_name': 'maria',
    'last_name': 'kontostergiou',
    'age': 31,
    'city': 'edinburgh',
}

print(personal_details)

# 6.2
favorite_numbers = {
    'john': 3,
    'maria': 5,
    'harris': 10,
    'sam': 15,
    'euan': 32,
    }

print(favorite_numbers)

# 6.3
glossary = {
    'f-string': 'format string',
    'dictionary': 'stores key-value pairs',
    'tuple': 'an immutable list',
    'python': 'from monty-python!',
    'import_this': 'the zen of python'
}

print(f"""F-string means {glossary['f-string']}.\nDictionary {glossary[
    'dictionary']}.\nTuple is an {glossary['tuple']}.\nPython comes from {
    glossary['python']}.\nWith import_this {glossary['import_this']} appears!""")