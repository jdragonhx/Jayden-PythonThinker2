"""
============================================================
Q1. Hero Quest
============================================================
A hero goes on an adventure, starting at Full Health.
He fights monsters and loses health randomly each round.

Requirements:
- Start with 100 health
- Print starting message
- Lose between 1 to 15 health each round (random)
- Use a while-loop
- Continue until health <= 0
- Print total number of battles fought

============================================================
"""

# ============================================================
# Step 1: Import required module
# ============================================================



# ============================================================
# Step 2: Initialize variables
# ============================================================



# ============================================================
# Step 3: Print starting message
# ============================================================



# ============================================================
# Step 4: Create while-loop for battles
# ============================================================
# - Randomly reduce health between 1 and 15
# - Increase battle counter
# - Print updated health
# ============================================================



# ============================================================
# Step 5: Print final result
# ============================================================
# Print in this format:
# He fought xxx battles, and died
# ============================================================

import random
health = 100
battles = 0
print("The hero starts his adventure with health: 100")
while health > 0:
    damage = random.randint(1, 15)
    health -= damage
    battles += 1
    print(f"After fighting monsters, the hero's health is now: {health}")
print(f"After fighting monsters, his health is now: {health}")
print(f"He fought {battles} battles, and died.")

# -------------------------------------------------------------------------------------------------------------------

