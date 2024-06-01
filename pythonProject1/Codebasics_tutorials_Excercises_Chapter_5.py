# QUESTION 1
'''
Let us say your expense for every month are listed below,
January - 2200
February - 2350
March - 2600
April - 2130
May - 2190
Create a list to store these monthly expenses and using that find out,
'''
my_exp = [['January', 2200], ['Feburary', 2350], ['March', 2600], ['April', 2130], ['May', 2190]]

# In Feb, how many dollars you spent extra compare to January?
# print(my_exp[1][1])

# Find out your total expense in first quarter (first three months) of the year.
# print(my_exp[0][1]+my_exp[1][1]+my_exp[2][1])

# Find out if you spent exactly 2000 dollars in any month
# my_exp_1=[2200, 2350, 2600, 2130, 2190]
# print("Did I spend $2000 in any month ?:",2000 in my_exp_1)

# June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
# june_m = ['June', 1980]
# my_exp.append(june_m)
# print(my_exp)

'''You returned an item that you bought in a month of April and got a refund of 200$. 
Make a correction to your monthly expense list based on this.'''
# my_exp[3][1] = my_exp[3][1] - 200
# print(my_exp)

# QUESTION 2
'''You have a list of your favourite marvel super heros.
heros=['spider man','thor','hulk','iron man','captain america']
'''
heros = ['spider man', 'thor', 'hulk', 'iron man', 'captain america']

# Length of the list
print(len(heros))

# Add 'black panther' at the end of this list
heros.append('black panther')
print(heros)

'''You realize that you need to add 'black panther' after 'hulk',
so remove it from the list first and then add it after 'hulk' '''
heros.pop()
print(heros)
heros.insert(3,'blank panther')
print(heros)

'''Now you don't like thor and hulk because they get angry easily.
So you want to remove 'thor and 'hulk' from list and replace them with doctor strange (because he is cool).
Do that with one line of code.'''
heros[1:3]=['doctor Strange']
print(heros)

'''Sort the heros list in alphabetical order 
(Hint. Use dir() functions to list down all functions available in list)'''

heros.sort()
print(heros)