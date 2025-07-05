# Random Password Generator#

import random
import string
Pass_len = 12

charVal = string.ascii_letters+string.digits+string.punctuation

random.choice(charVal)

password = ""
# for i in range(Pass_len):
#     password +=random.choice(charVal)
# print("Passwprd: ",password)

#List Compherension
res ="".join([random.choice(charVal) for i in range(Pass_len)])
print(res)