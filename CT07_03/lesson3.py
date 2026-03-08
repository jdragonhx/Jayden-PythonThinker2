# Task 1

# import time

# minutes = int(input("How many minutes would you like to study?"))

# seconds = minutes * 60

# while seconds > 0:
#     print(seconds/60)
#     time.sleep(seconds)
#     seconds -= 60

# print("Congratulations")

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Task 2

# savings = 0

# while savings < 100:
#     today_save = input("How much did i save today? $")

#     savings += today_save

#     if savings >= 100:
#         print(f"Congratulations, you have saved ${savings} !!")
#         break

# -----------------------------------------------------------------------------------------------------------------------------------------------------------

# Task 3

# import random

# lives = 3
# num_of_questions = 4

# for _ in range(num_of_questions):
#     num1 = random.randint(2, 20)
#     num2 = random.randint(2, 20)
#     correct_ans = num1 * num2

#     while lives > 0:
#         answer = int(input(f"what is {num1} x {num2}? "))

#         if answer == correct_ans:
#             print("Correct!")
#             break
#         else:
#             lives -= 1
#             print(f"Incorrect. You have {lives} lives left.")
#             if lives == 0:
#                 print(f"Game over! Go see Ms Tan for rememdial")  
#                 break
#     if lives == 0:
#         break
# else:
#     print("Congratulations! You have completed the quiz.")

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Task 4

import time
import datetime

timestamp = time.time()
sg_time = time.localtime(timestamp)

