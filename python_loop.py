def hi(name):
    print('Hi ' + name + "!")

person = {
'name' : 'Ola',
'height' : 155,
"favourite_language":"Python",
}

for element in person:
    print(element)
for element in person.values():
    print(element)
for element in person.items():
    print(element)
for key, value in person.items():
    print('Person\'s ' + str(key) +' is ' + str(value))
