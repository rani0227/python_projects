import enchant
from itertools import permutations as p
d=enchant.Dict("en_US")
print("This is my test program")
word=input("enter your letters :")
not_found=True
for combination in list(p(word)):
    words=''.join(combination)
    if d.check(words):
        print(words)
        not_found=False
if not_found:
        print("No combination found")    
