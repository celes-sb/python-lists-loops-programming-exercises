
all_names = ["Romario","Boby","Roosevelt","Emiliy", "Michael", "Greta", "Patricia", "Danzalee"]

#Your code go here:
def filter_r(names):
    if names[0] == 'R':
        return names

resulting_names = list(filter(filter_r, all_names))
print(resulting_names)




