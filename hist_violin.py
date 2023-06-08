from matplotlib import pyplot as plt
# x = [1,3,3,3,4,4,6,7,5,2,2,2,2,8,6]
# plt.hist(x,bins=20)
# plt.show()

x = [1,2,3,4,5,6,7,8]
y = [3,4,5,6,7,8,9,3]
z = [6,7,8,9,6,7,8,9]
data= list([x,y,z])

# plt.boxplot(data)  ## will show you min max, 25%, mean and 75% of given set of values##
plt.violinplot(data, showmedians=True)  ## will show you min, max, median if given as True ##
plt.show()
