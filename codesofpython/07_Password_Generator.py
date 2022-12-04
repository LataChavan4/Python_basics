import string
import random

s = []
s1 = string.ascii_uppercase
s2 = string.ascii_lowercase
s3 = string.punctuation
s4 = string.digits
s.extend(s1)
s.extend(s2)
s.extend(s3)
s.extend(s4)

plen = int(input("Enter the length of the password: "))


print("".join(random.sample(s,plen)))

