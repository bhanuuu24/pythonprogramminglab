
"""my_list = [12, 19, 26, 23]
my_list.append(30)
print(my_list)"""

"""python_datatypes = ["lists"]
python_datatypes.extend(["tuples", "sets"])
print(python_datatypes)"""

"""blue_shades = ['navy', 'sky blue', 'sapphire', 'powder blue', 'teal', 'turquoise']
blue_shades = ['cobalt', 'azure', 'ice blue']
print(blue_shades)"""

"""blue_shades = ['navy', 'sky blue', 'sapphire', 'powder blue', 'teal', 'turquoise']
blue_shades[0:4] = ['denim', 'aqua']
print(blue_shades)"""


"""blue_shades = ['navy', 'sky blue', 'sapphire', 'powder blue', 'teal', 'turquoise']
blue_shades[0:1] = ['denim', 'aqua']
print(blue_shades)"""

"""blue_shades = ['navy', 'sky blue', 'sapphire', 'powder blue', 'teal', 'turquoise']
blue_shades[0:2] = ['denim', 'aqua']
print(blue_shades)"""

"""blue_shades = ['navy', 'sky blue', 'saphire', 'powder blue', 'teal', 'turquoise']
blue_shades[2] = 'sapphire'
print(blue_shades)"""


"""space_movies = ['Interstellar', 'Gravity', 'The Martian', 'Apollo 13', 'Star Wars']
print(space_movies)

del space_movies[2]
print(space_movies)"""


"""space_movies = ['Interstellar', 'Gravity', 'The Martian', 'Apollo 13', 'Star Wars']

del space_movies[1:3]
print(space_movies)"""


"""space_movies = ['Interstellar', 'Gravity', 'The Martian', 'Apollo 13', 'Star Wars']
print(space_movies)

space_movies.remove('Gravity')
print(space_movies)"""

"""space_movies = ['Interstellar', 'Gravity', 'The Martian', 'Apollo 13', 'Star Wars']
print(space_movies)
space_movies.remove('Gravity')
print(space_movies)"""

"""space_movies = ['Interstellar', 'Gravity', 'The Martian', 'Apollo 13', 'Star Wars']
space_movies.clear()
print(space_movies)"""

"""space_movies = ['Interstellar', 'Gravity', 'The Martian', 'Apollo 13', 'Star Wars']

removed_movie = space_movies.pop(2)
print("The removed movie is = " + removed_movie)
print(space_movies)"""


"""my_list = [num for num in range (1,6)]
try:
    element = my_list[10]
except IndexError:
    print("Index is out of range!")"""

"""my_list = [num for num in range (1,6)]
last_element = my_list[-1]
print(last_element)"""

"""my_list = [num for num in range (1,6)]
my_list[start:end]
my_list = [1, 5, 10, 15, 20, 25, 30, 35, 40]
my_new_list = [2:5]
print(my_new_list)"""

"""my_list = [num for num in range (1,6)]
print(my_list)"""

"""my_list = list(["Lists", "are", "useful!"])
print(my_list)"""

"""my_list = [1, 5, 10, 15, 20]
print(my_list)
print([True, False, False, "1"])"""


"""my_list = [1, 5, 10, 15, 20, 25, 30]
print(my_list[0:2])"""

"""my_list = [1, 5, 10, 15, 20, 25, 30]
my_list[0:2] = 50, 55
print(my_list)"""

"""my_list = [1, 5, 10, 15, 20, 25, 30]
print(my_list[1:5:2])"""

"""my_list = [1, 5, 10, 15, 20, 25, 30]
slice_list_from_start = my_list[:4]
print(slice_list_from_start)"""

"""my_list = [1, 5, 10, 15, 20, 25, 30]
slice_list_till_end = my_list[4:]
print(slice_list_till_end)"""

"""my_list = [1, 5, 10, 15, 20, 25, 30]

last_three_elements = my_list[-3:]
print("Last three elements:", last_three_elements)"""

"""my_list = [1, 5, 10, 15, 20, 25, 30]

skip_every_second_from_end = my_list[-1:-6:-2]
print(skip_every_second_from_end)"""

"""numbers = [1, 2, 3, 4, 5]
squares = [num ** 2 for num in numbers]
print(squares)"""

"""numbers = [1, 2, 3, 4, 5]
odd_numbers = [num for num in numbers if num % 2 != 0]
print(odd_numbers)"""

"""words = ["hoodie", "rivers", "cat", "monitor", "bag", "cup"]
short_words = [word for word in words if len(word) <= 5]
print(short_words)"""

"""numbers = [1, 2, 3, 4, 5]
pairs = [(num, num * 2) for num in numbers]
print(pairs)"""

"""songs = ['Neon Lights', 'Pieces', 'Everything']
uppercase_songs = [song.upper() for song in songs]
print(uppercase_songs)"""

"""my_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transpose = [[row[i] for row in my_matrix] for i in range(len(my_matrix[0]))]
print(transpose)"""

"""python_modules = ["NumPy", "Pandas"]

additional_modules = ["Matplotlib", "scikit-learn"]
python_modules.extend(additional_modules)

print(python_modules)"""

"""programming_languages = ["C", "Java", "Python", "Ruby"]
programming_languages.insert(1, "C++")                                 #for inserting in desired indexes

print(programming_languages)"""


"""frameworks = ["Django", "Flask", "Pyramid", "Flask"]
frameworks.remove("Flask")
print(frameworks)"""

"""web_frameworks = ["Django", "Flask", "Pyramid", "FastAPI"]
removed_framework = web_frameworks.pop(2)
print(web_frameworks)"""

"""scripting_languages = ["Python", "Ruby", "Perl"]
scripting_languages.clear()
print(scripting_languages)"""

"""languages = ["C", "C++", "Python", "Java", "Python"]
python_index = languages.index("Python")
print(python_index)"""

"""version_numbers = [2, 3, 3, 3, 3, 3, 3, 3, 3, 3]
python3_count = version_numbers.count(3)
print(python3_count)"""

"""numeric_versions = [2.2, 2.7, 3.0, 5.9, 3.6, 3.7, 3.8, 3.9]
numeric_versions.sort()
print(numeric_versions)"""

"""libraries = ["NumPy", "Pandas", "Matplotlib", "Scikit-Learn"]
libraries.reverse()
print(libraries)"""

"""original_list = ["Python", "is", "so" , "cool"]
copied_list = original_list.copy()
print(copied_list)"""

