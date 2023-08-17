#Remember import random function here:
import random

my_list = [4,5,734,43,45]

#The magic is here:
for number in range(10):
    randomNumber = random.randint(1, 100)
    my_list.append(randomNumber)

print(my_list)