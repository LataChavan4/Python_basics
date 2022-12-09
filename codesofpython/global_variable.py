a = 24
def func():
    a = 8
    print(a)

func()    # will create local variable with new value i.e. 8
print(a)  # value of golbal variable will remain same i'e. 24

