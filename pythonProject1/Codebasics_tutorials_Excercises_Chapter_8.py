# QUESTION 1
# india = ["mumbai", "banglore", "chennai", "delhi"]
# pakistan = ["lahore","karachi","islamabad"]
# bangladesh = ["dhaka", "khulna", "rangpur"]

# QUESTIION i
# user_input = input("Enter a city name: ").lower()
# if user_input in india:
#     print(f"The city {user_input} is in India ")
# elif user_input in pakistan:
#     print(f"The city {user_input} is in Pakistan ")
# elif user_input in bangladesh:
#     print(f"The city {user_input} is in Bangladesh ")
# else:
#     print(f"The city {user_input} is not in our list. Sorry!")

# QUESTION ii
# user_input_1 = input("Enter the 1st City Name: ")
# user_input_2 = input("Enter the 2nd City Name: ")
#
# if user_input_1 in india and user_input_2 in india:
#     print("Both the cities are in the same country, India.")
# elif user_input_1 in pakistan and user_input_2 in pakistan:
#     print("Both the cities are in the same country, Pakistan.")
# elif user_input_1 in bangladesh and user_input_2 in bangladesh:
#     print("Both the cities are in the same country, Bangladesh.")
# else:
#     print("Both the cities are not in the same country.")


# QUESTION 2
user_diab = int(input("Enter your blood glucose level: "))
if user_diab < 80:
    print("Beware! Your blood glucose level is too low. Take immediate action.")
elif 80 <= user_diab <= 100:
    print("Congratulations! Your blood glucose is normal.")
else:
    print("Attention! Your blood glucose level is high.")