original_array = ['by', 'planet', 'abc', '123', 'null', '9503']
max_length = 3

new_array = []
for word in original_array:
    if len(word) <= max_length:
        new_array.append(word)

print(new_array)