# Recap 1a

# Favorite_foods = ["Air", "Water", "dirt", "stone", "lava"]
# print(Favorite_foods)

# Recap 1b

# Favorite_foods.pop(2)
# print(Favorite_foods)

# Recap 1c

# food.insert(2, "pizza")
# food.append("sushi")

# for item in food:
#     print(item)

# Task 1

# import random

# numbers = []

# for i in range(100):
#     num = random.randint(1, 1000)
#     numbers.append(num)

# print(numbers)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Task 2

# import random

# numbers = []

# for i in range(100):
#     num = random.randint(1, 1000)
#     if num not in numbers:
#         numbers.append(num)
#     else:
#         while num in numbers:
#             num = random.randint(1, 1000)
#         numbers.append(num)

# print(numbers)
# print(len(numbers))

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Task 3

# import random

# scores = []
# for i in range(100):
#     score = random.randint(0, 100)
#     scores.append(score)

# max_score = max(scores)
# min_score = min(scores)

# print(f"Average score: {sum(scores) / len(scores)}")
# print(f"Highest score: {max_score}")
# print(f"Lowest score: {min_score}")

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Task 4a & 4b

# namelist = ["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace", "Hannah", "Ian", "Jack"]

# heightlist = [165, 172, 158, 180, 170, 175, 160, 168, 174, 169]
# tallest_height = max(heightlist)
# tallest_index = heightlist.index(tallest_height)
# tallest_name = namelist[tallest_index]
# print(f"The tallest person is {tallest_name} with a height of {tallest_height} cm.")
# print(f"The shortest person is {namelist[heightlist.index(min(heightlist))]} with a height of {min(heightlist)} cm.")

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Task 5

# import random

# pokemon_list = ["Bulbasaur", "Charmander", "Squirtle", "Pikachu", "Eevee", "Jigglypuff", "Meowth", "Psyduck", "Snorlax", "Mewtwo", "Chikorita", "Cyndaquil", "Totodile", "Togepi", "Marill", "Sudowoodo", "Hoothoot", "Ledyba", "Spinarak", "Crobat", "Treecko", "Torchic", "Mudkip", "Poochyena", "Zigzagoon", "Wurmple", "Lotad", "Seedot", "Taillow", "Wingull", "Ralts", "Surskit", "Shroomish", "Slakoth", "Nincada", "Whismur", "Makuhita", "Meditite", "Electrike", "Numel", "Spoink", "Spheal", "Clamperl", "Relicanth", "Luvdisc", "Bagon", "Beldum",  "Starly", "Bidoof", "Kricketot", "Shinx", "Budew", "Cranidos"]

# powers = [random.randint(50, 100000) for _ in range(len(pokemon_list))]

# pokemon_1 = random.choice(pokemon_list)
# pokemon_2 = random.choice(pokemon_list)

# while pokemon_1 == pokemon_2:
#     pokemon_2 = random.choice(pokemon_list)
# index_1 = pokemon_list.index(pokemon_1)
# index_2 = pokemon_list.index(pokemon_2)

# power_1 = powers[index_1]
# power_2 = powers[index_2]

# print(f"{pokemon_1} (Power: {power_1}) vs {pokemon_2} (Power: {power_2})")

# if power_1 > power_2:
#     print(f"{pokemon_1} wins!")
# elif power_2 > power_1:
#     print(f"{pokemon_2} wins!")
# else:
#     print("It's a tie!")

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Gambling Game

import random

balance = 1000000

while balance > 0:
    print(f"Current balance: ${balance}")
    bet = int(input("Enter your bet amount (or 0 to quit): "))
    if bet == 0:
        print("Thanks for playing!")
        break
    if bet > balance:
        print("You cannot bet more than your current balance.")
        continue

    user_number = int(input("Choose a number between 1 and 20: "))
    winning_number = random.randint(1, 20)

    game_result = f"You chose {user_number}. The winning number is {winning_number}."
    print(game_result)

    if user_number == winning_number:
        winnings = bet * 10
        balance += winnings
        print(f"Congratulations! You guessed the correct number {winning_number} and won ${winnings}!")
    else:
        balance -= bet
        print(f"Sorry, the correct number was {winning_number}. You lost your bet of ${bet}.")
        
        leave_game = input("Do you want to continue playing? (yes/no): ").lower()
        if leave_game == "no":
            print("Thanks for playing!")
            break

if balance == 0:
    print("You have run out of money. Game over!")


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------  