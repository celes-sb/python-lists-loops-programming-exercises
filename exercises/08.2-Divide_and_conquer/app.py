list_of_numbers = [4,	80,	85,	59,	37, 25, 5, 64, 66, 81, 20, 64, 41, 22, 76, 76, 55, 96, 2, 68]


#Your code here:
def merge_two_list(list_of_numbers):
    odd_list = []
    even_list = []

    for number in list_of_numbers:
        if number % 2 == 0:
            even_list.append(number)
        elif number % 2 != 0:
            odd_list.append(number)

    mergeTwoList = [odd_list, even_list]
    return mergeTwoList


print(merge_two_list(list_of_numbers))

