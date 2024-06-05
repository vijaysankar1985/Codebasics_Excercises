# OUESTION 1
#
# After flipping a coin 10 times you got this result,
# result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
# Using for loop figure out how many times you got heads

# CODE 1
# result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
#
# cnt = 0
# for head in result:
#     if head == "heads":
#         cnt+=1
#
# print("The no.of. heads is: ", cnt)

# QUESTION 2
# Print square of all numbers between 1 to 10 except even numbers

# CODE 2
# for sq in range (1,11,2):
#     sq = sq*sq
#     print(sq)


# QUESTION 3
# Your monthly expense list (from Jan to May) looks like this,
# expense_list = [2340, 2500, 2100, 3100, 2980]
# Write a program that asks you to enter an expense amount and
# the program should tell you in which month that expense occurred.
# If expense is not found then it should print that as well.

# CODE 3
# expense_list = [2340, 2500, 2100, 3100, 2980]
# user_input = int(input("Enter the expense amount: "))
#
# if user_input not in expense_list:
#     print(f"The entered amount {user_input} is not found.")
# else:
#     for exp in range(len(expense_list)):
#         if expense_list[exp] == user_input:
#             print(f"The amount: {user_input} belongs to month: {exp+1}")
#             continue

# QUESTION 4:
# Lets say you are running a 5 km race. Write a program that,
#
# Upon completing each 1 km asks you "are you tired?"
# If you reply "yes" then it should break and print "you didn't finish the race"
# If you reply "no" then it should continue and ask "are you tired" on every km
# If you finish all 5 km then it should print congratulations message

# CODE 4
# for i in range(0,6):
#     user_input = input("Are you tired? Please answer with Yes/ No: ")
#     if user_input == 'Yes':
#         print(f"Sorry! You did not complete the race.You completed {i} km. All the best for future.")
#         break
#     elif user_input == 'No':
#         print(f"{i} km completed...")
#         if i >=5 and user_input == 'No':
#             print("Congratulations! You have completed the 5km race.")
#         continue

# QUESTION 5
# Write a program that prints following shape
#
# *
# **
# ***
# ****
# *****

# CODE 5
n = int(input("Enter the no.of. lines for star pattern: "))
for i in range(n+1):
    print(i*"*")
