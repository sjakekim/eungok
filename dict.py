family = {'mom':'kim', 'dad':'choi', 'baby': 'choi'}
print(family.keys())
print(family.values())
print(family.items())

result = dict([('a',1),('b',2 ),('c',3)])
print(result)


# name_and_ages = [['alice', 5], ['Bob', 13]]
# dict(name_and_ages)
# {'alice': 5, 'Bob': 13}
# name_and_ages = [('alice', 5), ('Bob', 13)]
# dict(name_and_ages)
# {'alice': 5, 'Bob': 13}
# name_and_ages = (('alice', 5), ('Bob', 13))
# dict(name_and_ages)
# {'alice': 5, 'Bob': 13}
# name_and_ages = (['alice', 5], ['Bob', 13])
# dict(name_and_ages)
# {'alice': 5, 'Bob': 13}


# a = {'alice': [1, 2, 3], 'bob': 20, 'tony': 15, 'suzy': 30}
# a.update({'bob':99, 'tony':99, 'kim': 30})
# a
# {'alice': [1, 2, 3], 'bob': 99, 'tony': 99, 'suzy': 30, 'kim': 30}


a = {'alice': [1, 2, 3], 'bob': 99, 'tony': 99, 'suzy': 30, 'kim': 30}
key_list = []
value_list = []
for key, value in a.items():
    key_list.append(key)
    value_list.append(value)

print(key_list)
print(value_list)