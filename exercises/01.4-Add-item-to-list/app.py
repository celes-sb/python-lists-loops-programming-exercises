#Remember import random function here:
import random

my_list = [4,5,734,43,45]

#The magic is here:
for num in range(10):
    randomNums = random.randint(1, 100)
    my_list.append(randomNums)
print(my_list)