x = [[5, 2, 3], [10, 8, 9]]
x[1][0] = 15
print(x)  # Output: [[5, 2, 3], [15, 8, 9]]

students = [{'first_name': 'Michael', 'last_name': 'Jordan'}, {'first_name': 'John', 'last_name': 'Rosales'}]
students[0]['last_name'] = 'Bryant'
print(students)  # Output: [{'first_name': 'Michael', 'last_name': 'Bryant'}, {'first_name': 'John', 'last_name': 'Rosales'}]

sports_directory = {'basketball': ['Kobe', 'Jordan', 'James', 'Curry'], 'soccer': ['Messi', 'Ronaldo', 'Rooney']}
sports_directory['soccer'][0] = 'Andres'
print(sports_directory)  # Output: {'basketball': ['Kobe', 'Jordan', 'James', 'Curry'], 'soccer': ['Andres', 'Ronaldo', 'Rooney']}

z = [{'x': 10, 'y': 20}]
z[0]['y'] = 30
print(z)  # Output: [{'x': 10, 'y': 30}]
