from prettytable import PrettyTable # importing module 
table = PrettyTable()               # creating an object
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])  # adding new column .add_column("Column Heading", [list of items belonging to that column
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"                   # changing alignment of table "l" for left, "c" for center, "r" for right
print(table)
