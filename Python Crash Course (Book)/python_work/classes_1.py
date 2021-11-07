# 9.4
class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and age attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0


    def describe_restaurant(self):
        print(f"{self.restaurant_name.title()}'s cuisine type is {self.cuisine_type}.")


    def open_restaurant(self):
        print(f'{self.restaurant_name.title()} is now open!')

    def set_number_served(self, number_of_customers):
        self.number_served += number_of_customers

    def increment_number_served(self):
        self.number_served += 50


restaurant = Restaurant('labrinaki', 'souvlaki')
print(f'The restaurant has served {restaurant.number_served} customers.')
restaurant.number_served = 5
print(f'The restaurant has served {restaurant.number_served} customers.')

restaurant.set_number_served(60)
print(f'The restaurant has served {restaurant.number_served} customers.')

restaurant.increment_number_served()
print(f'The restaurant has served {restaurant.number_served} customers.')

# 9.5
class User:

    def __init__(self, first_name, last_name, age, residency, birthcountry, login_attempts):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.residency = residency
        self.birthcountry = birthcountry
        self.login_attempts = login_attempts


    def describe_user(self):
        print(f'{self.first_name.title()} {self.last_name.title()} is a resident '
            f'in {self.residency.title()} and he was born in {self.birthcountry.title()}.')

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


user_0 = User('Harris', 'Spinis', '30', 'scotland', 'greece', 0)
user_0.increment_login_attempts()
user_0.increment_login_attempts()
user_0.increment_login_attempts()
print(f'The user had tried to login in {user_0.login_attempts} times.')
user_0.reset_login_attempts()
print(f'The user had tried to login in {user_0.login_attempts} times.')
