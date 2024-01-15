import random

class Character:
    MAX_HEALTH_INCREASE = 10
    ATTACK_DEFENSE_INCREASE = 3
    EXPERIENCE_FOR_LEVEL_UP = 50

    def __init__(self, name, health, attack, defense, level=1, experience=0):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.level = level
        self.experience = experience

    def level_up(self):
        self.level += 1
        self.attack += random.randint(1, self.ATTACK_DEFENSE_INCREASE)
        self.defense += random.randint(1, self.ATTACK_DEFENSE_INCREASE)
        self.health += random.randint(1, self.MAX_HEALTH_INCREASE)
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

class Game:
    def __init__(self):
        self.player = None

    def start(self):
        print("Welcome to the Text RPG Adventure!")
        self.player_name = input("Enter your character's name: ")
        self.player = Character(self.player_name, health=100, attack=15, defense=10)
        print(f"\nHello, {self.player.name}! Let the adventure begin.\n")

        while True:
            self.show_menu()

    def show_menu(self):
        print("Options:")
        print("1. Battle an enemy")
        print("2. Check character stats")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            self.battle_enemy()
        elif choice == '2':
            self.player.show_stats()
        elif choice == '3':
            print("Thanks for playing! See you next time.")
            exit()
        else:
            print("Invalid choice. Please enter a valid option.")

    def generate_random_attribute(self, base_value, increase_range):
        return base_value + random.randint(1, increase_range)

    def generate_random_enemy(self):
        enemy_name = random.choice(["Goblin", "Orc", "Dragon", "Witch"])
        return Enemy(
            enemy_name,
            health=self.generate_random_attribute(base_value=30, increase_range=20),
            attack=self.generate_random_attribute(base_value=8, increase_range=7),
            defense=self.generate_random_attribute(base_value=3, increase_range=5)
        )

    def battle_enemy(self):
        enemy = self.generate_random_enemy()
        print(f"A wild {enemy.name} appears!\n")

        while self.player.health > 0 and enemy.health > 0:
            self.player.attack_enemy(enemy)
            if enemy.health <= 0:
                print(f"You defeated the {enemy.name}!")
                self.player.gain_experience(random.randint(10, 30))
                while self.player.experience >= self.player.EXPERIENCE_FOR_LEVEL_UP * self.player.level:
                    self.player.level_up()
                break
            enemy.attack_player(self.player)
            if self.player.health <= 0:
                print(f"You were defeated by the {enemy.name}. Game Over!")
                exit()

        print(f"{self.player.name}'s remaining health: {self.player.health}\n")


if __name__ == "__main__":
    game = Game()
    game.start()
