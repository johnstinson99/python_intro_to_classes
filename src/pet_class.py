class Pet:

    def __init__(self):  # class_name, pet_name='No name'
        # if name == '':
        #     self.name = self.__class__.__name__ + ' with no name yet'
        # else:
        self.no_of_legs = 4
        self.noise = ''
        self.pet_name = ''

    def make_noise(self):
        print(self.noise)

    def do_things(self):
        print(self)
        print('no of legs = ', self.no_of_legs)
        self.make_noise()
    # def make_noise(self):
    #     print(self.__class__.sound)

    def __repr__(self):
        return self.pet_name
