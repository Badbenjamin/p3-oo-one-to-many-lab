class Pet:

    all = []
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile",  "exotic"]
    
    def __init__(self, name, pet_type, owner = None):
        
        self.name = name
        if pet_type in self.PET_TYPES:
            self.pet_type = pet_type
        else:
            raise Exception
        
        self.owner = owner
        
        self.all.append(self)

    # def __repr__(self) -> str:
    #     return f'<{self.name}, {self.pet_type}, {self.owner}>'
        


class Owner:
    
    def __init__(self, name):
        self.name = name

    def __repr__(self) -> str:
        return f'<{self.name}>'
    
    def pets(self):
        result = []
        for pet in Pet.all:
            if pet.owner is self:
                result.append(pet)
        return result
    
    def add_pet(self, pet):
        if isinstance(pet, Pet):
            pet.owner = self
        else:
            raise Exception

    def get_sorted_pets(self):
        result = []
        # remember to iterate through list
        for pet in Pet.all:
            if pet.owner is self:
                result.append(pet)
        return sorted(result, key=lambda pet: pet.name)



# ben = Owner("ben")
# jim = Owner("jim")
# bird = Pet("birdy", "bird", ben)
# doggy = Pet("doggy", "dog", ben)
# liz = Pet("liz",  "reptile")
# stinky = Pet("stinky",  "dog", jim)

# ben.add_pet(liz)

# print(jim.get_sorted_pets())
# ben.get_sorted_pets()