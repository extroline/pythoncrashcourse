class Character: 
    def __init__(self, name, health,strength,):
        self.name = name 
        self.health = health
        self.strength = strength 

    def greet(self): 
        print(f"My name is {self.name}! I like cheese ")

    def instigate(self, opponent_name,): 
        
       print(f"{self.name}  Meanie meanie {opponent_name} ")

    def attack(self, opponent,):
        #who is attackinh who 
        # how much damage they deal 
        # remaining health of the one who was attacked 
        print(f"{self.name} I AM ATTACKING {opponent.name} ")
        print(f"{self.name} does {self.strength} ")
        opponent.health = opponent.health - self.strength
        print(f"{opponent.name} has {opponent.health} health remaining")



character = Character("Bob", 54, 22)
character_1 = Character("Drake", 43, 33)
character_2 = Character("Miles Tuah", 53, 52)

#print(character_2.health)
#character_1.attack(character_2)
#print(character_2.health)
while character_1.health > 0 and character_2.health > 0:

    character_1.attack(character_2)
    character_2.attack(character_1)

# print(character.name, character.health)
# print(character_1.name, character_1.health)
# print(character_2.name, character_2.health)

# character_1.greet()
# character.greet()
# character.instigate(character_1.name)