# 8.1 
def display_message():
    """
    Displays a message demonstrating
    what I am learning in this chapter! 
    """
    print("I am learning to define functions,\nand what parameters, arguments "
        "and docstrings are!")

display_message()

# 8.2
def favorite_book(title, author):
    """
    Displays the inputed book title and author in a message as your favorite book.
    """
    print(f'One of my favorite books is {title} by {author}!')

favorite_book('The Spinoza Problem', 'Irvin Yalom')

# 8.3
def make_shirt(size, message):
    print(f'The size of the shirt will be {size.upper()}.\nThe printed message'
    f'will be "{message}".')

make_shirt('M', 'Molly')
make_shirt(message = 'Molly', size = 'M')

# 8.4
def make_shirt(size = 'Large', message = 'I love Python!'):
    print(f'The size of the shirt will be {size.upper()}.\nThe printed message'
    f'will be "{message}"')

make_shirt()
make_shirt('Medium')
make_shirt('Small', 'I really love Python!')

# 8.5
def describe_city(city_name, country = 'Iceland'):
    print(f'{city_name.title()} is in {country.title()}.')

describe_city('Athens', 'Greece')
describe_city('Reykjavik')
describe_city('London', 'the United Kingdom')


