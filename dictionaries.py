# dictionaries

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing someting over and over again"
                        }                     
programming_dictionary["Issue"] ="a thing that needs to be done or fixed"
programming_dictionary["Class"]="an object that is created for future use in OOP"


print(programming_dictionary["Bug"])


# programming_dictionary.pop("Issue")
# print(programming_dictionary)
# print(programming_dictionary.keys())
# print(programming_dictionary.items())
# keys=['Bug', 'Issue', 'System']
# for key in keys:
#     programming_dictionary.pop(key, None)

print(programming_dictionary)
# dict={}
# del dict
# programming_dictionary={}
# print(programming_dictionary)

# looping

for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])


