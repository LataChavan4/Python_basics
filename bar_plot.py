
from matplotlib import pyplot as plt

# students = {"lata":82, "trupti":56, "sai":80}
# name = list(students.keys())
# score = list(students.values())
#
# plt.barh(name, score, color="green")
# plt.title("Marks")
# plt.xlabel("Score")
# plt.ylabel("Names")
# plt.show()

x = [1,2,3,4,5,6,7,8,9]
y = [9,8,7,6,5,4,3,2,1]
z = [3,5,6,8,4,7,1,5,2]

plt.scatter(x,y, c="g", s=60, marker="*")
plt.scatter(x,z, c="r", s=100, marker=".")
plt.show()
