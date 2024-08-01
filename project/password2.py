import random
import string

pass_len=8
char_val=string.punctuation+string.ascii_letters+string.digits

password ="".join([random.choice(char_val) for i in range(pass_len)])

print("your password is",password)    