import random
import string

pass_len=8
char_val=string.punctuation+string.ascii_letters+string.digits
password=""
for i in range(pass_len):
    password+=random.choice(char_val)

print("your password is",password)    


