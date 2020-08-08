#Extract First Names
#Use a list comprehension to create a new list first_names containing just the first names in names in lowercase.

names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]

first_names = [ (fname.split(" ")[0]).lower() for fname in names ]
print(first_names)