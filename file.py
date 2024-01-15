import random

class Character:
    def __init__(self, name, health, attack, defense, level=1, experience=0):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.level = level
        self.experience = experience

    def level_up(self):
        self.level += 1
        self.attack += random.randint(1, 3)
        self.defense += random.randint(1, 3)
        self.health += random.randint(5, 10)
        print(f"{self.name} leveled up to level {self.level}!")

    def attack_enemy(self, enemy):
        damage = max(0, self.attack - enemy.defense)
        enemy.health -= damage
        print(f"{self.name} attacks {enemy.name} and deals {damage} damage.")

    def gain_experience(self, experience):
        self.experience += experience
        print(f"{self.name} gained {experience} experience points!")

    def show_stats(self):
        print(f"\n{self.name}'s Stats:")
        print(f"Level: {self.level}")
        print(f"Health: {self.health}")
        print(f"Attack: {self.attack}")
        print(f"Defense: {self.defense}")
        print(f"Experience: {self.experience}\n")

class Enemy:
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense

    def attack_player(self, player):
        damage = max(0, self.attack - player.defense)
        player.health -= damage
        print(f"{self.name} attacks {player.name} and deals {damage} damage.")

    def show_stats(self):
        print(f"\n{self.name}'s Stats:")
        print(f"Health: {self.health}")
        print(f"Attack: {self.attack}")
        print(f"Defense: {self.defense}\n")

def main():
    print("Welcome to the Text RPG Adventure!")
    player_name = input("Enter your character's name: ")

    player = Character(player_name, health=100, attack=15, defense=10)

    print(f"\nHello, {player.name}! Let the adventure begin.\n")

    while True:
        print("Options:")
        print("1. Battle an enemy")
        print("2. Check character stats")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            enemy_name = random.choice(["Goblin", "Orc", "Dragon", "Witch"])
            enemy = Enemy(enemy_name, health=random.randint(20, 50), attack=random.randint(5, 15), defense=random.randint(2, 8))
            print(f"A wild {enemy.name} appears!\n")
            
            while player.health > 0 and enemy.health > 0:
                player.attack_enemy(enemy)
                if enemy.health <= 0:
                    print(f"You defeated the {enemy.name}!")
                    player.gain_experience(random.randint(10, 30))
                    if player.experience >= 50 * player.level:
                        player.level_up()
                    break
                enemy.attack_player(player)
                if player.health <= 0:
                    print(f"You were defeated by the {enemy.name}. Game Over!")
                    exit()

        elif choice == '2':
            player.show_stats()

        elif choice == '3':
            print("Thanks for playing! See you next time.")
            exit()

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
