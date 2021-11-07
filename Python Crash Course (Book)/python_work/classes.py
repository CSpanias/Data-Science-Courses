# 9.1.
class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and age attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type


    def describe_restaurant(self):
        print(f"{self.restaurant_name.title()}'s cuisine type is {self.cuisine_type}.")


    def open_restaurant(self):
        print(f'{self.restaurant_name.title()} is now open!')


restaurant = Restaurant('labrinaki', 'souvlaki')
restaurant.describe_restaurant()
restaurant.open_restaurant()

# 9.2
restaurant_1 = Restaurant('taj mahal', 'indian')
restaurant_2 = Restaurant('dionisos', 'greek')
restaurant_3 = Restaurant('simply greek', 'greek')
restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()

# 9.3
class User:

    def __init__(self, first_name, last_name, age, residency, birthcountry):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.residency = residency
        self.birthcountry = birthcountry


    def describe_user(self):
        print(f'{self.first_name.title()} {self.last_name.title()} is a resident '
            f'in {self.residency.title()} and he was born in {self.birthcountry.title()}.')


user_0 = User('Harris', 'Spinis', '30', 'scotland', 'greece')
user_1 = User('Maria', 'Kontopeniou', '40', 'england', 'france')

user_0.describe_user()
user_1.describe_user()

