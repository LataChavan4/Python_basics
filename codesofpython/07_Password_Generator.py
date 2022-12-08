import string
import random

s = []
s1 = string.ascii_uppercase   #characters in upppercase
s2 = string.ascii_lowercase   #characters on lowercase
s3 = string.punctuation       #Special Characters
s4 = string.digits            # numbers
s.extend(s1)
s.extend(s2)
s.extend(s3)
s.extend(s4)

plen = int(input("Enter the length of the password: "))


print("".join(random.sample(s,plen)))

