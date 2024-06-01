# QUESTION 1
"""Create 3 variables to store street, city and country, now create address variable to store entire address.
Use two ways of creating this variable, one using + operator and the other using f-string.
Now Print the address in such a way that the street, city and country prints in a separate line"""

# ANSWER 1
# street = 'Sharadapuram 1st Street'
# city = 'Chennai'
# country = 'India'
# address_1 = street+city+country
# print(address_1)
# print(f"Street: {street}\n City: {city}\n Country: {country}")

# QUESTION 2
'''Create a variable to store the string "Earth revolves around the sun"
Print "revolves" using slice operator
Print "sun" using negative index'''

# ANSWER 2
# my_string = "Earth revolves around the sun"
# print(my_string[6:14])
# print(my_string[-3:])

# QUESTION 3
'''Create two variables to store how many fruits and vegetables you eat in a day. 
Now Print "I eat x veggies and y fruits daily" where x and y presents vegetables and fruits that you eat everyday. 
Use python f string for this.'''

# ANSWER 3
# fruits = 3
# vegetables = 4
# print(f"I eat {vegetables} veggies and {fruits} fruits daily")

# QUESTION 4
'''I have a string variable called s='maine 200 banana khaye'. 
This of course is a wrong statement, the correct statement is 'maine 10 samosa khaye'. 
Replace incorrect words in original strong with new ones and print the new string. 
Also try to do this in one line.'''

# ANSWER 4
s='maine 200 banana khaye'
s=s.replace('banana','samosa')
s=s.replace('200','10')
print("Using two line replace:",s)

s='maine 200 banana khaye'
s=s.replace('banana','samosa').replace('200','10')
print("Using single line:",s)