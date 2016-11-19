from src.pet_class import Pet


class Dog(Pet):

    def __init__(self, pet_name='no name dog'):
        super().__init__()
        self.pet_name = pet_name
        self.noise = 'Woof'
