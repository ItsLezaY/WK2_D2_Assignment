# Exercise 1

# Using the given list, print out a filtered version of the list with only the numbers that are less than ten


alist = [1,11,14,5,8,9]

filtered_list = []

for num in alist:
    if num < 10:
        filtered_list.append(num)

print(filtered_list)





# Exercise 2

# Merge and sort the two lists below
# Hint: You can use the .sort() method

list_1 = [1,2,3,4,5,6]
list_2 = [3,4,5,6,7,8,10]

merged_list = list_1 + list_2
merged_list.sort()

print(merged_list)





# Exercise 3 

# Square every number from 1 to 15

squared_list = []

for num in range(1, 16):    # range 1 thru 16 so 15 ** 2 is in output
    squared_list.append(num ** 2)

print(squared_list)





# Exercise 4

# Using List Comprehension and the given list, print out a filtered list with only the names that start with the letter 'a'. The names in the outputted list should be title cased and have no whitespace.

# Hint: There is an empty string at the end of the list you will need to account for.

names_list = ['   amy', 'Briant', 'Ryan ', ' Alex', 'steve', '  ']
# last value is an empty string
# expected output = ['Amy', 'Alex']

filtered_list = [name.strip().title() for name in names_list if name.strip().lower().startswith('a')]

print(filtered_list)





# Exercise 5

# Print all Prime numbers from 1 to 100

# Hint: A Prime # is any # that is ONLY divisible by 1 and itself. So think how you can iterate through the list of #s from 1 to 100 and check to see if its divisible by ANY # below it.

# The For/Each might be very helpful for this question. https://www.geeksforgeeks.org/using-else-conditional-statement-with-for-loop-in-python/

# potentially utilizing range

def prime_number(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

for num in range(1, 101):
    if prime_number(num):
        print(num)











