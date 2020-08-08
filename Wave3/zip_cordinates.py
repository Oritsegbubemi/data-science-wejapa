#Zip Coordinates
#Use zip to write a for loop that creates a string specifying the label and coordinates of each point and appends it to the list points. Each string should be formatted as label: x, y, z. For example, the string for the first coordinate should be F: 23, 677, 4.


x_coord = [23, 53, 2, -12, 95, 103, 14, -5]
y_coord = [677, 233, 405, 433, 905, 376, 432, 445]
z_coord = [4, 16, -6, -42, 3, -6, 23, -1]
labels = ["F", "J", "A", "Q", "Y", "B", "W", "X"]

points = []
# write your for loop here
for point in zip(labels, x_coord, y_coord, z_coord):
    points.append("{0}: {1}, {2}, {3}".format(*point))

for point in points:
    print(point)