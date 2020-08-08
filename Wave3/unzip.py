#Unzip Tuples
#Unzip the cast tuple into two names and heights tuples.

cast = (("Barney", 72), ("Robin", 68), ("Ted", 72), ("Lily", 66), ("Marshall", 76))

# define names and heights here
names = list(zip(*cast))[0]
heights = list(zip(*cast))[1]

print(names)
print(heights)