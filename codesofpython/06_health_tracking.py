def getdate ():
    import datetime
    return datetime.datetime.now ()
    
time = getdate()


def getData():
    name = input("Enter your name: ")
    action = input("Select whether you want to update Diet(D) or Excersice(E): ")
    with open(f'{name}_{action}.txt','w') as f:
            f.write(str(time) +'\n')
    if action == 'D':
        diet = input('Enter the food you have eaten: ')
        with open(f'{name}_{action}.txt','a') as f:
            f.write(diet)
    elif action == 'E':
        excercise =input("Enter the name of excercise you have done: ")   
        with open(f'{name}_{action}.txt','a') as f:
             f.write(excercise)
    else:
        print("Please enter a valid input")         

getData()










        

print(getdate())