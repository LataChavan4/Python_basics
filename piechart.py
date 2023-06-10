from matplotlib import pyplot as plt

fruits = ["Mango", "Apple", "Peach", "lemon", "chiku"]
quantity = [50, 20, 23, 25, 30]

plt.pie(quantity, labels=fruits, colors=["orange", "red", "green", "yellow", "brown"],  autopct="%.1f%%", radius=1)
plt.pie([10], colors="w", radius=0.5)
plt.show()
