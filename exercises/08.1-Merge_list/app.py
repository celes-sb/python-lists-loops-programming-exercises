chunk_one = [ 'Lebron', 'Aaliyah', 'Diamond', 'Dominique', 'Aliyah', 'Jazmin', 'Darnell' ]
chunk_two = [ 'Lucas' , 'Jake','Scott','Amy', 'Molly','Hannah','Lucas']


def merge_list(list1, list2):
    #Your code go here:
    list3 = []
    for item in list1:
         list3.append(item)

    for item in list2:
        list3.append(item)
        
    return list3

print(merge_list(chunk_one, chunk_two))
