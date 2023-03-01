numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# we can use items of existing list to create new list without using loop ##
squared_numbers = [num * num for num in numbers]
print(squared_numbers)


# Filter out even numbers using list comprehension ##
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [num for num in numbers if num%2 == 0]
print(squared_numbers)

