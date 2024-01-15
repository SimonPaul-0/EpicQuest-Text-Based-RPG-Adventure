import random

class Character:
    MAX_HEALTH_INCREASE = 10
    ATTACK_DEFENSE_INCREASE = 3
    EXPERIENCE_FOR_LEVEL_UP = 50

    def __init__(self, name, health, attack, defense, level=1, experience=0):
        """
        Initialize a character.

        Parameters:
        - name (str): The name of the character.
        - health (int): The initial health of the character.
        - attack (int): The initial attack strength of the character.
        - defense (int): The initial defense strength of the character.
        - level (int): The initial level of the character (default is 1).
        - experience (int): The initial experience points of the character (default is 0).
        """
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.level = level
        self.experience = experience

    def level_up(self):
        """
        Level up the character, increasing stats randomly.
        """
        self.level += 1
        self.attack += random.randint(1, self.ATTACK_DEFENSE_INCREASE)
        self.defense += random.randint(1, self.ATTACK_DEFENSE_INCREASE)
        self.health += random.randint(1, self.MAX_HEALTH_INCREASE)
        print(f"{self.name} leveled up to level {self.level}!")

    def attack_enemy(self, enemy):
        """
        Attack an enemy and deal damage.

        Parameters:
        - enemy (Enemy): The enemy to attack.
        """
        damage = max(0, self.attack - enemy.defense)
        enemy.health -= damage
        print(f"{self.name} attacks {enemy.name} and deals {damage} damage.")

    def gain_experience(self, experience):
        """
        Gain experience points.

        Parameters:
        - experience (int): The amount of experience points to gain.
        """
        self.experience += experience
        print(f"{self.name} gained {experience} experience points!")

    def show_stats(self):
        """
        Return a formatted string representing the character's stats.
        """
        return (
            f"\n{self.name}'s Stats:\n"
            f"Level: {self.level}\n"
            f"Health: {self.health}\n"
            f"Attack: {self.attack}\n"
            f"Defense: {self.defense}\n"
            f"Experience: {self.experience}\n"
        )

class Enemy:
    def __init__(self, name, health, attack, defense):
        """
        Initialize an enemy.

        Parameters:
        - name (str): The name of the enemy.
        - health (int): The initial health of the enemy.
        - attack (int): The initial attack strength of the enemy.
        - defense (int): The initial defense strength of the enemy.
        """
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense

    def attack_player(self, player):
        """
        Attack the player and deal damage.

        Parameters:
        - player (Character): The player to attack.
        """
        damage = max(0, self.attack - player.defense)
        player.health -= damage
        print(f"{self.name} attacks {player.name} and deals {damage} damage.")

    def show_stats(self):
        """
        Return a formatted string representing the enemy's stats.
        """
        return (
            f"\n{self.name}'s Stats:\n"
            f"Health: {self.health}\n"
            f"Attack: {self.attack}\n"
            f"Defense: {self.defense}\n"
        )

class Boss(Enemy):
    def __init__(self, name, health, attack, defense, special_attack):
        """
        Initialize a boss enemy.

        Parameters:
        - name (str): The name of the boss.
        - health (int): The initial health of the boss.
        - attack (int): The initial attack strength of the boss.
        - defense (int): The initial defense strength of the boss.
        - special_attack (int): The strength of the boss's special attack.
        """
        super().__init__(name, health, attack, defense)
        self.special_attack = special_attack

    def perform_special_attack(self, player):
        """
        Perform a special attack on the player.

        Parameters:
        - player (Character): The player to attack with the special attack.
        """
        damage = max(0, self.special_attack - player.defense)
        player.health -= damage
        print(f"{self.name} performs a special attack on {player.name} and deals {damage} damage.")

class Game:
    def __init__(self):
        self.player = None

    def start(self):
        """
        Start the game and manage the game loop.
        """
        print("Welcome to the Epic RPG Adventure!")
        self.player_name = input("Enter your character's name: ")
        self.player = Character(self.player_name, health=100, attack=15, defense=10)
        print(f"\nHello, {self.player.name}! Let the adventure begin.\n")

        while True:
            self.show_menu()

    def show_menu(self):
        """
        Display the game menu and handle player choices.
        """
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
            print("Thanks for playing! See you next time.")
            exit()
        else:
            print("Invalid choice. Please enter a valid option.")

    def generate_random_attribute(self, base_value, increase_range):
        """
        Generate a random attribute value within a specified range.

        Parameters:
        - base_value (int): The base value of the attribute.
        - increase_range (int): The range for random increase.

        Returns:
        - int: The randomly generated attribute value.
        """
        return base_value + random.randint(1, increase_range)

    def generate_random_enemy(self):
        """
        Generate a random enemy.

        Returns:
        - Enemy: The generated enemy.
        """
        enemy_name = random.choice(["Goblin", "Orc", "Dragon", "Witch"])
        return Enemy(
            enemy_name,
            health=self.generate_random_attribute(base_value=30, increase_range=20),
            attack=self.generate_random_attribute(base_value=8, increase_range=7),
            defense=self.generate_random_attribute(base_value=3, increase_range=5)
        )

    def generate_random_boss(self):
        """
        Generate a random boss enemy.

        Returns:
        - Boss: The generated boss enemy.
        """
        boss_name = random.choice(["Evil Wizard", "Dark Knight", "Ancient Dragon"])
        return Boss(
            boss_name,
            health=self.generate_random_attribute(base_value=100, increase_range=50),
            attack=self.generate_random_attribute(base_value=20, increase_range=10),
            defense=self.generate_random_attribute(base_value=15, increase_range=5),
            special_attack=self.generate_random_attribute(base_value=30, increase_range=15)
        )

    def handle_player_turn(self, enemy):
        """
        Handle the player's turn in the battle.

        Parameters:
        - enemy (Enemy): The enemy being battled.
        """
        self.player.attack_enemy(enemy)
        if isinstance(enemy, Boss) and random.choice([True, False]):
            enemy.perform_special_attack(self.player)
        else:
            enemy.attack_player(self.player)

    def battle_enemy(self):
        """
        Initiate a battle with a random enemy or boss.
        """
        if random.choice([True, False]):
            enemy = self.generate_random_enemy()
            print(f"A wild {enemy.name} appears!\n")
        else:
            enemy = self.generate_random_boss()
            print(f"Watch out! {enemy.name} is approaching!\n")

        while self.player.health > 0 and enemy.health > 0:
            self.handle_player_turn(enemy)

            if enemy.health <= 0:
                print(f"You defeated the {enemy.name}!")
                self.player.gain_experience(random.randint(10, 30))
                while self.player.experience >= self.player.EXPERIENCE_FOR_LEVEL_UP * self.player.level:
                    self.player.level_up()
                break

            if self.player.health <= 0:
                print(f"You were defeated by the {enemy.name}. Game Over!")
                exit()

        print(f"{self.player.name}'s remaining health: {self.player.health}\n")

if __name__ == "__main__":
    game = Game()
    game.start()
