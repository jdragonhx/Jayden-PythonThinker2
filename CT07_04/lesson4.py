# Recap 1

# import time

# seconds = int(input("Enter the number of seconds to countdown: "))
# while seconds > 0:
#     print(f"Time left: {seconds} seconds")
#     time.sleep(1)
#     seconds -= 1
# print("HAPPY NEW YEAR!")

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Task 1a

# Planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

# for planet in Planets:
#     print(planet)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Task 1b

# Planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

# Planets[3] = "Red Planet"
# for planet in Planets:
#     print(planet)


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Task 2

# Planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

# for planet in Planets: 
#     if planet == "Earth":
#         print(f"{planet} is my home planet.")
#     else:
#         print(planet)



# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Task 3

# Planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

# append_planet = input("Enter the name of a planet to add to the list: ")
# Planets.append(append_planet)

# for planet in Planets: 
#     print(planet)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------  

# Task 2 Bonus

# Planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

# Planets.insert(3, "lalaland")
# for i in range(len(Planets)): 
#     if Planets[i] == "Earth":
#         print(f"{Planets[i]} is my home planet.")
#     elif Planets[i] == "Mars":
#         print(f"{Planets[i]} , I have conquered.")
#     elif Planets[i] == "lalaland":
#         print(f"{Planets[i]} , I created this.")
#     else:
#         print(Planets[i])

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Task 3 Bonus

# user_input = ""
# countries = []
# while user_input != "end":
#     user_input = input("What country whould you like to visit? ")
#     if user_input == "end":
#         break
#     else:
#         countries.append(user_input) 
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------  

# Task 4a

# Menu = []

# while True:
#     user_input = input("Enter a menu item (or type 'done' to finish): ")
#     if user_input != "done":
#         Menu.append(user_input)
#     else:
#         break
# print("Menu Items:")
# for item in Menu:
#     print(item)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Task 4b

Menu = []

while True:
    user_input = input("Enter a menu item (or type 'done' to finish): ")
    if user_input != "done":
        Menu.append(user_input)
    else:
        break
print("Menu Items:")
for item in Menu:
    print(item)

customer_order = input("Please enter your order: ")

for item in Menu:
    if item == customer_order:
        print(f"{customer_order} is available.")
        break
    else:
        print(f"Sorry, {customer_order} is not on the menu.")

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------