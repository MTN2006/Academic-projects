import random

class Pokemon:
    def __init__(self, name: str, attack: int, defense: int, max_health: int, current_health: int):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.max_health = max_health
        self.current_health = current_health

    def __str__(self):
        return f"{self.name} (health: {self.current_health}/{self.max_health})"

    def lose_health(self, amount: int):
        if amount < 0:
            return
        self.current_health = max(self.current_health - amount, 0)

    def is_alive(self) -> bool:
        return self.current_health > 0

    def revive(self):
        self.current_health = self.max_health
        print(f"{self.name} has been revived!")

    def attempt_attack(self, other: 'Pokemon') -> tuple:
        # Randomly choose a coefficient of luck for the attacker
        luck = random.choice([0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3])
        damage = round(luck * self.attack)

        # Check if attack is successful
        if damage > other.defense:
            damage_dealt = damage - other.defense
            other.lose_health(damage_dealt)
            return True, damage
        else:
            return False, damage


def read_pokemon_from_file(filename: str) -> list:
    pokemon_list = []
    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()
        # Skip the header line
        for line in lines[1:]:
            line = line.strip()
            if not line:  # Skip empty lines
                continue

            # Split the line into attributes
            parts = line.split("|")
            if len(parts) != 4:  # Skip improperly formatted lines
                continue

            # Unpack the parts and create a Pokémon object
            name, attack, defense, max_health = parts
            pokemon = Pokemon(name, int(attack), int(defense), int(max_health), int(max_health))
            pokemon_list.append(pokemon)

    return pokemon_list


def main():
    filename = input('Enter filename: ')
    seed_val = input('Enter seed value: ')
    print()
    random.seed(seed_val)

    pokemon_list = read_pokemon_from_file(filename)

    # Randomly select two Pokémon
    pokemon1 = random.choice(pokemon_list)
    pokemon2 = random.choice(pokemon_list)

    # Ensure both Pokémon are different
    while pokemon1 == pokemon2:
        pokemon2 = random.choice(pokemon_list)

    print(f"Welcome {pokemon1} and {pokemon2}!")

    rounds = 0
    while pokemon1.is_alive() and pokemon2.is_alive() and rounds < 10:
        rounds += 1
        print(f"\nRound {rounds} begins! {pokemon1} vs {pokemon2}!")

        # Pokémon 1 attacks Pokémon 2
        attack_success, damage = pokemon1.attempt_attack(pokemon2)
        if attack_success:
            print(f"{pokemon1.name} attacks {pokemon2.name} for {damage} damage!")
            print(f"Attack is successful! {pokemon2.name} has {pokemon2.current_health} health remaining.")
        else:
            print(f"{pokemon1.name} attacks {pokemon2.name} for {damage} damage!")
            print("Attack is blocked!")

        if not pokemon2.is_alive():
            if random.choice([True, False]):
                pokemon2.revive()
            else:
                None

        # Pokémon 2 attacks Pokémon 1 if still alive
       # Check if Pokemon2 is still alive before it can attack Pokemon1
    if pokemon2.is_alive():
    # Attempt to attack Pokemon1 using Pokemon2
        attack_success, damage = pokemon2.attempt_attack(pokemon1)

    # Check if the attack was successful
    if attack_success:
        # If successful, print the damage dealt and the remaining health of Pokemon1
        print(f"{pokemon2.name} attacks {pokemon1.name} for {damage} damage!")
        print(f"Attack is successful! {pokemon1.name} has {pokemon1.current_health} health remaining.")
    else:
        # If the attack was blocked, print the damage attempted and that the attack was blocked
        print(f"{pokemon2.name} attacks {pokemon1.name} for {damage} damage!")
        print("Attack is blocked!")

    # After the attack, check if Pokemon1 is still alive
    if not pokemon1.is_alive():
        # If Pokemon1 is fainted, randomly decide whether to revive it
        if random.choice([True, False]):
            pokemon1.revive()  # Revive Pokemon1 if chosen randomly
        else:
            None  # No action if the decision was to not revive


    if pokemon1.is_alive() and not pokemon2.is_alive():
        print(f"\n{pokemon1} has won in {rounds} rounds!")
    elif pokemon2.is_alive() and not pokemon1.is_alive():
        print(f"\n{pokemon1} has won in {rounds} rounds!")
    else:
        print(f"\nIt's a tie between {pokemon1} and {pokemon2}!" )

   


if __name__ == "__main__":
    main()

