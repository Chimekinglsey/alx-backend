my_dict = {}
names = ['John', 'Dwayne', 'Doe']
i = 0
my_list = []

for item in names:
    my_dict.update({f'Person {i}': {item}})
    my_list.append(f"Person {i}: {item}")
    i += 1
for id, name in my_dict.items():
    print(f'{id}: {name}')
print(my_list)