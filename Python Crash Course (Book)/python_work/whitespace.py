print('Python')

# tab space
print('\tPython') 

# new line
print('Languages\nPython\nnC\nJavaScript')

# combine new line and tab space
print('Languages\n\tPython\n\tnC\n\tJavaScript')

favorite_language = 'python '
# remove whitespaces from the right side
favorite_language.rstrip()

# nothing changed!
print(favorite_language)
# associated it with the variable's name
favorite_language = favorite_language.rstrip()

# remove whitespaces from the left side
favorite_language = ' python'
favorite_language = favorite_language.lstrip()

# remove whitespaces from both sides
favorite_language = ' python '
favorite_language = favorite_language.strip()