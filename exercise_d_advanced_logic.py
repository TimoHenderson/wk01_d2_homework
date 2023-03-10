# For the following list of numbers:

numbers = [1, 6, 2, 2, 7, 1, 6, 13, 99, 7]

# 1. Print out a list of the even integers:
evens = []
for number in numbers:
    if number % 2 == 0:
        evens.append(number)
print(evens)

# 2. Print the difference between the largest and smallest value:
nums_copy = numbers.copy()
nums_copy.sort()
difference = nums_copy[-1] - nums_copy[0]
print(difference)

# 3. Print True if the list contains a 2 next to a 2 somewhere.
prev_num = None
for number in numbers:
    if number == 2 and prev_num == 2:
        print(True)
        break
    prev_num = number

# 4. Print the sum of the numbers, 
#    BUT ignore any section of numbers starting with a 6 and extending to the next 7.
#    
#    So [11, 6, 4, 99, 7, 11] would have sum of 22
sum = 0
add = True
for number in numbers:
    if number != 6 and add:
        sum += number
    elif number == 6:
        add = False
    elif number == 7:
        add = True
print(sum)

# 5. HARD! Print the sum of the numbers. 
#    Except the number 13 is very unlucky, so it does not count.
#    And numbers that come immediately after a 13 also do not count.
#    HINT - You will need to track the index throughout the loop.
#
#    So [5, 13, 2] would have sum of 5. 

sum = 0
add = True

for number in numbers:
    if number == 13:
        add = False
    elif add == False:
        add = True
    else:
        sum += number

print(sum)




