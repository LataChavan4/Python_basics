def greater_than_5(num):
    if num > 5:
        return True
    else:
        return False

l = [1, 23, 4, 66, 90, 2, 43, 0]

print(list(filter(greater_than_5,l)))