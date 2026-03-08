# Task 1

# for i in range(0, 21):
#     print(i)
# for x in range(1, 31):
#     print(x)
# for y in range(2, 25, 2):
#     print(y)

# Task 2

# counter = 0
# while counter <21:
#     print(counter)
#     counter += 1

# Task 3A

# counter = 1
# while counter < 11:
#     print(counter)
#     counter +=1
# else:
#     print("count has reached 10")
    

# Task 3B

# counter = 1
# while counter < 11:
#     if counter > 5:
#         break
#     else:
#         print(counter)
#         counter +=1
# else:
#     print("count has reached 10")

# Task 4

# topping = ""
# pizza_input = ""

# while True:
#     topping = input("What topping would you like to add: ")
#     if pizza_input == "end":
#         break
#     else:
#         topping += pizza_input + " "
#         print(topping)

# print(topping)

# Task 5

max_attempt = 3
score = 0

question_answer = [
        "What is 2+2? ","4",
        "What is 7 x 4? ","28",
        "What is 22 - 22? ","0"]
for i in range(0, len(question_answer), 2):
    question = question_answer[i]
    ans = question_answer[i+1]
    attempt = 0

    while attempt < max_attempt:
        user_input = input(question)
        if user_input.lower() == ans.lower():
            print("Correct")
            score +=1
            break
        elif user_input.lower() == "skip":
            print("Skipped")
        else:
            print("WRONG!")
            attempt +=1

        if attempt == max_attempt:
            print("TOO MANY ATTEMPTS, SYSTEM CRASHING")

print(f"Your final score is {score}")