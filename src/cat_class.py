from src.pet_class import Pet


class Cat(Pet):

    def __init__(self, pet_name='Cat with no name'):
        super().__init__()
        self.pet_name = pet_name
        self.noise = 'Miow'
