a = 24
def func():
    a = 8
    print(a)

func()    # will create local variable with new value i.e. 8
print(a)  # value of golbal variable will remain same i'e. 24



#****using global variable****

a = 24
def func():
    global a  # use global variable
    print (a) # will print defined value of global variable i.e 24
    a = 8
    print(a)

func()    # will uppdate global variable with new value i.e. 8
print(a)  # value of golbal variable will remain changed i.e 8 


