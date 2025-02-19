class Zoo:
    __animals = 0

    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.mammals = list()
        self.fishes = list()
        self.birds = list()

    def add_animal(self, species, name):
        if species == 'mammal':
            self.mammals.append(name)
        elif species == 'fish':
            self.fishes.append(name)
        elif species == 'bird':
            self.birds.append(name)

        Zoo.__animals += 1

    def get_info(self, species):
        result = ''
        if species == 'mammal':
            result += f"Mammals in {self.zoo_name}: {', '.join(self.mammals)}"
        elif species == 'fish':
            result += f"Fishes in {self.zoo_name}: {', '.join(self.fishes)}"
        elif species == 'bird':
            result += f"Birds in {self.zoo_name}: {', '.join(self.birds)}"

        result += f"\nTotal animals: {Zoo.__animals}"
        return result


name_of_zoo = input()
zoo = Zoo(name_of_zoo)
number = int(input())

for i in range(number):
    info = input().split(' ')
    specie = info[0]
    type_of_animal = info[1]
    zoo.add_animal(specie, type_of_animal)

additional_info = input()
print(zoo.get_info(additional_info))
