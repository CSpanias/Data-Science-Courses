# 8.12
def sandwich_maker(*args):
    print('\nYou sandwich will contain:')
    for arg in args:
        print(f'-{arg}')

sandwich_maker('ham')
sandwich_maker('ham', 'cheese')
sandwich_maker('ham', 'chicken', 'egg', 'cheese')

# 8.13
def build_profile(first, last, **user_info):
    """
    Build a dictionary containing everything we know about a user.
    """
    user_info['first_name']= first
    user_info['last_name']= last
    return user_info


user_profile = build_profile('Harris', 'Polikarpos', age = 30)
user_profile_1 = build_profile('Harris', 'Tade', age=30, height=180)
print(user_profile)
print(user_profile_1)

# 8.14
def car_info(manufacturer, model_name, **cars):
    cars['manufacturer'] = manufacturer
    cars['model_name'] = model_name
    return cars


car_1 = car_info('subaru', 's4')
car_2 = car_info('subaru', 's4', color='green', tow_package=True)
print(car_1)
print(car_2)