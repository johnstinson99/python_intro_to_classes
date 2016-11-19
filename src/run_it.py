from src.dog_class import Dog
from src.cat_class import Cat
my_dog = Dog()
print(my_dog)
print('no of legs = ', my_dog.no_of_legs)
my_dog.make_noise()
print()

my_cat = Cat(pet_name='Tinkerbell')
print(my_cat)
print(my_cat.no_of_legs)
my_cat.make_noise()
print()

pet_list = [my_dog, my_cat]
for my_pet in pet_list:
    my_pet.do_things()
    # print(my_pet)
    # print(my_pet.no_of_legs)
    # my_pet.make_noise()
    # print()

# my_dog_list = [Dog('dog #' + str(i)) for i in range(20)]
# print(my_dog_list)
