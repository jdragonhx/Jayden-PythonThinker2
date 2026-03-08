# Recap 1a

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

# Task 1

contacts = []
contact1 = ["John", "98453126", "john@gmail.com"]
contact2 = ["Adam", "93029102", "adam@gmail.com"]
contact3 = ["Sylvia", "87894032", "sylvia@gmail.com"]

contacts.append(contact1)
contacts.append(contact2)
contacts.append(contact3)

for contact in contacts:
    for detail in contact:
        print(detail)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Task 2

students = [
    ["Olivia", "F"],
    ["Liam", "M"],
    ["Ava", "F"],
    ["Noah", "M"],
    ["Isabella", "F"],
    ["William", "M"],
    ["Emma", "F"],
]

# Task 3

pokemons = [
    "Bulbasaur",
    "Charmander",
    "Squirtle",
    "Pikachu",
    "Eevee",
    "Snorlax",
    "Mewtwo",
    "Gengar",
    "Dragonite",
    "Mew",
    
]