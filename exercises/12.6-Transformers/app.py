incoming_ajax_data = [
    { "name": 'Mario', "last_name": 'Montes' },
    { "name": 'Joe', "last_name": 'Biden' },
    { "name": 'Bill', "last_name": 'Clon' },
    { "name": 'Hilary', "last_name": 'Mccafee' },
    { "name": 'Bobby', "last_name": 'Mc birth' }
]

#Your code go here:
def data_transformer(data):
    result = data['name'] + " " + data['last_name']
    return result

new_list = list(map(data_transformer, incoming_ajax_data[0]))
print(new_list)

#pendiente de terminar