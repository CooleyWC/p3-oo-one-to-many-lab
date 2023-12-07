class Pet:

    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]

    all = []

    def __init__(self, name, pet_type, owner=None):
        self.name = name
        self.owner = owner

        if pet_type in Pet.PET_TYPES:
            self.pet_type = pet_type
            Pet.all.append(self)
        else:
            raise Exception("must be in PET-TYPES")

class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        owners_pets = [pet for pet in Pet.all if pet.owner == self]
        return owners_pets
    
    def add_pet(self, pet):
        if isinstance(pet, Pet):
            pet.owner = self
        else:
            raise Exception('must be a pet')
        
    def get_sorted_pets(self):
        sorted_pets = Pet.all
        sorted_pets = sorted(sorted_pets, key=lambda pet:pet.name)
        return sorted_pets

        



# dog1 = Pet('will', 'dog', 'boss')
# print(Pet.all)