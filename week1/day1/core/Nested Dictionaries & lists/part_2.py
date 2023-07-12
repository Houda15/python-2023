students = [
    {'first_name': 'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]

def iterateDictionary(some_list):
    for student in some_list:
        output = ""
        for key, value in student.items():
            output += f"{key} - {value}, "
        print(output[:-2])

def iterateDictionary2(key_name, some_list):
    for student in some_list:
        print(student[key_name])

# Calling iterateDictionary
iterateDictionary(students)

# Output:
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

# Calling iterateDictionary2 with 'first_name'
iterateDictionary2('first_name', students)

# Output:
# Michael
# John
# Mark
# KB

# Calling iterateDictionary2 with 'last_name'
iterateDictionary2('last_name', students)

# Output:
# Jordan
# Rosales
# Guillen
# Tonel
