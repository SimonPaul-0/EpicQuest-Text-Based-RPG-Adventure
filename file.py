import random

class Character:
    MAX_HEALTH_INCREASE = 10
    ATTACK_DEFENSE_INCREASE = 3
    EXPERIENCE_FOR_LEVEL_UP = 50

    def __init__(self, name, health, attack, defense, level=1, experience=0, skill_points=0):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.level = level
        self.experience = experience
        self.skill_points = skill_points

    def level_up(self):
        self.level += 1
        self.experience = 0  # Reset experience to 0 after leveling up
        self.skill_points += 1  # Gain a skill point on level up
        print(f"{self.name} leveled up to level {self.level}!")

        while self.skill_points > 0:
            print(self.show_stats())
            print("Assign your skill point:")
            print("1. Increase Health")
            print("2. Increase Attack")
            print("3. Increase Defense")

            stat_choice = int(input("Enter your choice (1-3): "))

            if stat_choice not in [1, 2, 3]:
                print("Invalid choice. Please choose again.")
                continue

            if stat_choice == 1:
                self.health += random.randint(10, self.MAX_HEALTH_INCREASE)
                print(f"Health increased! Current Health: {self.health}")
            elif stat_choice == 2:
                self.attack += random.randint(10, self.ATTACK_DEFENSE_INCREASE)
                print(f"Attack increased! Current Attack: {self.attack}")
            elif stat_choice == 3:
                self.defense += random.randint(10, self.ATTACK_DEFENSE_INCREASE)
                print(f"Defense increased! Current Defense: {self.defense}")

            self.skill_points -= 1

    def attack_enemy(self, enemy):
        damage = max(0, self.attack - enemy.defense)
        enemy.health -= damage
        print(f"{self.name} attacks {enemy.name} and deals {damage} damage.")

    def gain_experience(self, experience):
        self.experience += experience
        print(f"{self.name} gained {experience} experience points!")

    def show_stats(self):
        return (
            f"\n{self.name}'s Stats:\n"
            f"Level: {self.level}\n"
            f"Health: {self.health}\n"
            f"Attack: {self.attack}\n"
            f"Defense: {self.defense}\n"
            f"Experience: {self.experience}\n"
            f"Skill Points: {self.skill_points}\n"
        )

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
        return (
            f"\n{self.name}'s Stats:\n"
            f"Health: {self.health}\n"
            f"Attack: {self.attack}\n"
            f"Defense: {self.defense}\n"
        )

class Boss(Enemy):
    def __init__(self, name, health, attack, defense, special_attack):
        super().__init__(name, health, attack, defense)
        self.special_attack = special_attack

    def perform_special_attack(self, player):
        damage = max(0, self.special_attack - player.defense)
        player.health -= damage
        print(f"{self.name} performs a special attack on {player.name} and deals {damage} damage.")

class Game:
    def __init__(self):
        self.player = None

    def start(self):
        print("Welcome to the Epic RPG Adventure!")
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
            print(self.player.show_stats())
        elif choice == '3':
            restart = input("Do you want to restart? (yes/no): ").lower()
            if restart == 'yes':
                self.start()
            else:
                print("Thanks for playing! See you next time.")
                exit()
        else:
            print("Invalid choice. Please enter a valid option.")

    def generate_random_attribute(self, base_value, increase_range):
        return base_value + random.randint(10, increase_range)

    def generate_random_enemy(self):
        enemy_name = random.choice(["Goblin", "Orc", "Dragon", "Witch"])
        return Enemy(
            enemy_name,
            health=self.generate_random_attribute(base_value=30, increase_range=20),
            attack=self.generate_random_attribute(base_value=8, increase_range=7),
            defense=self.generate_random_attribute(base_value=3, increase_range=5)
        )

    def generate_random_boss(self):
        boss_name = random.choice(["Evil Wizard", "Dark Knight", "Ancient Dragon"])
        return Boss(
            boss_name,
            health=self.generate_random_attribute(base_value=100, increase_range=50),
            attack=self.generate_random_attribute(base_value=20, increase_range=10),
            defense=self.generate_random_attribute(base_value=15, increase_range=5),
            special_attack=self.generate_random_attribute(base_value=30, increase_range=15)
        )

    def handle_player_turn(self, enemy):
        self.player.attack_enemy(enemy)
        if isinstance(enemy, Boss) and random.choice([True, False, False, False]):  # Decreased boss appearance probability
            enemy.perform_special_attack(self.player)
        else:
            enemy.attack_player(self.player)

    def battle_enemy(self):
        if random.choice([True, False, False]):  # Decreased boss appearance probability
            enemy = self.generate_random_enemy()
            print(f"A wild {enemy.name} appears!\n")
        else:
            enemy = self.generate_random_boss()
            print(f"Watch out! {enemy.name} is approaching!\n")

        while self.player.health > 0 and enemy.health > 0:
            self.handle_player_turn(enemy)

            if enemy.health <= 0:
                print(f"You defeated the {enemy.name}!")
                self.player.gain_experience(random.randint(30, 80))  # Increased experience gain
                self.player.health = 100  # Restore player's health after battle
                while self.player.experience >= self.player.EXPERIENCE_FOR_LEVEL_UP * self.player.level:
                    self.player.level_up()
                break

            if self.player.health <= 0:
                print(f"You were defeated by the {enemy.name}. Game Over!")
                restart = input("Do you want to restart? (yes/no): ").lower()
                if restart == 'yes':
                    self.start()
                else:
                    print("Thanks for playing! See you next time.")
                    exit()

        print(f"{self.player.name}'s remaining health: {self.player.health}\n")

if __name__ == "__main__":
    game = Game()
    game.start()
