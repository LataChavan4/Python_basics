# Before f string format method was used to get variables

name = 'lata'
city = 'mumbai'
education = 'BE'

info = "I am {}, I live in {} and I have commpleted my education till {}".format(name, city, education)
# You can use index {0},{1},{2} if the sequence of varaible is different or if you want to use single variable multiple time

sentence = "{0} lives in {1} and she has done {2} from {1} university".format(name, city, education)

print(info)
print(sentence)